#include<bits/stdc++.h>
using namespace std;
#define f_in(st) freopen(st,"r",stdin);
#define f_out(st) freopen(st,"w",stdout);
int main()
{
	f_in("B-large.in");
    f_out("B-largeout.txt");
	long long t,j,len,i;
	cin>>t;
	string s;
	getchar();
	for(j=1;j<=t;j++)
	{
		cin>>s;
		long long count=0;
		cout<<"Case #"<<j<<": ";
		len=s.length();
		char ch=s[0];
		for(i=1;i<len;i++)
		{
			if(s[i]!=ch)
			{
				count++;
				ch=s[i];
			}
		}
		if(ch=='-')
		{
			count++;
		}
		cout<<count<<endl;
	}
	return 0;
}

