#include<bits/stdc++.h>
#include<limits>
#include<fstream>
#define ge getchar 
#define pc(x) putchar(x)
#define max(a,b) a>b?a:b
#define mod 1000000007
#include<map>
#include<vector>
#define ll  int
ll scani();
using namespace std;
inline ll min(ll a,ll b)
{
	if(a>b)
	return b;
	return a;
}
ll powe(ll a, ll b)
{
    ll res = 1, y = a;
    while(b)
    {
        if(b&1)
            res = (res * y);
        y = (y * y);
        b >>= 1;
    }

    return res;
}
int main()
{
	ll t = scani(),k=0;
	ofstream pno;
	pno.open("outputgooglel2.txt");
	while(t--)
	{
		k++;
		ll  max;
		cin>>max;
		char arr[max+3];
		cin>>arr;
		ll ans=0,num=0,i,a;
		for(i=0;i<=max;i++)
		{
		if(num>=i)
			num = num + arr[i]-'0';
		else
		{   a = ans;
			ans = ans + i - num;
			num = num + arr[i]-'0' + ans - a;
		}
		}
		pno<<"Case #"<<k<<": "<<ans<<endl;
	}
	return 0;
}
ll scani()
{
	ll  x=0;
  	 int neg=0;
	register int c=ge();
	for(;((c<'0' || c>'9') && c!='-');c=ge());
	if(c=='-')
	{neg=1;
	c=ge();
	}
	for(;c>='0' && c<='9';c=ge())
	x=(x<<1)+(x<<3)+c-'0';
	if(neg==1)
	return -x;
	return x;
}

