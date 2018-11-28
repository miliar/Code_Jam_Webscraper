#include<bits/stdc++.h>
#define fs first
#define sc second
#define pb push_back
#define mp make_pair
using namespace std;
int T;
long long N,R,P,S;
long long NM;
string v[202020];
int OK;
string gets(int a,int b,int c) {
    if(a)
        return "R";
    if(b) return "P";
    return "S";
}
void rev(int st,int dr, int a,int b, int c) {
    //cout << st << " " << dr << endl;
    if(st==dr) {
        v[st] = gets(a,b,c);
    } else {
        if(a) {
            int mij = (st+dr) / 2;
            rev(st,mij,1,0,0);
            rev(mij+1,dr,0,0,1);
        }
        if(b) {
            int mij = (st+dr) / 2;
            rev(st,mij,0,1,0);
            rev(mij+1,dr,1,0,0);
        }
        if(c) {
            int mij = (st+dr) / 2;
            rev(st,mij,0,1,0);
            rev(mij+1,dr,0,0,1);
        }
    }
}
string srt(int st,int dr) {
    if(st == dr) {
        return v[st];
    }
    int mij = (st+dr) / 2;
    string a = srt(st,mij);
    string b = srt(mij+1,dr);
    if(a < b)
        return a + b;
    return b + a;
}
void make(int N,int R,int P,int S) {
    if(N==1) {
        rev(1,NM,R,P,S);
        return;
    }
    if((R + S - P) < 0) {
        OK = 1;
        return;
    }
    if( (R+P-S) < 0) {
        OK = 1;
        return;
    }
    if((P+S-R) < 0) {
        OK = 1;
        return;
    }
    int NR = (R + S - P)/2;
    int NP = (R+P-S) / 2;
    int NS = (P+S-R) / 2;
    make(N/2,NR,NP,NS);
}
int main() {
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    cin >> T;
    for(int tt=1;tt<=T;++tt) {
        //cout << "WTF";
        cin >> N >> R >> P >> S;
        NM = R+P+S;
        N = R + P + S;
        OK=0;
        make(N,R,P,S);
        //cout << "WTF" << endl;
        //for(int i=1;i<=N;++i)
        //    cout << v[i];
        //cout << endl;
        if(OK) {
            printf("Case #%d: IMPOSSIBLE\n",tt);
        } else {
            printf("Case #%d: ",tt);
            cout << srt(1,N) << endl;
        }
    }
}
