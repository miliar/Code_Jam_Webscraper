#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
using namespace std;

long long int gcd(long long int c,long long int d)
{
    if(d==0)
        return c;
    return gcd(d,c%d);
}
int i,n,len,x;
char a[50];
long long int p,q,l;
double m;
int main()
{  freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    scanf("%d",&t);
    while(t--)
    { x++;
        p=q=0;
        scanf("%s",a);
        i=0;
        len=strlen(a);
        while(a[i]!='/')
        {
          p=p*10+(a[i]-48);
          i++;
        }
        i++;
        while(i<len)
        {
            q=q*10+(a[i]-48);
            i++;
        }
    l=gcd(p,q);
        while(l!=1)
        {
            p=p/l;
            q=q/l;
            l=gcd(p,q);
        }
        m=log(q);
        m=m/log(2);
        n=m;
        if((q-pow(2,n))!=0)
        {
            printf("Case #%d: impossible\n",x);
        continue;
        }
        if(p==1)
        {
            m=log(q);
            m=m/log(2);
            n=m;
            printf("Case #%d: %d\n",x,n);
        }
        else
        {m=log(p);
        m=m/log(2);
        n=m;
       l=pow(2,n);
        m=q/l;
        m=log(m)/log(2);
        n=m;
        printf("Case #%d: %d\n",x,n);
        }
    }
return 0;
}
