#include<bits/stdc++.h>
using namespace std;

int c[1003]={0};
int j[1003]={0};
int ct,jt;
int func(string s){
    for(int i=0;i<s.size();++i){
        if(s[i]=='?'){
            for(int j=0;j<=9;++j){
                s[i]=j+'0';
                func(s);
            }
            return 0;
        }
    }
    int x=0;
    for(int i=0;i<s.size();++i)
        x=x*10+s[i]-'0';
    c[ct++]=x;
    return 0;
}

int func2(string s){
    for(int i=0;i<s.size();++i){
        if(s[i]=='?'){
            for(int j=0;j<=9;++j){
                s[i]=j+'0';
                func2(s);
            }
            return 0;
        }
    }
    int x=0;
    for(int i=0;i<s.size();++i)
        x=x*10+s[i]-'0';
    j[jt++]=x;
    return 0;
}

int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("y.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;++t){
        ct=0,jt=0;
        string a,b;
        cin>>a>>b;
        int L=a.size();
        func(a);
        func2(b);
        int ca=0,ja=1000;
        for(int i=0;i<ct;++i){
            for(int k=0;k<jt;++k){
                if(abs(ja-ca)>abs(c[i]-j[k])){
                    ca=c[i];
                    ja=j[k];
                }
                else if(abs(ja-ca)>abs(c[i]-j[k])){
                    if(ca>c[i]){
                        ca=c[i];
                        ja=j[k];
                    }
                    else if(ca==c[i]){
                        if(ja>j[k]){
                            ca=c[i];
                            ja=j[k];
                        }
                    }
                }
            }
        }
        int ans[3];
        printf("Case #%d: ",t);
        int kag=0;
        while(ca){
            ans[kag++]=ca%10;
            ca/=10;
        }
        while(kag<L)
            ans[kag++]=0;
        for(int i=L-1;i>=0;--i)
            printf("%d",ans[i]);
        printf(" ");
        kag=0;
        while(ja){
            ans[kag++]=ja%10;
            ja/=10;
        }
        while(kag<L)
            ans[kag++]=0;
        for(int i=L-1;i>=0;--i)
            printf("%d",ans[i]);
        printf("\n");
    }
    return 0;
}
