#include <iostream>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <queue>
#include <cstring>
#include<string>
#include <cmath>
#include <vector>
#include <stack>
#include <set>
#include <map>
#include <deque>
#define SET(p) memset(p,-1,sizeof(p))
#define CLR(p) memset(p,0,sizeof(p))
#define LL long long int
#define ULL unsigned long long int
#define S(n)                    scanf("%d",&n)
#define Sl(n)                     scanf("%lld",&n)
#define Sf(n)                     scanf("%lf",&n)
#define Ss(n)                     scanf("%s",n)
using namespace std;
/* template <class T>
inline void r_f(T &p)
{
         char c;
         while (((c=getchar_unlocked()) < 48)|(c > 57));
         p=c-48;
         while ((c=getchar_unlocked()) >= 48 && c <= 57) p=p*10+c-48;
} */
int ispal(int x)
{
	int n=x,m=0,ct=1,p=0;
	while(n)
	{
		int temp2=n%10;
		m=m*10+temp2;
		n/=10;
	}
	if(m==x)
	return 1;
	else return 0;
}
		
int main()
{
	int t,i,j,k,n,x,w,h,p,a,b;
	#ifndef ONLINE_JUDGE
    freopen("example.txt","r",stdin);
	freopen("code.txt","w",stdout);
    #endif
    S(x);
    for(t=1;t<=x;t++)
    {
    	printf("Case #%d: ",t);
    	S(a);S(b);
    	int ct=0;
		for(i=a;i<=b;i++)
		{
			if(ispal(i))
			{
				for(j=1;j<=35;j++)
				if(j*j==i)
				if(ispal(j))
				ct++;
			}
		}
		cout<<ct<<endl;
		
    }
    return 0;
}
