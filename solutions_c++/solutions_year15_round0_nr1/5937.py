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

//  CREATED BY: ATUL SEHGAL
char s[10003];
int main()
{
    freopen("input-Alarge.txt","r",stdin);
    freopen("output-Alarge.txt","w",stdout);
 	int t,i,j,n,ans,T=1,sum;
	si(t);
	while(t--)
	{
	    ans=sum=0;
		si(n);
		scanf("%s",s);
		for(i=0;i<=n;i++)
        {
            if(i>sum)
            {
                ans+=(i-sum);
                sum=i;
            }
            sum+=(s[i]-'0');
        }
		printf("Case #%d: ",T++);
		pi(ans);
	}
	return 0;
}
