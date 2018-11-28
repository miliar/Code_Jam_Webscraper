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

lli checkrev(string a,lli j)
{
	if(a[j]!=a[0])
		return 1;
	else
		return 0;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	lli test,len,count;
	string str;
	cin>>test;
	for(lli i=1;i<=test;i++)
	{
		count=0;
		cout<<"Case #"<<i<<": ";
		cin>>str;
		len=str.length();
		lli val=0;
		lli z=0;
		while(str[z++]=='-')
		{
			val=1;;
		}
		if(val==1)
			count++;
		for(lli j=z;j<len-1;j++)
		{
			if(str[j]=='-')
			{
				while(str[j]==str[j+1])
					j++;
				count+=2;
			}	
		}
		if(str[len-2]=='+' && str[len-1]=='-')
			count+=2;
		cout<<count<<endl;
	}
	
    return 0;
}
