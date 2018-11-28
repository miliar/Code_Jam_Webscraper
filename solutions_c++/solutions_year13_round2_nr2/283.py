#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
using namespace std;
double nCr[1010][1010];
double p[3000];
double np[3000];
void mic(int rem,int lim,int need){
    //printf("%d %d %d\n",rem,lim,need);
    for(int i=0;i<3000;i++)p[i]=np[i]=0.0;
    p[0]=1.0;
    for(int i=0;i<rem;i++){
        for(int j=0;j<=lim;j++)np[j]=0.0;
        for(int j=0;j<=min(lim,i);j++){
            int a=j;
            int b=i-j;
            //printf("%d %d %d %d\n",i,j,a,b);
            if(a>=lim){
                np[j]+=p[j];
            }
            else if(b>=lim){
                np[j+1]+=p[j];
            }
            else{
                np[j]+=0.5*p[j];
                np[j+1]+=0.5*p[j];
            }
        }
        for(int j=0;j<=lim;j++){p[j]=np[j];}
        //printf("\n");
    }
    double ans=0;
    for(int i=need;i<=lim;i++)ans+=p[i];
    printf("%.10lf\n",ans);
    return;
}
void solve(){
    int n;
    int x,y;
    scanf("%d %d %d",&n,&x,&y);
    int SZ=1;
    int rem=n;

    for(int Y=0;rem>0;Y+=2){
        //printf("%d %d\n",Y,rem);
        if(rem>=SZ){
            rem-=SZ;
            if(x==0&&Y==y){
                printf("1.0\n");
                return ;
            }
            if( (x!=0) && (y<Y ) &&  ((Y-y)/x ==1 || (Y-y)/x==-1 ) ){
                printf("1.0\n");
                return ;
            }
        }
        else{
            if(x==0&&Y==y){
                printf("0.0\n");
                return ;
            }
            if(x!=0&&y<Y &&  ((Y-y)/x ==1 || (Y-y)/x==-1 )){
                int need=y+1;
                if(need>rem){
                    printf("0.0\n");
                    return;
                }
                else{
                    int lim=SZ/2;
                    mic(rem,lim,need);
                    return;
                }
            }
            rem-=SZ;
        }
        SZ+=4;
    }
    printf("0.0\n");
    return;

}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    for(int i=0;i<=1000;i++){
        nCr[i][0]=nCr[i][i]=1;
        for(int j=1;j<i;j++)nCr[i][j]=nCr[i-1][j]+nCr[i-1][j-1];
    }
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        solve();
    }
}
