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

int main()
{
    freopen("BB-large.in","r",stdin);
    freopen("output-Blarge.txt","w",stdout);
	int T=1,t,j,n;
	double i,c,f,x,sum,ans;
	si(t);
	while(t--)
	{
	    i=2.0;
		slflf(c,f);slf(x);
		ans=0.0;
		while(1)
        {
            if(c/i + x/(i+f)>=x/i)
            {
                ans+=x/i;
                break;
            }
        //    cout<<"+ "<<c/i<<endl;
            ans+=c/i;
            i+=f;
        }
		printf("Case #%d: %0.7lf\n",T++,ans);
		//system("pause");
	}
	return 0;
}
