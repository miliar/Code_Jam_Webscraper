#include<cstdio>
#include<algorithm>
using namespace std;
int main(){
int test;
freopen("D-large.in","r",stdin);
freopen("outD.txt","w",stdout);
scanf("%d",&test);
for(int n=1;n<=test;n++)
{
    int num;
    scanf("%d",&num);
    double A[1005],B[1005];
    for(int i=0;i<num;i++)
        scanf("%lf",&A[i]);
    for(int i=0;i<num;i++)
        scanf("%lf",&B[i]);
    int la=0,ra=num-1,lb=0,rb=num-1;
    printf("Case #%d: ",n);
    sort(A,A+num);sort(B,B+num);
        while(1){
        for(int i=la,j=lb;i<=ra;i++,j++)
            if(A[i]<B[j])   break;
            else if(i==ra)
            {
                printf("%d ",ra-la+1);
                goto nxt2;
            }
        if(la==ra)
        {
            printf("0 ");
            break;
        }
        la++;
    }
    nxt2:
    la=0,ra=num-1,lb=0,rb=num-1;
    int ans=0;
    while(1)
    {
        if(A[ra]>B[rb])
        {
            lb++;ans++;
        }
        else
            rb--;
        if(ra==0)   break;
        ra--;
    }
    printf("%d\n",ans);
    nxt:;
}
return 0;
}
