#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
typedef long long ll;
int T,t,n,m;
ll ans[55][11],ans_num;
int s[20];
ll Prime(ll num){
    ll i,j,k,R=sqrt(num)+1;
    for(i=2;i<=R;i++)
        if(num%i==0)
            return i;
    return 0;
}
void solve(int num){
    //printf("solve %d\n",num);
    int i,j,k=0;
    ll ret=num,f,temp;
    while(ret){
        s[++k]=ret&1;
        ret/=2;
    }
    for(k=2;k<=10;k++){
        ret=0;
        for(i=16;i>=1;i--){
            ret=ret*k+s[i];
        }
        if(k==10)
            temp=ret;
        f=Prime(ret);
        //printf("%I64d %I64d\n",ret,f);
        if(f>0)
            ans[ans_num+1][k]=f;
        else
            return;
    }
    ans_num++;
    ans[ans_num][1]=temp;
    //printf("%I64d %I64d\n",ans_num,temp);
}
int main(){
    freopen("out.txt","w",stdout);
    int i,j,k=0,r,ret=0;
    n=(1<<15)+1;
    r=1<<16;
    while(ans_num<50){
        solve(n);
        n+=2;
        k++;
    }
    printf("Case #1:\n");
    for(i=1;i<=50;i++){
        printf("%I64d",ans[i][1]);
        for(j=2;j<=10;j++)
            printf(" %I64d",ans[i][j]);
        printf("\n");
    }
}
