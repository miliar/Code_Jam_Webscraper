#include<bits/stdc++.h>
using namespace std;

char x[4][4]={{'1','i','j','k'},{'i','1','k','j'},{'j','k','1','i'},{'k','j','i','1'}};
int sig[4][4]={{1,1,1,1},{1,-1,1,-1},{1,-1,-1,1},{1,1,-1,-1}};

int main(){
    int T;
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small_outfin.txt","w",stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;++t){
        int L,X;
        string s;
        scanf("%d %d",&L,&X);
        cin>>s;
        string s1=s;
        for(int i=0;i<X;++i)
            s=s+s1;
        char lol[10002];
        int lols[10002];
        for(int i=L*X-1;i>=0;--i){
            if(i==L*X-1){
                lols[L*X-1]=1;
                lol[L*X-1]=s[L*X-1];
            }
            else{
                int u,v;
                if(s[i]=='1')
                    u=0;
                else
                    u=s[i]-'i'+1;
                if(lol[i+1]=='1')
                    v=0;
                else
                    v=lol[i+1]-'i'+1;
                lol[i]=x[u][v];
                lols[i]=lols[i+1]*sig[u][v];
            }
        }
        int fl=0;
        char fc,sc,tc;
        int fs=1,ss=1,ts=1;
        for(int i=0;i<L*X && !fl;++i){
            if(i==0){
                fc=s[i];
            }
            else{
                int u,v;
                if(fc=='1')
                    u=0;
                else
                    u=fc-'i'+1;
                if(s[i]=='1')
                    v=0;
                else
                    v=s[i]-'i'+1;
                fc=x[u][v];
                fs=fs*sig[u][v];
            }
            if(fc=='i' && fs==1){
                for(int j=i+1;j<L*X;++j){
                    if(j==i+1){
                        sc=s[j];
                        ss=1;
                    }
                    else{
                        int u,v;
                        if(sc=='1')
                            u=0;
                        else
                            u=sc-'i'+1;
                        if(s[j]=='1')
                            v=0;
                        else
                            v=s[j]-'i'+1;
                        sc=x[u][v];
                        ss=ss*sig[u][v];
                    }
                    if(ss==1 && sc=='j' && j+1<L*X && lol[j+1]=='k' && lols[j+1]==1){
                        fl=1;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %s\n",t,fl?"YES":"NO");
    }
}
