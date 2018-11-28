#include<iostream>
#include<stdio.h>
#include<cstring>
#include<stdlib.h>
#include<cmath>
#include<vector>
#include<algorithm>
#include<map>
#include<functional>
#include<stack>
#include<set>
#include<queue>
#include<fstream>

using namespace std;

int a[1000][1000];
int m,n;

bool check(int row,int col)
{
    bool flag1 = true,flag2 = true;
    for (int i=0;i<n;i++ )
    {
    	if(a[row][i]>a[row][col])
    	{
    	    flag1 = false;
    	}
    }
    for (int i=0;i<m;i++ )
    {
    	if(a[i][col]>a[row][col])
    	{
    	    flag2 = false;
    	}
    }
    return (flag1||flag2);

}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
	int test;
	cin>>test;

	for(int testno = 0; testno < test ; testno++ )
	{

		cin>>m>>n;

		for (int i=0;i<m;i++ )
		{
			for (int j=0;j<n;j++ )
			{
				cin>>a[i][j];
			}
		}

		bool flag = true;
		for (int i=0;i<m;i++ )
		{
			for (int j=0;j<n;j++ )
			{
				if(check(i,j)==false)
				{
				    flag = false;
				    break;
				}
			}
			if(flag == false)
			{
			    break;
			}
		}
		if(flag == true)
		{
		    cout<<"Case #"<<testno+1<<": YES\n";
		}
		else
		{
		    cout<<"Case #"<<testno+1<<": NO\n";
		}


	}
}
