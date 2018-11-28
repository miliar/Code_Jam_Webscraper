#include<stdio.h>
#define rep(i,n) for(i=0;i<n;i++)
#define each(i,x,n) for(i=x;i<n;i++)
#define repb(i,n) for(i=n;i>0;i--)
#define eachb(i,x,n) for(i=n;i>x;i--)
#define su(b) scanf("%llu",&b);
#define sd(b) scanf("%lld",&b);
#define ss(b) scanf("%s",&b);
#define sc(b) scanf("%c",&b);
#define sf(b) scanf("%lf",&b);
typedef long long ll;
typedef unsigned long long ull;
ll t,res[1000000];
void output()
{ll i;
 rep(i,t)
{
 printf("Case #%lld: %lld\n",i+1,res[i]);
}
}
int main()
{ll r,c,w;
 ll i,j;
 sd(t);
 rep(i,t)
{sd(r);
sd(c);
sd(w);
 if(c == w)
 res[i]=r+w-1;
else if(w>(c/2))
 res[i]=r+w;
else if(w==1)
 res[i]=r*c;
else 
 res[i]=(((c-1)/w)+w)+(r-1)*(c/w);
 

}
output();
}
