#include<bits/stdc++.h>
using namespace std;

char dp[16][1<<16];
char op[]={'P','R','S'};

string tmp;
void build(int ll,int rr){
    if(ll==rr)return ;
    int mid=(ll+rr)>>1;
    build(ll,mid);
    build(mid+1,rr);

    bool judge=true;
    for(int i=ll,j=0;i<=mid;i++,j++){
        if(tmp[i]>tmp[mid+1+j]){
            judge=false;
            break;
        }
        if(tmp[i]<tmp[mid+1+j]){
            judge=true;
            break;
        }
    }
    if(!judge){
        string now;
        for(int i=mid+1;i<=rr;i++){
            now.push_back(tmp[i]);
        }
        for(int i=ll;i<=mid;i++){
            now.push_back(tmp[i]);
        }
        for(int i=ll,j=0;i<=rr;i++,j++){
            tmp[i]=now[j];
        }
    }
    //cout<<tmp<<endl;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int test;
    scanf("%d",&test);
    for(int _=1;_<=test;_++){
        int n,R,P,S;
        scanf("%d%d%d%d",&n,&R,&P,&S);

        string ret="Z";
        bool judge=false;
        for(int mm=0;mm<3;mm++){
            dp[0][0]=op[mm];
            for(int i=0; i<n; i++)
            {
                for(int j=0; j<(1<<i); j++)
                {
                    if('P'==dp[i][j])
                    {
                        dp[i+1][j<<1]='P';
                        dp[i+1][j<<1|1]='R';
                    }
                    else if('R'==dp[i][j])
                    {
                        dp[i+1][j<<1]='R';
                        dp[i+1][j<<1|1]='S';
                    }
                    else
                    {
                        dp[i+1][j<<1]='P';
                        dp[i+1][j<<1|1]='S';
                    }
                }
            }
            int a=0,b=0,c=0;
            for(int i=0; i<(1<<n); i++)
            {
                if(dp[n][i]=='P')a++;
                else if(dp[n][i]=='R')b++;
                else c++;
            }


            if(a==P&&b==R&&c==S){
                judge=true;
                dp[n][1<<n]=0;
                tmp=dp[n];
                build(0,(1<<n)-1);
                ret=min(ret,tmp);
            }
        }
        printf("Case #%d: ",_);
        if(judge)cout<<ret<<endl;
        else puts("IMPOSSIBLE");
    }
    return 0;
}
