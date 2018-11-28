#include<cstdio>
#include<cmath>
#include<cstring>
using namespace std;
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("textC1.out","w",stdout);
    int a,b;
    int sa,sb;
    int T,ca=1;
    int i,j;
    int sum;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&a,&b);
        sa=sqrt(a);
        sb=sqrt(b);
        printf("Case #%d: ",ca++);
        for(i=sa,sum=0;i<=sb;i++){
            j=i*i;
            if(j<a)continue;
            if(i<10&&j<10)sum++;
            else if(j>100){
                if((i%10==i/10)&&(j%10==j/100)){sum++;}
            }
        }
        printf("%d\n",sum);
    }
    return 0;
}
