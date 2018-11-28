/* Only for small */

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
#include <iomanip>
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
        double v,x;
        cin>>n>>v>>x;
        double r[n],c[n];
        double ret[n];
        REP(i,n) cin>>r[i]>>c[i];
        double tret=0.0;
        
        if(n==1){
            if(x!=c[0]) tret=-1.0;
            else tret=v/r[0];
        }else{
        double diff=(c[1]-c[0]);
            if(diff==0.0){
                if(x!=c[0]) tret=-1.0;
                else tret=v/(r[0]+r[1]);
            }else{
        ret[0]=v*((x-c[1])/(diff*-1.0));
        ret[1]=v*((x-c[0])/diff);
        
        
        REP(i,n){
            if(ret[i]<0.0){
                tret=-1.0;
                break;
            }else tret=max(ret[i]/r[i],tret);
        }}
        }
        if(tret<0.0) cout<<"IMPOSSIBLE\n";
        else cout<< fixed << setprecision(9)<<tret<<"\n";
    }
}
