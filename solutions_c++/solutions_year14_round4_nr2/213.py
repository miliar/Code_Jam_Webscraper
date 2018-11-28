#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <queue>
#include <vector>
#include <ctime>
#include <set>
#include <bitset>
#include <map>
#include <utility>
#include <iterator>
using namespace std;
inline int get()
{
    int f=0,v=0;char ch;
    while(!isdigit(ch=getchar()))if(ch=='-')break;
    if(ch=='-')f=1;else v=ch-48;
    while(isdigit(ch=getchar()))v=v*10+ch-48;
    if(f==1)return -v;else return v;
}
inline double getd()
{
    double d=0,d2=0,d3=1; char ch; bool flag=0;
    while(!isdigit(ch=getchar()))if(ch=='-')break;
    if(ch=='-')flag=true;else d=ch-48;
	while(isdigit(ch=getchar()))d=d*10+ch-48;
    if(ch=='.')
    {
        while(isdigit(ch=getchar()))d2=d2*10+ch-48,d3=d3*0.1;
        d+=d3*d2;
    }
    if(flag)return -d;else return d;
}
const int maxn=10003;
int n,a[maxn];
int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int T=get();
    for(int t=1;t<=T;t++)
    {
		n=get();
		for(int i=1;i<=n;i++)a[i]=get();
		int ans=0;
		while(n>1)
		{
			int t=1;
			for(int i=2;i<=n;i++)
				if(a[t]>a[i])t=i;
			ans+=min(t-1,n-t);
			for(int i=t+1;i<=n;i++)a[i-1]=a[i];
			n--;
		}
		printf("Case #%d: %d\n",t,ans);
	}
    return 0;
}
