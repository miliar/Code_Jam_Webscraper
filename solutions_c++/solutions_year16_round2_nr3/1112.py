#include<bits/stdc++.h>
using namespace std;
map <string,int> m;
int ar[18][2];
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("y.txt","w",stdout);
    int T,N;
    scanf("%d",&T);
    for(int t=1;t<=T;++t){
        m.clear();
        int ct=0,ans=0;
        scanf("%d",&N);
        for(int i=0;i<N;++i){
            string a,b;
            cin>>a>>b;
            if(m.find(a)==m.end()){
                m[a]=++ct;
                ar[i][0]=ct;
            }
            else
                ar[i][0]=m[a];
            if(m.find(b)==m.end()){
                m[b]=++ct;
                ar[i][1]=ct;
            }
            else
                ar[i][1]=m[b];
        }
        for(int q=0;q<(1<<N);++q){
            //printf("%d\n",i);
            int b[52];
            memset(b,0,sizeof(b));
            int x=0,tmp=q;
            while(tmp){
                b[x++]=tmp%2;
                tmp/=2;
            }
            int abc=0,bty=0;
            for(int i=0;i<N;++i){
                if(b[i]==1){
                    ++bty;
                    int fl=0;
                    for(int j=0;j<N;++j){
                        if(b[j]==0 && ar[j][0]==ar[i][0])
                            fl=1;
                    }
                    if(fl==1){
                        for(int j=0;j<N;++j){
                            if(b[j]==0 && ar[j][1]==ar[i][1])
                                fl=2;
                        }
                    }
                    if(fl==2){
                        ++abc;
                    }
                }
            }
            if(bty==abc){
                ans=max(ans,bty);
            }
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
