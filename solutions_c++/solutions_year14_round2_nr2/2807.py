#include<cstdio>
using namespace std;
int a,b,k,cnt,l;
int main()
{
int t,i,j,x=0;
freopen("out.txt","w",stdout);
freopen("inp.in","r",stdin);
    scanf("%d",&t);
    while(t--)
    { cnt=0;
    x++;
        scanf("%d %d %d",&a,&b,&k);
        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                l=i&j;
                if(l<k)
                    cnt++;
            }
        }
        printf("Case #%d: %d\n",x,cnt);
    }
return 0;
}
