#include <cstdio>
#include <string>
using namespace std;

int n,p,r,s;
string gen(char x,int i){
    string tmp;
    if(i==0){
        char t[2];
        t[0]=x;
        t[1]=0;
        return string(t);
    }
    else{
        if(x=='P'){
            return min(gen('P',i-1)+gen('R',i-1),gen('R',i-1)+gen('P',i-1));
        }
        else if(x=='R'){
            return min(gen('R',i-1)+gen('S',i-1),gen('S',i-1)+gen('R',i-1));
        }
        else {
            return min(gen('S',i-1)+gen('P',i-1),gen('P',i-1)+gen('S',i-1));
        }
    }
}
void print(int ans){
    string tmp;
        if(ans==0)tmp="P";
        else if(ans==1)tmp="S";
        else tmp="R";
    printf("%s\n",gen(tmp[0],n).c_str());
}
int main (){
    int T;
    scanf("%d",&T);
    for(int I=1 ; I <= T ; I++){
        scanf("%d%d%d%d",&n,&r,&p,&s);
        int tp,tr,ts;
        tp=1;ts=0;tr=0;
        int ans=-1;
        for(int i = 0 ; i < n ; i ++){
            int np=tp+ts;
            int nr=tr+tp;
            int ns=ts+tr;
            tp=np;
            tr=nr;
            ts=ns;
        }
        if(tp==p&&tr==r&&ts==s) ans=0;
        else{
            tp=0;ts=1;tr=0;
            for(int i = 0 ; i < n ; i ++){
                int np=tp+ts;
                int nr=tr+tp;
                int ns=ts+tr;
                tp=np;
                tr=nr;
                ts=ns;
            }
            if(tp==p&&tr==r&&ts==s)ans=1;
            else{
                tp=0;ts=0;tr=1;
                for(int i = 0 ; i < n ; i ++){
                    int np=tp+ts;
                    int nr=tr+tp;
                    int ns=ts+tr;
                    tp=np;
                    tr=nr;
                    ts=ns;
                }
                if(tp==p&&tr==r&&ts==s)ans=2;
            }
        }
        printf("Case #%d: ",I);
        if(ans==-1)printf("IMPOSSIBLE\n");
        else print(ans);
    
    }



}
