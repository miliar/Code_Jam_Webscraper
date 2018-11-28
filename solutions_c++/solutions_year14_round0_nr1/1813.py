#include<iostream>
#include<stdio.h>
#include<cmath>
#include<cstring>
#include<stdlib.h>
#include<algorithm>
#include<limits.h>
using namespace std;

/*printing definitions*/
#define pi(x) printf("%d\n",(x))
#define pii(x,y) printf("%d %d\n",(x),(y))
#define pl(x) printf("%lld\n",(x))
#define pll(x,y) printf("%lld %lld\n",(x),(y))
#define pil(x,y) printf("%d %lld\n",(x),(y))
#define pli(x,y) printf("%lld %d\n",(x),(y))
#define plf(x) printf("%lf\n",(x))
#define plflf(x,y) printf("%lf %lf\n",(x),(y))

/*scanning definitions*/
#define si(x) scanf("%d",&x)
#define sii(x,y) scanf("%d %d",&x,&y)
#define sl(x) scanf("%lld",&x)
#define sll(x,y) scanf("%lld %lld",&x,&y)
#define sil(x,y) scanf("%d %lld",&x,&y)
#define sli(x,y) scanf("%lld %d",&x,&y)
#define slf(x) scanf("%lf",&x)
#define slflf(x,y) scanf("%lf %lf",&x,&y)

/*fast i/p definitions*/
#define getcx getchar_unlocked
#ifndef ONLINE_JUDGE
    #define getcx getchar
#endif       
//  CREATED BY: ATUL SEHGAL
inline int in()
{
   int n=0;
   int ch=getcx();int sign=1;
   while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();}

   while(  ch >= '0' && ch <= '9' )
           n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
   return n*sign;
}
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output-A.txt","w",stdout);
	int T=1,t,i,j,n,a[5][5],k;
	t=in();
	while(t--)
	{
	    k=0;
	    n=in();
	    for(i=1;i<5;i++)
            for(j=1;j<5;j++)
                a[i][j]=in();
		bool ans[17]={0};
		for(j=1;j<5;j++)
            ans[a[n][j]]=1;
        n=in();
	    for(i=1;i<5;i++)
            for(j=1;j<5;j++)
                a[i][j]=in();
		for(j=1;j<5;j++)
            if(ans[a[n][j]])
                i=a[n][j],k++;
        
		printf("Case #%d: ",T++);
        if(i && k==1)
            pi(i);
        else if(k>1)
            printf("Bad magician!\n");
        else
            printf("Volunteer cheated!\n");
	}
	return 0;
}
