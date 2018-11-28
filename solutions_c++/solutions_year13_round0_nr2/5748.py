#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int judgeRow(int**,int ,int,int,int );
	int judgeCol(int**,int ,int,int,int );
    ofstream fo("output.txt");
    ifstream fi("data.txt");
	int cases;
	fi >> cases;
	int i=0;
	for(i;i<cases;++i)
	{
begin:
		if(i== cases)
			break;
		int n,m,min;
		fi >> n >> m;
		if((n == 1) ||(m==1))
		{
			int temp;
			for(int j=0;j<n*m;++j)
				fi >> temp;
			fo << "Case #" << i+1 << ":" << " YES" << endl;
		}
		else
		{
			int** ans = new int*[n];
			int** conn = new int*[n];
			for(int j=0;j<n;++j)
			{
				ans[j] = new int[m];
				conn[j] = new int[m];
			}
			int min=1000;
			int max=0;
		
			for(int j=0;j<n;++j)
			{
				for(int k=0;k<m;++k)
				{
					fi >> ans[j][k];
					if(ans[j][k] < min)
						min = ans[j][k];
					if(ans[j][k]>max)
						max = ans[j][k];
					conn[j][k] = 0;
			//		cout << conn[j][k] << " ";
					cout << "ans " << ans[j][k];
				}
				cout << endl;

			}
		    for(int j=0;j<n;++j)
			{
				for(int k=0;k<m;++k)
				{
					if(judgeRow(ans,j,k,n,m) || (judgeCol(ans,j,k,n,m)))
					{
						conn[j][k] =1;
					}
					if((conn[j][k] == 0) && (ans[j][k] <max))
					{
						fo << "Case #" << i+1 << ":" << " NO" << endl;
						i++;
						goto begin;
					}
				}
			}
			fo << "Case #" << i+1 << ":" << " YES" << endl;
			delete ans;
		}
	}

	fi.close();
	fo.close();
	return 0;
}
int judgeCol(int** ans,int j ,int k,int n, int m)
{
	for(int jj=0;jj<n;++jj)
	{
		if(ans[j][k] != ans[jj][k])
		{
			return 0;
		}
	}
	return 1;
}
int judgeRow(int** ans,int j ,int k,int n, int m)
{
		for(int jj=0;jj<m;++jj)
	{
		if(ans[j][k] != ans[j][jj])
		{
			return 0;
		}
	}
		return 1;
}