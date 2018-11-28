
#include<iostream>
#include<sstream>
#include<vector>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<functional>
#include<climits>
#include<utility>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int,int> pi;

#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define FORB(i,s,e,st) for (int i = int(s); i < int(e); i+=(int(st)))
#define FOR(i,s,e) FORB(i,s,e,1)
#define REP(i,x) FOR(i,0,x)
#define CLR(a) memset((a), 0 ,sizeof(a))


const int MOD = 1000000007;
const double PI  = acos(-1.0);


int main(){
    int T;
    cin>>T;
    REP(t,T){
        cout<<"Case #"<<(t+1)<<": ";
        ll k,c,s;
        cin>>k>>c>>s;
        if(c*s<k) cout<<"IMPOSSIBLE\n";
        else{
            int cnt=(k+c-1)/c;
            REP(i,cnt){
                ll a=c*i,b=c*(i+1);
                if(i==cnt-1){
                    b=k;
                    a=max(k-c,0);
                }
                ll ret=1;
                while(a!=b){
                    ret=(ret-1)*k+(++a);
                }
                cout<<ret<<" ";
            }
            cout<<"\n";
        }
    }
}