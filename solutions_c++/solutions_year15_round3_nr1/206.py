#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <list>
#include <queue>
#include <vector>
#include <ctime>
#include <set>
#include <bitset>
#include <deque>
#include <fstream>
#include <stack>
#include <map>
#include <utility>
#include <cassert>
#include <string>
#include <iterator>
#include <cctype>
using namespace std;
typedef long long LL;
double getd()
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
int get()
{
    int f=0,v=0;char ch;
    while(!isdigit(ch=getchar()))if(ch=='-')break;
    if(ch=='-')f=1;else v=ch-48;
    while(isdigit(ch=getchar()))v=v*10+ch-48;
    if(f==1)return -v;else return v;
}
int n,a[100000];
int main()
{
	freopen("Al.in","r",stdin);
	freopen("Al.out","w",stdout);
	int T=get();
	for(int _=1;_<=T;_++)
	{
		int r=get(),c=get(),w=get(),ans=0;
		if(r==1)
		{
			while(c-w>=w)ans++,c-=w;
			ans+=w;
			if(c>w)ans++;
		}else
		{
			ans+=(c/w)*(r-1);
			while(c-w>=w)ans++,c-=w;
			ans+=w;
			if(c>w)ans++;
		}
		printf("Case #%d: %d\n",_,ans);
	}
	return 0;
}
