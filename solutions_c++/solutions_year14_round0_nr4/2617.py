#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    int i,t,n,res1,res2,j,k;
    bool ma[2000],mb[2000],flag;
    double a[2000],b[2000];
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d",&n);
        res1=res2=0;
        for(j=1;j<=n;j++){
            scanf("%Lf",&a[j]);
            ma[j]=false;
        }
        for(j=1;j<=n;j++){
            scanf("%Lf",&b[j]);
            mb[j]=false;
        }
        sort(&a[1],&a[n+1]);
        sort(&b[1],&b[n+1]);
        for(j=1;j<=n;j++)
        {
            flag=true;
            for(k=1;k<=n;k++)
            {
                if(!mb[k]&&b[k]>a[j])
                {
                    mb[k]=true;
                    flag=false;
                    break;
                }
            }
            if(flag){
                res1++;
                for(k=n;k>=1;k--)
                {
                    if(!mb[k])
                    {
                        mb[k]=true;
                        break;
                    }
                }
            }
        }
        for(j=n;j>=1;j--)
        {
            flag=true;
            for(k=n;k>=1;k--)
            {
                if(!ma[k]&&a[k]>b[j])
                {
                    res2++;
                    ma[k]=true;
                    flag=false;
                    break;
                }
            }
            if(flag)
            {
                for(k=1;k<=n;k++)
                {
                    if(!ma[k])
                    {
                        ma[k]=true;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %d %d\n",i,res2,res1);
        getchar();
    }
    return 0;
}
