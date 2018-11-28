#include <bits/stdc++.h>
#define q1 0
#define qi 1
#define qj 2
#define qk 3
#define qn1 4
#define qni 5
#define qnj 6
#define qnk 7
using namespace std;
int operation[4][4];
int st[10001];
int L,X;
int toPos(int a){
    if(a>=4) return a-4;
    return a;
}
int getOperation(int a,int b){
    return operation[a][b];
}
int neg(int a){
    if(a<4) return a+4;
    return a-4;
}
int quat(int a,int b){
    if(a>=4 && b<4 || a<4 && b>=4){
        return neg(getOperation(toPos(a),toPos(b)));
    }
    return getOperation(toPos(a),toPos(b));
}
int eval(unsigned long long s,unsigned long long e){
    if(s>=e)
        return st[s%L];
    int m = (s+e)/2;
    return quat(eval(s,m),eval(m+1,e));
}
int main(){
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    operation[q1][q1]=q1;
    operation[q1][qi]=qi;
    operation[q1][qj]=qj;
    operation[q1][qk]=qk;

    operation[qi][q1]=qi;
    operation[qi][qi]=qn1;
    operation[qi][qj]=qk;
    operation[qi][qk]=qnj;

    operation[qj][q1]=qj;
    operation[qj][qi]=qnk;
    operation[qj][qj]=qn1;
    operation[qj][qk]=qi;

    operation[qk][q1]=qk;
    operation[qk][qi]=qj;
    operation[qk][qj]=qni;
    operation[qk][qk]=qn1;
    int T;
    cin>>T;
    for(int c=1;c<=T;c++){
        cin>>L>>X;
        cout<<"Case #"<<c<<": ";
        for(int i=0;i<L;i++){
            char x; cin>>x;
            if(x=='i') st[i]=qi;
            if(x=='j') st[i]=qj;
            if(x=='k') st[i]=qk;
        }
        bool ok=false;
        if(eval(0,L*X-1) != quat(qi,quat(qj,qk))){ cout<<"NO"<<endl; continue;}

        int ci=0;
        for(ci=0;ci<L*X;ci++){
                if(eval(0,ci)== qi)
                    break;
        }
        int ck=0;
        if(eval(ci+1,L*X-1) == quat(qj,qk)){
            for(ck=L*X-1;ck>ci && ck>0;ck--){
                if(eval(ck,L*X-1) == qk && eval(ci+1,ck-1) == qj){
                   ok=true; break;
                }
                if(eval(ck,L*X-1) == qj && eval(ci+1,ck-1) == quat(qj,qi)){
                    ok=true; break;
                }
            }
        }
        if(ok) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
}
