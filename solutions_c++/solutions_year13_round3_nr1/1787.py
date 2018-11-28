#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
using namespace std;
int main()
{
	int T;
	scanf("%d",&T);
	string s;
	int n;
	for(int iter=0;iter<T;iter++)
	{
		cin>>s>>n;
		int count=0;
		for(int i=0;i<s.size();i++)
		{
			for(int j=i;j<s.size();j++)
			{
				int cnt=0;
				for(int k=i;k<=j;k++)
				{
					if(s[k]!='a' && s[k]!='e' && s[k]!='i' && s[k]!='o' && s[k]!='u')
					{
						cnt++;
						if(cnt==n)
						{
						//	for(int l=i;l<=j;l++)
							//	cout<<s[l];
						//	cout<<"\n";
							count++;
							break;
						}
					}
					else
						cnt=0;
				}
			}
		}
		cout<<"Case #"<<iter+1<<": "<<count<<"\n";
		
	}
}

