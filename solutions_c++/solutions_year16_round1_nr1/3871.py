#include<bits/stdc++.h>
#define lli long long int
#define gc getchar_unlocked
#define MOD 1000000007
using namespace std;


void scan(lli &x)
{
    register lli c = gc();
    x = 0;
    lli neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}


int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	lli t;
	string str,ans;
	cin>>t;
	for(lli i=1;i<=t;i++)
	{
		cout<<"Case #"<<i<<": ";
		lli len;
		cin>>str;
		len=str.length();
		ans="";
		ans=ans+str[0];
		for(lli j=1;j<=len;j++)
		{
			if(str[j]>=ans[0])
			{
				ans=str[j]+ans;
			}
			else
			{
				ans=ans+str[j];
			}
		}
		cout<<ans<<endl;
	}
    return 0;
}
