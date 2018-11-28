#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<string.h>
#include<vector>
#include<set>
#include<map>
#include<cstdio>
#include<queue>
#include<sstream>
#include<list>
#include<bitset>
#include<ctime>
using namespace std;

typedef long long Int;
#define FOR(i,a,b) for(int i=(a); i<=(b);++i)
#define mp make_pair
#define pb push_back
#define sz(s) (int)((s).size())
const int inf = 1000000000;
const int MOD = 1000000007;
const double pi=acos(-1.0);

string M="1ijki1kjjk1ikji1";

inline int id(int a) {
    a=abs(a);
    if(a=='1') return 0;
    if(a=='i') return 1;
    if(a=='j') return 2;
    if(a=='k') return 3;
}

inline int mult(int A, int B) {
    int a=abs(A);
    int b=abs(B);
    int res=M[id(a)*4+id(b)];
    if(a=='i' && (b=='i' || b=='k')) res=-res;
    if(a=='j' && (b=='i' || b=='j')) res=-res;
    if(a=='k' && (b=='j' || b=='k')) res=-res;
    if(A<0 && B>0 || A>0 && B<0) res=-res;
    return res;
}

int f[210009];

int main() {
	freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	int t;cin>>t;
	FOR(t_,1,t) {
        cerr<<t_<<endl;
        Int L,X;
        cin>>L>>X;
        //if(t_==30) cerr<<L<< " "<<X<<endl;
        if(X>=11) {
            int x=11;
            while(x%4!=X%4)x++;
            X=x;
        }
        string ss;cin>>ss;

        string s="";
        FOR(i,1,X) FOR(j,0,sz(ss)-1) s+=ss[j];
        string ans="NO";
        f[sz(s)]='1';
        for(int i=sz(s)-1; i>=0; --i) {
            f[i]=mult(s[i], f[i+1]);
        }

        int pr='1';
        FOR(i,0,sz(s)-2) {
            pr=mult(pr, s[i]);
            if(i>4*L) break;
            if(pr!='i' || ans=="YES") continue;

            //cerr<<i<<endl;

            int md='1';
            for(int j=i+1; j<sz(s)-1; ++j) {
                if(j-i>4*L) break;
                md=mult(md, s[j]);
                if(md!='j') continue;
                if(f[j+1]=='k') ans="YES";
            }
        }

        cout<<"Case #"<<t_<<": "<<ans<<endl;
	}
}
