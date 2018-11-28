#include <cstdio>
#include <sstream>
#include <vector>
#include <list>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <functional>
#include <cstdlib>
#include <stack>
#include <queue>
#include <string>
#include <climits>

#pragma once
using namespace std;

void main()
{
	freopen("input.txt","r",  stdin);
	freopen("output.txt", "w", stdout);

	int T = 0;
	bool w = false;
	int N,M;
	vector< vector<int> > lawn;

	cin>>T;

	for(int t = 1; t <= T; t++)
	{
		cin>>N>>M;
		vector<int> listN;
		for(int i = 0; i < N; i++) 
		{
			for(int j = 0; j < M; j++) 
			{
				int v;
				cin>>v;
				listN.push_back(v);
			}
			lawn.push_back(listN);
			listN.clear();
		}		
		bool check1,check2,done;
		for(int r=0;r<N;r++)
		{
			done=false;
			for(int c=0;c<M;c++)
			{
				check1=true;
				check2=true;
				if ( lawn[r][c]==1)
				{
					for (int i=0;i<M;i++)
					{
						if( lawn[r][i]==2)
						{
							check1 =false;
							break;
						}
					}
					if(!check1)
					{
						for(int j=0;j<N;j++)
						{
							if (lawn[j][c]==2)
							{
								check2=false;
								break;
							}
						}
					}

				}//if ( lawn[r][c]==1)
				if(check1==false && check2== false)
				{
					cout<<"Case #"<<t<<": NO"<<endl;
					done=true;
					break;
				}
				
			}//for(int c=0;c<M;c++)

			if(done)break;
			
		}//for(int r=0;r<N;r++)
		
		if(!done)
		{
			cout<<"Case #"<<t<<": YES"<<endl;
		}
		lawn.clear();
	}//for(int t = 1; t <= T; t++)
}