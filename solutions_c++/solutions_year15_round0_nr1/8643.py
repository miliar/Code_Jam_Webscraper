#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
#include<set>
#include<queue>
#include<cmath>
#include<stdio.h>
#include<fstream>
#include <stdio.h>
#include <string.h>

#define fori(i,n) for(int i=1;i<=n;i++)
#define pb push_back
#define mp make_pair

typedef long long LL;

using namespace std;

const LL INF=1000000009;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int T;
	cin>>T;
	
	for(int t=1;t<=T;t++)
	{
		int n;
		cin>>n;
		
		string s;
		cin>>s;
		
		int ans=0;
		int c=0;
		c=s[0]-'0';
		for(int i=1;i<s.size();i++)
		{
			if(i>c){
				ans+=i-c;
				c+=i-c;
				c+=s[i]-'0';
			}
			else {
				c+=s[i]-'0';
			}
			
			
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
}
