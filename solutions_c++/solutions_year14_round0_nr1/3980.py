#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std; 

const int arr_size=4;
struct node
{
	int arrangement1 [arr_size] [arr_size];
	int arrangement2 [arr_size] [arr_size];
	int selection1;
	int selection2;
	node(): selection1(0), selection2(0)
	{
	}
};

int do_something (node *my, int &answer)
{
	int count=0;
	for (int x=0;x<arr_size;x++)
	{
		for (int y=0;y<arr_size;y++)
		{
			if (my->arrangement1[my->selection1][x] == my->arrangement2[my->selection2][y])
			{
				answer = my->arrangement1[my->selection1][x];
				count++;
			}
		}
	}

	return count;
}

int main ()
{
	
	try{
		ifstream fin;
		ofstream fout;
		fout.open("output.txt");
		fin.open("A-small-attempt1.in");
		
		if (!fin.is_open() || !fout.is_open())
			throw "Input or output file not opening exception";
		else
		{
			int size=0;
			fin >> size;

			for (int x=0;x<size && fin.good();x++)
			{
				node * current_node = new node();
				int ans1=0,ans2=0;
				fin >> ans1;

				for (int i=0;i<arr_size;i++)
				{
					for (int j=0;j<arr_size;j++)
					{
						int temp =0;
						fin >> temp;
						current_node->arrangement1[i][j] = temp;
					}
				}

				fin >> ans2;

				for (int i=0;i<arr_size;i++)
				{
					for (int j=0;j<arr_size;j++)
					{
						int temp =0;
						fin >> temp;
						current_node->arrangement2[i][j] = temp;
					}
				}

				current_node->selection1=ans1-1;
				current_node->selection2=ans2-1;

				int answer=0;
				int c = do_something(current_node, answer);

				fout <<"Case #" <<x+1<<": ";
				if ( c==1)
				{
					fout << answer;
				}
				else if ( c>1 && c<5)
				{
					fout << "Bad magician!";
				}
				else if ( c==0)
				{
					fout << "Volunteer cheated!";
				}
				else
					fout <<"you just cheated";

				fout <<endl;

			}
		}
	}
	catch (string a)
	{
		cout <<endl << "EXCEPTION : " << a <<endl;
	}
	return 0;
}
