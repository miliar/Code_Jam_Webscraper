#include<bits/stdc++.h>
#define ll unsigned long long

using namespace std;
int ans2[50],n,ans[12];
ll a[12];
void solve(int limit)
{
    int ck=0;
    for(ll mask=1;mask<(1<<(n-1));mask++){
        int cnt=0,pt=0;
        memset(a,0,sizeof(a));
        memset(ans,0,sizeof(ans));
        if(mask&1){
        for(int j=0;j<(n-1);j++){
            if(mask&(1<<j)){
                ans2[pt++]=1;
                for(int i=2;i<=10;i++){
                    double b,ex,num;
                    b=i; ex=j;
                    num=(pow(b,ex));
                    a[i]=a[i]+num;
//                    cout<<a[i]<<" ";
                } //cout<<'\n';
            }
            else
                ans2[pt++]=0;
        }
        for(int i=2;i<=10;i++){
            double b,ex,num;
            b=i; ex=n-1;
            num=(pow(b,ex));
            a[i]=a[i]+num;
//            cout<<a[i]<<" ";
            for(int k=2;k<=(sqrt(a[i]));k++){
                if(a[i]%k==0){
                    ans[i]=k;
                    cnt++;
                    break;
                }
            }
        } //cout<<'\n';
        if(cnt==9){
            ans2[pt]=1;
            for(int j=n-1;j>=0;j--)
                printf("%d",ans2[j]);
            printf(" ");
            for(int j=2;j<=10;j++)
                printf("%d ",ans[j]);
            printf("\n");
            ck++;
        }
        }
        if(ck==limit)
            break;
    }
}
int main()
{
    int T,t,i,k;
    freopen("C-small.in","r",stdin);
    freopen("A-output.txt","w",stdout);
    scanf("%d",&T);
    for(t=1;t<=T;t++){
        int j;
        scanf("%d%d",&n,&j);
        printf("Case #%d:\n",t);
        solve(j);
    }
    return 0;
}
