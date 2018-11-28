#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<vector>
#include<set>
#include<math.h>
#include<map>
#include<algorithm>
#include<queue>
#include<cstring>
#include<stack>
using namespace std;

int main()
{
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	int id=1;
	cin>>t;
	while(t--)
	{
		long long a,aa;
		cin>>a;
		
		vector<int>F(10,0);
		int cnt=0,l=1;
		
		if(a==0)
		{
			cout<<"Case #"<<id<<": "<<"INSOMNIA\n";
			id++;
			continue;
		}
		aa=a;
		
		while(1)
		{
			long long tmp=aa;
			while(tmp!=0)
			{
				int re=tmp%10;
				if(F[re]==0)
				{
					F[re]=1;
					cnt++;
				}
				tmp=tmp/10;
			
			}
				if(cnt>=10)
				break;
			l++;
			aa=a*l;
		}
		
			cout<<"Case #"<<id<<": "<<a*l<<"\n";
			id++;
	}
}
 

