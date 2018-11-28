#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<vector>
#include<cstring>
using namespace std;

int m, n;
int grid[4][4];
int record[4];

void Input()
{
}

void Solve()
{
}

int main()
{
	int T;
	cin>>T;
	for (int c = 1; c <= T; c++) {
		Input();
		Solve();
		int count = 0;
		int num = 0;
		cin>>m;
		for (int i = 0; i < 4; i++)  {
			for (int j = 0; j < 4; j++)  {
				cin>>grid[i][j];
			}
		}
		for (int i = 0; i < 4; i++)  {
			record[i] = grid[m-1][i];
		}
		cin>>n;
		for (int i = 0; i < 4; i++)  {
			for (int j = 0; j < 4; j++)  {
				cin>>grid[i][j];
			}
		}
		for (int i = 0; i < 4; i++)  {
			for (int j = 0; j < 4; j++) {
				if (grid[n-1][i] == record[j]) {
					num = record[j];
					count++;
				}
			}
		}
		if (count == 1) {
			cout<<"Case #"<<c<<": "<<num<<endl;
		} else if (count >= 1) {
			cout<<"Case #"<<c<<": Bad magician!"<<endl;
		} else if (count == 0) {
			cout<<"Case #"<<c<<": Volunteer cheated!"<<endl;
		}
	}
	return 0;
}
