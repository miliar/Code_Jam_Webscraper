//  Created by Vignesh Manoharan

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <cstring>
#include <cassert>
#include <numeric>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<vi> vvi;
typedef vector<ii> vii;

const int INF = 1000000000;
const ll LINF = 1e17;
const double PI =3.141592653589793238;
const int mod=1000000007;
#pragma unused(INF,PI,LINF,mod)
#define F(i,a,n) for(int i=(a);i<(n);i++)

template<typename T,typename TT> ostream& operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream& operator<<(ostream &s,vector<T> t){
    for(int i=0;i<(t).size();i++)s<<t[i]<<((i<(t).size()-1)?" ":"");return s; }
template<typename T> ostream& operator<<(ostream &s,set<T> t){for(T x:t) s<<x<<" ";return s; }
template<typename T> istream& operator>>(istream &s,vector<T> &t){
    for(int _i=0;_i<t.size();_i++) s>>t[_i];return s; }

#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()

int result(char c1,char c2){
    if(c1>c2) swap(c1,c2);
    if(c1=='P'){
        if(c2=='R') return 'P';
        else return 'S';
    }
    return 'R';
}
int check_terminate(string s,int n,int N){
    F(level,0,n){
        int mult = (1<<level);
        for(int i=0; i<N; i+=2*mult){
            if(s[i] == s[i+mult]) return false;
            s[i] = result(s[i], s[i+mult]);
        }
    }
    return true;
}
int main(int argc, const char * argv[]) {
#ifdef local_test
    // input
    //    freopen("input","w",stdout);
    //    cout<<"1000000\n";
    //    F(i,0,1000000) cout<<i<<"\n";
    freopen("input","r",stdin);
    freopen("output","w",stdout);
#endif
    int t;
    cin>>t;
    F(tt,0,t){
        int n,N;
        int r,p,s;
        cin>>n>>r>>p>>s;
        N=(1<<n);
        string perm(N,'P');
        F(i,0,p) perm[i]='P';
        F(i,p,p+r) perm[i]='R';
        F(i,p+r,p+r+s) perm[i]='S';
        printf("Case #%d: ",tt+1);
        int done=false;
        do{
            if(check_terminate(perm, n, N)) {
                cout<<perm<<"\n";
                done=true;
                break;
            } else {
//                cout<<"wrong "<<perm<<"\n";
            }
        }while(next_permutation(all(perm)));
        if(!done) cout<<"IMPOSSIBLE\n";
    }
}
