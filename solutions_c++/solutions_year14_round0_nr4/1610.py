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
double a[10001],b[10001];
bool b11[10001],b12[10001];
int main()
{
    freopen("D-largeinput.txt","r",stdin);
    freopen("output-Dlarge.txt","w",stdout);
	int T=1,t,i,j,n,ans1,ans2;
	t=in();
	while(t--)
	{
	    for(i=0;i<10000;i++)
            a[i]=b[i]=0.0,b11[i]=b12[i]=0;
	    ans1=ans2=0;
		n=in();
		for(i=0;i<n;i++)
            cin>>a[i];
		for(i=0;i<n;i++)
            cin>>b[i];
        sort(a,a+n);
        sort(b,b+n);
      
        for(i=0;i<n;i++)
        {
            int f=0;
            for(j=0;j<n;j++)
            {
                if(b[j]>a[i] && !b11[j])
                {
                //    cout<<"lost at i="<<i<<" j="<<j<<endl;
       //             ans1++;
                    b11[j]=1;
                    f=1;
                    break;
                }
            }
            if(f==0)
            {
                for(j=0;j<n;j++)
                {
                    if(b[j]<a[i] && !b11[j])
                    {
                //        cout<<"won at i="<<i<<" j="<<j<<endl;
                        b11[j]=1;
                        ans1++;
                        break;
                    }
                }
            }
        }
        memset(b11,0,sizeof(b11));
        int min_wo=0,max_wo=n-1,min_i=0,max_i=n-1;
        while(1)
        {
            if(min_wo>max_wo)
                break;
        //    cout<<"in";
            if(a[min_i]<b[min_wo])
            {
                b11[min_i]=1;
                b12[max_wo]=1;
         //       cout<<"lost at i="<<min_i<<" j="<<max_wo<<endl;
                min_i+=1;
                max_wo-=1;
            }
            else
            {
                b11[min_i]=1;
                b12[min_wo]=1;
                ans2++;
         //       cout<<"won at i="<<min_i<<" j="<<min_wo<<endl;
                min_i+=1;
                min_wo+=1;
            }
        }
		printf("Case #%d: ",T++);
		pii(ans2,ans1);
	}
	return 0;
}
