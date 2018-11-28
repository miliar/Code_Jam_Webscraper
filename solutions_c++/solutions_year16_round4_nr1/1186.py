#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
vector<string> v[12];
/* P=0 R=1 S=2 PR=3 RS=4 PS=5*/
int rw[20][6],pw[20][6],sw[20][6];
char ans[20][10005];
int pow2[20];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    rw[1][1]=1;
    pw[1][0]=1;
    sw[1][2]=1;
    for(int i=1;i<=12;i++){
        rw[i+1][0]=rw[i][0]+rw[i][2];
        rw[i+1][1]=rw[i][0]+rw[i][1];
        rw[i+1][2]=rw[i][1]+rw[i][2];
        pw[i+1][0]=pw[i][0]+pw[i][2];
        pw[i+1][1]=pw[i][0]+pw[i][1];
        pw[i+1][2]=pw[i][1]+pw[i][2];
        sw[i+1][0]=sw[i][0]+sw[i][2];
        sw[i+1][1]=sw[i][0]+sw[i][1];
        sw[i+1][2]=sw[i][1]+sw[i][2];
    }
    pow2[0]=1;
    for(int i=1;i<16;i++){
        pow2[i]=pow2[i-1]*2;
    }
    int tc;
    scanf("%d",&tc);
    for(int t=1;t<=tc;t++){
        memset(ans,0,sizeof(ans));
        int n,r,p,s;
        scanf("%d %d %d %d",&n,&r,&p,&s);
        n++;
        for(int i=0;i<=n;i++){
            v[i].clear();
        }
        printf("Case #%d: ",t);
        if(n==1){
            if(r!=0){
                printf("R\n");
            }
            else if(p!=0){
                printf("P\n");
            }
            else{
                printf("S\n");
            }
        }
        else{
            if(r==rw[n][1]&&p==rw[n][0]&&s==rw[n][2]){
//                printf("RWIN");
                ans[1][0]='R';
                for(int i=2;i<=n;i++){
                    int idx=0;
                    for(int j=0;j<pow2[i-1];j++){
                        if(ans[i-1][j]=='R'){
                            ans[i][idx]='R';
                            ans[i][idx+1]='S';
                            idx+=2;
                        }
                        else if(ans[i-1][j]=='P'){
                            ans[i][idx]='P';
                            ans[i][idx+1]='R';
                            idx+=2;
                        }
                        else{
                            ans[i][idx]='P';
                            ans[i][idx+1]='S';
                            idx+=2;
                        }
                    }
                }
            }
            else if(r==pw[n][1]&&p==pw[n][0]&&s==pw[n][2]){
//                printf("PWIN");
                ans[1][0]='P';
                for(int i=2;i<=n;i++){
                    int idx=0;
                    for(int j=0;j<pow2[i-1];j++){
                        if(ans[i-1][j]=='R'){
                            ans[i][idx]='R';
                            ans[i][idx+1]='S';
                            idx+=2;
                        }
                        else if(ans[i-1][j]=='P'){
                            ans[i][idx]='P';
                            ans[i][idx+1]='R';
                            idx+=2;
                        }
                        else{
                            ans[i][idx]='P';
                            ans[i][idx+1]='S';
                            idx+=2;
                        }
                    }
                }
            }
            else if(r==sw[n][1]&&p==sw[n][0]&&s==sw[n][2]){
//                printf("SWIN");
                ans[1][0]='S';
                for(int i=2;i<=n;i++){
                    int idx=0;
                    for(int j=0;j<pow2[i-1];j++){
                        if(ans[i-1][j]=='R'){
                            ans[i][idx]='R';
                            ans[i][idx+1]='S';
                            idx+=2;
                        }
                        else if(ans[i-1][j]=='P'){
                            ans[i][idx]='P';
                            ans[i][idx+1]='R';
                            idx+=2;
                        }
                        else{
                            ans[i][idx]='P';
                            ans[i][idx+1]='S';
                            idx+=2;
                        }
                    }
                }
            }
            else{
                printf("IMPOSSIBLE\n");
                continue;
            }
            char pp[3];
            for(int i=0;i<pow2[n];i+=2){
                pp[0]=ans[n][i];
                pp[1]=ans[n][i+1];
                string qq (pp);
                v[n-1].push_back(qq);
            }
            for(int i=n-1;i>=2;i--){
                for(int j=0;j<v[i].size();j+=2){
                    if(v[i][j+1]<v[i][j]){
                        swap(v[i][j+1],v[i][j]);
                    }
                    v[i-1].push_back(v[i][j]+v[i][j+1]);
                }
            }
            cout << v[1][0] <<'\n';
        }
    }
}
