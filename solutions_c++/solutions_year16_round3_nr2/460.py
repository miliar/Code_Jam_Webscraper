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

vi binary(long long m){
    vi b(18);
    if(m<=0) return b;
    int i=0;
    while(m>0){
        b[i++]=m%2;
        m/=2;
    }
    return b;
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
        int b;long long m;
        cin>>b>>m;
        printf("Case #%d: ",tt+1);

        long long max_paths = 1ll<<(b-2);
        vi mark(b-1);
        if(m>max_paths) printf("IMPOSSIBLE\n");
        else {
            printf("POSSIBLE\n");
            if(m==max_paths){
                mark = vi(b-1,1);
            } else {
                vi bin = binary(m);
//                cout<<"bin "<<bin<<"\n";
                F(i,1,b-1) mark[i]=bin[i-1];
            }
//            cout<<"mark "<<mark<<"\n";
            F(i,0,b-1){
                F(j,0,i+1) printf("0");
                F(j,i+1,b-1) printf("1");
                printf("%c\n",(mark[i]?'1':'0'));
            }
            F(i,0,b) printf("0");printf("\n");
        }
    }
}
