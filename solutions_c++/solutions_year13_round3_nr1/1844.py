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
int main()
{
	int t,i,j,k,n,x;
	char s[101];
	string str;
	#ifndef ONLINE_JUDGE
    freopen("example.txt","r",stdin);
	freopen("code.txt","w",stdout);
    #endif
    S(x);
    int p=0;
    for(t=1;t<=x;t++)
    {
    	printf("Case #%d: ",t);
    	cin>>s;
    	cin>>k;
    	int len,ct=0,ct2=0;
    	len=strlen(s);
    	for(i=0;i<strlen(s);i++)
    	{
    		int q=0,ct2=0;
    		
    		for(j=i;j<strlen(s);j++)
    		{
    			ct2++;
    			if(s[j]=='a'||s[j]=='i'||s[j]=='o'||s[j]=='u'||s[j]=='e')
    			{
    				q++;
    				ct2=0;
    			}
    			
    			if(ct2==k)
    			{ct+=strlen(s)-j; break;}
    		}
			
			}
			cout<<ct<<endl;
    }
    return 0;
}
