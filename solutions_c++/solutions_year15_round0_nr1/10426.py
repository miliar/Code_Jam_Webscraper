#include<stdlib.h>
#include<vector>
#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<string.h>
#include <iostream>
using namespace std;
inline void readint(int &x) {
    register int c = getchar_unlocked();
    x = 0;
    int neg = 0;
    for(; ((c<48 || c>57) && c != '-'); c = getchar_unlocked());
    if(c=='-') {
        neg = 1;
        c = getchar_unlocked();
    }
    for(; c>47 && c<58 ; c = getchar_unlocked()) {
        x = (x<<1) + (x<<3) + c - 48;
    }
    if(neg)
        x = -x;
}
long long int mod=1000003;
typedef long long int ll;
int main() 
{
 
ll t,n,j;
cin>>t;
for(j=1;j<=t;j++)
{
	cin>>n;
	ll s[n+1],i,count=0,sum=0;
	char a[100000];
	cin>>a;
	for(i=0;i<n+1;i++)
	{
		s[i]=(a[i]-'0');
	}
	count=s[0];
	for(i=1;i<n+1;i++)
	{
	//	if(s[i]==0)
	//	continue;
		if(count<i)
		{
			sum++;
		count+=s[i]+1;
         }
		else //if(s[i]!=0) 
		count=count+s[i];
	//cout<<i<<" "<<count<<" "<<sum<<endl;
	}
	cout<<"Case #"<<j<<": "<<sum<<endl;
}
return 0;
}  