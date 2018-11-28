//============================================================================
// Name        : CodeJam.cpp
// Author      : diametralis
// Version     :
// Copyright   : Your copyright notice
// Description : Code Jam contest
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <vector>
using namespace std;

#define MAX 100

class LM
{
public:
	void solve()
	{
		ifstream infile("input");
		ofstream outfile("output");
		if(!infile.is_open())
			cout<<"error while opening";

		int T;
		infile>>T;
		for(int i=0; i<T; ++i)
		{
			int N, M;
			infile>>N;
			infile>>M;
			memset(num, 0, sizeof(num));
			for(int j=0; j<N; ++j)
			{
				for(int n=0; n<M; ++n)
				{
					int next;
					infile>>next;
					arr[j][n]=next;
					num[next]=1;
				}
			}

			string res=calc(N, M);

			outfile<<"Case #"<<(i+1)<<": "<<res<<endl;
		}

		infile.close();
		outfile.close();
	}
private:
	int arr[MAX][MAX];
	int num[MAX+1];

	string calc(int N, int M)
	{
		int usedR[MAX];
		int usedC[MAX];
		memset(usedR, 0, sizeof(usedR));
		memset(usedC, 0, sizeof(usedC));

		for(int cur=0; cur<MAX+1; ++cur)
		{
			if(num[cur]==1)
			{
				while(true)
				{
					int fi, fj;
					find(fi, fj, cur, usedR, usedC, N, M);

					if(fi==-1 && fj==-1)
					{
						num[cur]=0;
						break;
					}

					//in fi and fj cur value
					bool rowOk=true;
					//check row
					for(int j=0; j<M; ++j)
					{
						if(arr[fi][j]>cur)
						{
							rowOk=false;
							break;
						}
					}
					if(rowOk)
					{
						usedR[fi]=1;
						continue;
					}
					for(int i=0; i<N; ++i)
					{
						if(arr[i][fj]>cur)
						{
							return "NO";
						}
					}
					usedC[fj]=1;
				}
			}
		}


		return "YES";
	}

	void find(int &fi, int &fj, int cur, int *usedR, int *usedC, int N, int M)
	{
		//find cur
		fi=-1;
		fj=-1;

		for(int i=0; i<N; ++i)
		{
			if(usedR[i]==0)
			{
				for(int j=0; j<M; ++j)
				{
					if(usedC[j]==0)
					{
						if(arr[i][j]==cur)
						{
							fi=i;
							fj=j;
							return;
						}
					}
				}
			}
		}
	}
};

int main() {
	LM lm;
	lm.solve();
	cout << "done" << endl;
	return 0;
}
