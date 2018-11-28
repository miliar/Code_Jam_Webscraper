#include <iostream>
#include <algorithm>
#include <math.h>
#include <stdio.h>
#include <vector>
#include <bits/stdc++.h>	
using namespace std;
//TODO
int main()
{
	int t;
	scanf("%d",&t);
	int count=0;
	
	while(count<t)
	{
		int Smax;
		string s;

		cin>>Smax;
		cin>>s;

		int ans=0;
		int total=0;
		for(int i=0;i<Smax;i++)
		{
			total+=(s[i]-48);
			if(total>=i+1&&s[i+1]!=0)continue;
			else if(total<i+1&&s[i+1]!=0)
			{
				int tmp=i+1-total;
				ans+=tmp;
				total+=tmp;
			}
			else continue;
		}

		cout<<"Case #"<<count+1<<": "<<ans<<endl;
		count++;
	}
}