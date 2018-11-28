#include<cstdio>
#include<string>
#include<vector>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<cstdlib>
#include<cctype>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<fstream>
#include<numeric>
#include<map>
#include<sstream>
#include<iterator>
#define M 100
using namespace std;
typedef long  ll;
ll power(ll i)
{
    int j,l=1;
    for(j=0;j<i;j++)
        l*=10;
    return l;
}
bool conv(ll n)
{
    ll i,j,k,l=0,pow;
    k =n;
    pow = floor(log10(k))+1;
    while(pow)
    {
        l+=(k%10)*power(pow-1);
        pow--;
        k/=10;
    }
    if(l==n) return true;
    return false;
}
int main()
{
	freopen("D:\\in.txt","r",stdin);
	freopen("D:\\out.txt","w",stdout);
	ll i,sb,j,k,a,b,l,c=1;
	cin >> k;
	while(k--)
    {
       l=0;
        cin >> a >> b;
        for(i=a;i<=b;i++)
        {
			j= sqrt(i);
			if(j*j==i)
            if(conv(i)&conv(j))
               l++;

        }
        printf("Case #%ld: %ld\n",c++,l);
    }
	return 0;
}
