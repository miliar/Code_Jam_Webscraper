using namespace std;
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <climits>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <string>

typedef long long L;
typedef unsigned long long U;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
string str[10];
int arr[10];
int m, n;
int mc,f;
void cost()
{
	/*for(int i = 0;i<n;i++)
		cout<<arr[i]<<" ";
	cout<<endl;*/
	int cst = 0;
	for(int i = 0;i<n;i++)
	{
		int m = 0;
		bool flag = 1;
		for(int j = 0;j<i;j++)
		{
			if(arr[i] == arr[j])
			{
				flag = 0;
				int c= 0;
				for(int k = 0;k<min(str[i].length(),str[j].length());k++)
				{
					if(str[i][k] == str[j][k])
						c++;
					else
						break;
				}
				m = max(m,c);
			}
		}
		cst += (str[i].length() - m);
		cst += flag;
		//cout<<str[i]<<" "<<(str[i].length() - m)<<endl;
	}
	//cout<<"Cost = "<<cst<<endl;
	if(cst > mc)
	{
		mc = cst;
		f = 1;
	}
	else if(cst == mc)
		f++;
}
void func(int x)
{
	if(x == n)
	{
		cost();
	}
	else
	{
		for(int i = 0;i<m;i++)
		{
			arr[x] = i;
			func(x+1);	
		}
	}
}
main()
{
	int tc;
	cin>>tc;
	for(int t = 1;t <=tc;t++)
	{
		cin>>n>>m;
		for(int i = 0;i<n;i++)
		{
			cin>>str[i];
		}
		f = 0;
		mc = 0;
		func(0);
		printf("Case #%d: %d %d\n", t, mc, f);
	}
}
