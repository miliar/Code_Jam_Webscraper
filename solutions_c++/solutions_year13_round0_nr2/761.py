#include<iostream>
using namespace std;

int T,R,C;
int in[110][110];
int CR[110];
int CC[110];

int main(){
    int i,j,k;
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for(int cs=1;cs<=T;++cs){
        cin>>R>>C;
        for(i=0;i<R;++i) for(j=0;j<C;++j) cin>>in[i][j];
        bool flag = true;
        for(k=1;k<=100&&flag;++k){
            memset(CR,0,sizeof(CR));
            memset(CC,0,sizeof(CC));
            for(i=0;i<R;++i) for(j=0;j<C;++j){
                if(in[i][j]<=k){
                    CR[i]++;
                    CC[j]++;
                }
            }
            for(i=0;i<R;++i) for(j=0;j<C;++j){
                if(in[i][j]<=k){
                    if(CR[i]==C||CC[j]==R){}
                    else{
                        flag = false;
                    }
                }
            }
        }
        cout<<"Case #"<<cs<<": ";
        if(flag) cout<<"YES\n";
        else cout<<"NO\n";
    }
    return 0;
}

