// Lawnmower.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("E:/google code jam/Lawnmower/b.in", "r", stdin);
    freopen("E:/google code jam/Lawnmower/b.out", "w", stdout);
	int caseNo;
	int m,n;
	int arr[10][10];
	bool mflag = true, nflag = true,flag = true;
	cin>>caseNo;
	for(int cno = 0; cno < caseNo; cno++)
	{
		cin>>m;
		cin>>n;		
		for(int i = 0; i < m; i++)
			for(int j = 0; j < n; j++)
				cin>>arr[i][j];
		//¥¶¿Ì
		for(int i = 0; i < m; i++)
		{
			for(int j = 0; j < n; j++)
			{
				mflag = true;
				nflag = true;
				flag = true;
				if(arr[i][j] == 1)
				{
					flag = false;
					int jtmp = j+1;	
					for(int r = 1; r < n; r++)
					{
											
						if(arr[i][(jtmp++)%n] == 2)
						{
							mflag = false;
							//flag = false;
						}
					}
					int itmp = i+1;
					for(int c = 1; c < m; c++)
					{
						
						if(arr[(itmp++)%m][j] == 2)
						{
							nflag = false;
						}
					}
					
				}
				if(flag == false && mflag == false && nflag == false)
					break;
			}
			if(flag == false && mflag == false && nflag == false)
					break;
		}
		if(flag == false && mflag == false && nflag == false)
			cout<<"Case #"<<cno+1<<": "<<"NO"<<endl;
		else cout<<"Case #"<<cno+1<<": "<<"YES"<<endl;
		
	}
	return 0;
}

