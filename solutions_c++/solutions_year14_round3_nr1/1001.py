#include<cstdio>
#include<fstream>
using namespace std;
long long c;
long long gcd(long long a,long long b)
{
    while(a%b>0)
    {
        c=a%b;
        a=b;
        b=c;
    }
    return b;
}
int main()
{
    FILE * sf=fopen("A-large.in","r");
    FILE * pf=fopen("ans.txt","w");
    int t,i,x;
    long long p,q,ans,h;
    double f,a,c,d;
    fscanf(sf,"%d",&t);
    for(x=1;x<=t;++x)
    {
        fscanf(sf,"%lld/%lld",&p,&q);
        h=gcd(p,q);
        p=p/h;
        q=q/h;
        c=p;
        d=q;
        while(q%2==0)q/=2;
        if(q==1)
        {
            f=c/d;
            a=0.5;
            ans=1;
            while(f<a)
            {
                ans++;
                a/=2;
            }
            fprintf(pf,"Case #%d: %lld\n",x,ans);
            //printf("Case #%d: %lld\n",x,ans);

        }
        else
        {
            fprintf(pf,"Case #%d: impossible\n",x);
            //printf("Case #%d: impossible\n",x);
        }
    }
    fclose(pf);

}
