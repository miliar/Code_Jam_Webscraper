#include<stdio.h>
#include<math.h>
using namespace std;
bool check(int n)
{
    int c=0;
    for(int i=n;i>0;i/=10)
    {
        c=c*10+i%10;
    }
    if(c==n)return 1;
    return 0;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    long int T,i,j,k,l=1,a,b,t;
    scanf("%ld",&T);
    for(i=1;i<=T;i++)
    {
        scanf("%ld %ld",&a,&b);
        for(j=a,k=0;j<=b;j++)
        {
            if(check(j)==1)
            {
                t=sqrt(j);
                if(t*t==j)
                {
                    if(check(t)==1)k++;
                }
            }
        }
        printf("Case #%ld: %ld\n",l++,k);
    }
    return 0;
}
