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
        int n;
        string s;
        cin>>n;
        cin>>s;
        int ret=0;
        int cnt=0;
        REP(i,n+1){
            if(cnt<i){
                ret+=i-cnt;
                cnt=i;
            }
            cnt+=s[i]-'0';
        }
        cout<<ret<<"\n";
    }
}