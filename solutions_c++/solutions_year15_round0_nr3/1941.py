#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <bitset>
#include <stack>
#include <string>
#include <map>

using namespace std;
const int N = 1e4+9;
const int OPP[5][5]={{0,0,0,0,0}
            ,{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2}
            ,{0,4,3,-2,-1}};
struct P{
    int x;
    P(int c=1){x=c;}
    P operator *(P a)const{
        int flag=x*a.x;
        if(flag>0)flag=1;
        else flag=-1;
        int ans = OPP[abs(x)][abs(a.x)];
        ans*=flag;
        return P(ans);
    }
    bool operator <(P y)const{
        return x<y.x;
    }
    bool operator ==(P y)const{
        return x==y.x;
    }
    bool operator !=(P y)const{
        return x!=y.x;
    }
};
P POW(P a,int pp){
    P ans;
    while(pp){
        if(pp&1)ans=ans*a;
        a=a*a;
        pp>>=1;
    }
    return ans;
}
P A[N],I[N],Aft[N];
int L,X;
char S[N];
set<P> Suf[N];
string solve(){
    scanf("%d%d%s",&L,&X,S);
    A[0]=P(1); I[0]=P(1);
    for(int i=1;i<=L;i++){
        P cur;
        if(S[i-1]=='i'){
            cur=P(2);
        }else if(S[i-1]=='j'){
            cur=P(3);
        }else{
            cur=P(4);
        }
        I[i]=cur;
        A[i]=A[i-1]*cur;
    }
    Suf[L+1].clear();
    Suf[L+1].insert(P(1));
    Aft[L+1]=P(1);
    for(int i=L;i>=0;i--){
        Aft[i]=I[i]*Aft[i+1];
        Suf[i]=Suf[i+1];
        Suf[i].insert(Aft[i]);
    }
    bool ok=false;
    P Last=POW(A[L],X);
    if(P(2)*P(3)*P(4)!=Last)return "NO";
    P PW[4];
    for(int j=0;j<4;j++)PW[j]=POW(A[L],j);
    for(int i=0;i<=L;i++)for(int j=0;j+1<=X && j<4;j++){
        P pre = PW[j]*A[i];
        if(pre!=P(2))continue; // 不是"i"
        for(set<P>::iterator it=Suf[i+1].begin();it!=Suf[i+1].end();it++){
            P suf = (*it) * PW[(X-j-1)%4];
            if(suf != P(4))continue; //不是"k"
            else{
                ok=true;
                break;
            }
        }
        int les=X-j-2;
        if(les<0)continue;
        for(int k=0;k<4 && k<=les;k++){
            for(set<P>::iterator it=Suf[1].begin();it!=Suf[1].end();it++){
                P suf = (*it) * PW[k];
                if(suf != P(4))continue; //不是"k"
                else{
                    ok=true;
                    break;
                }
            }
        }
        if(ok)break;
    }

    if(ok) return "YES";
    else   return "NO";
}
int main(){
    freopen("a.in","r",stdin);
    freopen("out.txt","w",stdout);

    int T;scanf("%d",&T);
    for(int i=1;i<=T;i++){
        printf("Case #%d: ",i);
        cout<<solve()<<endl;
    }
    return 0;
}
