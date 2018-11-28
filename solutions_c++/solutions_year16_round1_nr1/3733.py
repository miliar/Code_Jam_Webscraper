//Author:Hena Firdaus
#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
typedef pair<int,int> ii;
#define fr(i,a,b) for(i=a;i<b;i++)
int main()
{
	int t;
	string s;
	freopen("in1.txt","r",stdin);
	freopen("out1.txt","w",stdout);
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>s;
		string a="";
		a+=s[0];
		
		for(int j=1;j<s.length();j++)
		{
			if(s[j] >= a[0])
			{
				string t=""; t+=s[j];
				a=t+a;
			}
			else
				a+=s[j];
		}
		cout<<"Case #"<<i<<": "<<a<<endl;
	}
	return 0;
}

