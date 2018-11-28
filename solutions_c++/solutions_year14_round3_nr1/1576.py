#include <iostream>
#include <fstream>
#include <cstdio>
#include <math.h>
#include <vector>
#include <string.h>
#include <algorithm>
#include <climits>
#define MAX(a,b) a>b?a:b;
#define MIN(a,b) a<b?a:b;
typedef long long int lld;
using namespace std;

lld gcd(lld a, lld b)
{
    for (;;)
    {
        if (a == 0) return b;
        b %= a;
        if (b == 0) return a;
        a %= b;
    }
}

lld lcm(lld a, lld b)
{
    lld temp = gcd(a, b);

    return temp ? (a / temp * b) : 0;
}

int main()
{
	lld t,a,b,x=0,i,n,ans,temp;
	
	char s[100];
	cin>>t;
	while(t--)
	{
		x++;
		cin>>s;
		a=b=i=ans=0;
		while(s[i]!='/')
		{
			a=a*10+(s[i]-'0');
			i++;
		}
		i++;
		n=strlen(s);
		while(i!=n)
		{
			b=b*10 + (s[i] - '0');
			i++;
		}
		
		temp=gcd(a,b);
		temp=b/temp;
		while(temp%2==0)
		{
			temp/=2;
		}
		if(temp==1)
		{
		
		while(a<b)
		{
			a*=2;
			ans++;
		}
		cout<<"Case #"<<x<<": "<<ans<<endl;
		}
		
		else 
		cout<<"Case #"<<x<<": impossible"<<endl;
		
	}
	
	return 0;
}
