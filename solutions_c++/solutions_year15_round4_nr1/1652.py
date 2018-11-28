#include<iostream>
#include<cstdio>
#include<vector>
#include<cstring>
#include<queue>
#include<map>
#include<set>
#include<algorithm>
#include<stack>
#include<cmath>
#include<iomanip>
#include<cstdlib>
#include<sstream>
#include<climits>
using namespace std;

string a[200];
int vis[200][200];

int main()
{
	std::ios::sync_with_stdio(false); 

	long long int n, i, j, k, l ,t, ct = 0, flag, y, q, m, ans, r, c, store, storex, storey;
	
	cin>>t;

	while(t--)
	{
		ct++;
		cin>>r>>c;
		
		ans = 0;
		
		for(i = 0; i < r; i++)
		{
			cin>>a[i];
		}
		
		ans = 0;
		
		for(i = 0; i < r; i++)
		{
			for(j = 0; j < c; j++)
			{
				if(a[i][j] == '^')
				{
					flag = 0;
					
					for(k = i - 1; k >= 0; k--)
					{
						if(a[k][j] != '.')
						{
							flag = 1;
							break;
						}
					}
					
				//	cout<<i<<" "<<j<<" "<<flag<<endl;
					if(flag == 0)
					{
						ans++;
					}
				}

				if(a[i][j] == 'v')
				{
					flag = 0;
					
					for(k = i + 1; k < r; k++)
					{
						if(a[k][j] != '.')
						{
							flag = 1;
							break;
						}
					}
					
					if(flag == 0)
					{
						ans++;
					}
				}

				if(a[i][j] == '>')
				{
					flag = 0;
					
					for(k = j + 1; k < c; k++)
					{
						if(a[i][k] != '.')
						{
							flag = 1;
							break;
						}
					}
					
					if(flag == 0)
					{
						ans++;
					}
				}

				if(a[i][j] == '<')
				{
					flag = 0;
					
					for(k = j - 1; k >= 0; k--)
					{
						if(a[i][k] != '.')
						{
							flag = 1;
							break;
						}
					}
					
					if(flag == 0)
					{
						ans++;
					}
				}								
			}
		}

		store = ans;
		ans = 0;
		
		int flag;
		
	//	cout<<r<<" "<<c<<endl;
		for(i = 0; i < r; i++)
		{
			for(j = 0; j < c; j++)
			{
				flag = 0;
				
				if(a[i][j] == '.')
				{
					flag = 1;
					continue;
				}
				
				for(k = j + 1; k < c; k++)
				{
					if(a[i][k] != '.')
					{
						flag = 1;
						break;
					}
				}			
				
				if(flag == 1)
				{
					continue;
				}
				
				for(k = j - 1; k >= 0; k--)
				{
					if(a[i][k] != '.')
					{
						flag = 1;
						break;
					}
				}			

				if(flag == 1)
				{
					continue;
				}

				for(k = i + 1; k < r; k++)
				{
					if(a[k][j] != '.')
					{
						flag = 1;
						break;
					}
				}			

				if(flag == 1)
				{
					continue;
				}

				for(k = i - 1; k >= 0; k--)
				{
					if(a[k][j] != '.')
					{
						flag = 1;
						break;
					}
				}			

				if(flag == 1)
				{
					continue;
				}

				if(flag == 0)
				{
					break;
				}
				
				flag = 1;
			}
			
			if(flag == 0)
			{
				break;
			}
			
			flag = 1;
		}
			
		if(flag == 1)
		{
			cout<<"Case #"<<ct<<": "<<store<<endl;
		}
		
		else
		{
			cout<<"Case #"<<ct<<": "<<"IMPOSSIBLE"<<endl;
		}
	}
	
	return 0;
}
