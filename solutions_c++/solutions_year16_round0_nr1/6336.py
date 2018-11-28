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

int getNumber(int num)
{
    int digit[10]= {0}, count = 10, i=1 ;
    while(count)
    {
        int x=num*i;
        while(x)
        {
            if(!digit[x%10])
            {
                count--;
                digit[x%10] = 1;
            }
            x/=10;
            //pi(x);
        }
        //pi(num*i);
        if(!count)
            return num*i;
        i++;
        if(i>500000)
            return 0;
    }
    return 0;
}
int main()
{
    freopen("input-A-large.txt","r",stdin);
    freopen("output-Alarge.txt","w",stdout);
 	int t,n,ans,T=1;
	si(t);
	while(t--)
	{
		si(n);
		printf("Case #%d: ",T++);
		ans = getNumber(n);
		if(ans)
            pi(ans);
        else
            printf("INSOMNIA\n");
	}
	return 0;
}
