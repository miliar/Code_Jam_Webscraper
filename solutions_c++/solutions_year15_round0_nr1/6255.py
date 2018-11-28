#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#define lli long long int
#define gc getchar

using namespace std;

void scan(lli &x)
{
    register lli c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output1.txt","w",stdout);
	lli t,n,num,need,ans;
	string str;
	scan(t);
	for(lli z=1;z<=t;z++)
	{
		need=0;ans=0;
		scan(n);
		cin>>str;
		num=0;
		for(lli i=0;i<str.length();i++)
		{
			if(num>=i)
			{
				
				num+=((int)str.at(i)-48);
			}
			else
			{
				need=(i-num);
				ans+=need;
				num+=((int)str.at(i)-48)+need;
			}
			
		}
		cout<<"Case #"<<z<<": "<<ans<<endl;
	}
	return 0;
}
