#include<iostream>
#include<vector>
#include<fstream>
#include<queue>

using namespace std;
vector < vector <int> > grid;
vector < vector <bool> > locked;
vector < vector <int> > field;
int rows, cols;
bool possible;
typedef pair<int, int> patch;
priority_queue<patch, vector <patch>, less <patch> > toSort;
int main()
{
	int testCases=0;
	freopen("input.txt","r", stdin);
	freopen ("output.txt", "w", stdout);
	scanf("%d", &testCases);
	for (int a=0; a<testCases; a++)
	{
		possible=true;
		grid.clear();
		vector <patch> t(0);
		t.clear();
		toSort=priority_queue<patch, vector <patch>, less <patch> > (t.begin(),t.end());
		scanf("%d %d", &rows,&cols);		
		for (int row=0; row<rows;row++)
		{
			grid.push_back(vector <int> (0));
			for (int col=0; col<cols; col++)
			{
				int grassLength;
				scanf("%d", &grassLength);
				grid[row].push_back(grassLength);
				toSort.push(make_pair(grassLength,row*cols+col));
			}
		}
		
		locked= vector < vector <bool> > (rows, vector <bool> (cols, false));
		field= vector < vector <int> > (rows, vector <int> (cols,100));
		int solved=0;
		int current;
		while (solved!=rows*cols)
		{
			patch current=toSort.top();
			toSort.pop();
			int row=current.second/cols;
			int col=current.second%cols;
			int grassLength=current.first;
			if (field[row][col]!=grassLength)
			{
				//try row
				vector <int> temp(0);
				bool found=false;
				int miniCounter=0;
				for (int ab=0;ab<cols;ab++)
				{
					
					if (grassLength<grid[row][ab])
						break;
					else 
					{
						if (grassLength==grid[row][ab]&&field[row][ab]!=grassLength)
							miniCounter++;
						 temp.push_back(grassLength);
					}
				}
				if (temp.size()==cols)
				{
					field[row]=temp;
					solved+=miniCounter;
					found=true;
				}
				// try col
				temp.clear();
				miniCounter=0;
				bool right=true;
				
				for (int ab=0;ab<rows;ab++)
				{
					
					if (grassLength<grid[ab][col])
					{
						right=false;
						break;
					}
					else if (grassLength==grid[ab][col]&&field[ab][col]!=grassLength)
						miniCounter++;
					
				}
				if (right)
				{
					for (int ab=0;ab<rows;ab++)
					{
						field[ab][col]=grassLength;
					
					}
					solved+=miniCounter;
					found=true;
				}
				if (!found)
				{
					possible=false;
					break;
				}
			}

		}
		printf("Case #%d: ",a+1);
		if (possible) printf("YES\n");
		else printf("NO\n");

	}

}