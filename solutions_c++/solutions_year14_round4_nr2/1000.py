#include <fstream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

int T;
int N;

void findmin(vector<int> A, int start, int end, int &pos)
{
	pos = start;
	int minval = A[pos];
	for (int i = start; i <= end; i++)
		if(minval > A[i])
		{
			minval = A[i];
			pos = i;
		}
}

void swap(int &x, int &y)
{
	int tmp = x;
	x = y;
	y = tmp;
}

void main()
{
	ifstream fin("B-large.in");
	ofstream fout("out.txt");
	fin >> T;
	for (int i = 0; i != T; i++)
	{
		fout << "Case #" << i+1 << ": ";
		fin >> N;
		vector<int> A(N,0);
		for (int j = 0; j != N; j++)
			fin >> A[j];
		int pos;
		
		int y = 0;
		int start = 0;
		int end = N-1;
		while(start < end)
		{
			findmin(A,start,end,pos);
			if(pos-start < end-pos)
			{
				y += pos-start;
				for(int j = pos; j >= start+1; j--)
					swap(A[j],A[j-1]);
				start++;
			}
			else
			{
				y += end-pos;
				for(int j = pos; j <= end-1; j++)
					swap(A[j],A[j+1]);
				end--;
			}
		}
		fout << y << endl;
	}
	fin.close();
	fout.close();
}