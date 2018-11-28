#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstdlib>
#include <string>
#include <utility>
#include <algorithm>
using namespace std;

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int t,n,c;
	cin>>t;
	for(int z=0;z<t;z++)
	{
		cin>>n>>c;
		vector <int> fil(n);
		vector <bool> tak(n);
		for(int i=0;i<n;i++) {cin>>fil[i]; tak[i]=false;}
		sort(fil.begin(),fil.end());
		int ans=0;
		int low=0;
		for(int i=n-1;i>=0;i--)
		{
			if(tak[i]) break;
			if(low < i && fil[low]+fil[i]<=c) 
			{
				ans++;
				tak[low++]=true;
			}
			else ans++;
		}
		cout<<"Case #"<<z+1<<": "<<ans<<endl;
	}
	return 0;
}
