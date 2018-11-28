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
	#ifndef ONLINE_JUDGE
    freopen("example.txt","r",stdin);
	freopen("code.txt","w",stdout);
    #endif
    S(x);
    for(t=1;t<=x;t++)
    {
    	printf("Case #%d: ",t);
    	char a[5][5];int f=0,cto=0,ctx=0,ctt=0;
    	for(i=0;i<4;i++)
    	{
    		for(j=0;j<4;j++)
    		{
    			cin>>a[i][j];
    			
    		}
    	}
    /*	for(i=0;i<4;i++)
    	{
    		for(j=0;j<4;j++)
    		{
    			cout<<a[i][j]<<" ";
    		}
    		cout<<endl;
    	}*/
    	
    	for(i=0;i<4;i++)
    	{
    		ctt=cto=ctx=0;
    		for(j=0;j<4;j++)
    		{
    			if(a[i][j]=='T')
    			ctt++;
    			else if(a[i][j]=='O')
    			cto++;
    			else if(a[i][j]=='X')ctx++;
    		}
    		if(ctx==4 || (ctx==3 && ctt==1))
    		{
    			cout<<"X won"<<endl;
    			goto dd;
    		}
    		if(cto==4 || (cto==3 && ctt==1))
    		{
    			cout<<"O won"<<endl;
    			goto dd;
    		}
    	}
    	for(i=0;i<4;i++)
    	{
    		ctt=cto=ctx=0;
    		for(j=0;j<4;j++)
    		{
    			if(a[j][i]=='T')
    			ctt++;
    			else if(a[j][i]=='O')
    			cto++;
    			else if(a[j][i]=='X')ctx++;
    		}
    		if(ctx==4 || (ctx==3 && ctt==1))
    		{
    			cout<<"X won"<<endl;
    			goto dd;
    		}
    		if(cto==4 || (cto==3 && ctt==1))
    		{
    			cout<<"O won"<<endl;
    			goto dd;
    		}
    	}ctt=cto=ctx=0;
    	for(i=0;i<4;i++)
    	{
   		 
    		for(j=0;j<4;j++)
    		{
    			if(i==j)
    			{
    				if(a[i][j]=='T')
    			ctt++;
    			else if(a[i][j]=='O')
    			cto++;
    			else if(a[i][j]=='X')ctx++;
    			}
    		}
    		if(ctx==4 || (ctx==3 && ctt==1))
    		{
    			cout<<"X won"<<endl;
    			goto dd;
    		}
    		if(cto==4 || (cto==3 && ctt==1))
    		{
    			cout<<"O won"<<endl;
    			goto dd;
    		}
    	}
    	ctt=cto=ctx=0;
    		for(i=0;i<4;i++)
    	{
    		
    		for(j=0;j<4;j++)
    		{
    			if(i+j==3)
    			{
    				if(a[i][j]=='T')
    			ctt++;
    			else if(a[i][j]=='O')
    			cto++;
    			else if(a[i][j]=='X')ctx++;
    			}
    		}
   		
    		if(ctx==4 || (ctx==3 && ctt==1))
    		{
    			cout<<"X won"<<endl;
    			goto dd;
    		}
    		if(cto==4 || (cto==3 && ctt==1))
    		{
    			cout<<"O won"<<endl;
    			goto dd;
    		}
    	}
    	for(i=0;i<4;i++)
    	{
    		ctt=cto=ctx=0;
    		for(j=0;j<4;j++)
    		{
    			if(a[i][j]=='.')
    			{cout<<"Game has not completed"<<endl;
    			goto dd;
    			}
    		}
    	}
    		cout<<"Draw"<<endl;
			dd:;		
    	
    }
    return 0;
}
