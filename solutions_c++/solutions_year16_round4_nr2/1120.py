#include<bits/stdc++.h>
using namespace std;
double x[1000];
bool y[1000];
double ans;
vector<double>prob;
double dp[2][1000];
int main(){
    int T,n,k;
    FILE *in = fopen("input.txt","r");
    FILE *out = fopen("output.txt","w");
    fscanf(in,"%d",&T);
    for(int t=1;t<=T;t++){
        fscanf(in,"%d%d",&n,&k);
        ans = 0;
        for(int i=0;i<n;i++) fscanf(in,"%lf",&x[i]);
        for(int s=1;s<(1<<n);s++){
            int num=0;
            for(int i=0;i<n;i++)  if(s&(1<<i)) num++;
            if(num == k){
                prob.clear();
                for(int i=0;i<n;i++)  {
                    if(s&(1<<i)) {
                      prob.push_back(x[i]);
                    }
                }
                for(int i=0;i<=k;i++) dp[0][i]=dp[1][i]=0;
                int cur=0;
                dp[0][1] = prob[0];
                dp[0][0] = 1-prob[0];
                int mx=1;
                for(int i=1;i<k;i++){
                    for(int j=mx+1;j>=1;j--) {
                        dp[1-cur][j] = dp[cur][j-1]*prob[i]+dp[cur][j]*(1-prob[i]);
                    }
                    mx+=1;
                    dp[1-cur][0] = dp[cur][0]*(1-prob[i]);
                    cur=1-cur;
                }
                double nowans = dp[cur][k/2];
                if(ans<nowans) ans=nowans;
            }
        }
        fprintf(out,"Case #%d: %.7lf\n",t,ans);
    }
}
