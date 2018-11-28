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
        int d;
        cin>>d;
        int p[1001];
        int pcnt[1001];
        int pmax=0;
        CLR(p);
        CLR(pcnt);
        int num;
        REP(i,d){
            cin>>num;
            p[num]++;
            pmax=max(pmax,num);
        }

        for(int i=pmax;i>=1;i--){
            if(p[i]){
                FOR(j,1,i){
                    pcnt[j]+=p[i]*((int)(ceil((double)i/(double)j))-1);
                }
            }
        }
        int ret=INT_MAX;
        FOR(i,1,pmax+1){
            
                ret=min(ret,i+pcnt[i]);
            
        }
        cout<<ret<<"\n";
    }
}