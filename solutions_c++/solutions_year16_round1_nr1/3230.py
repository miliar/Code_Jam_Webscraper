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
#pragma unused(INF,PI,LINF)
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

const int mod=1000000007;

string lex_max(string s){
    char t[2100];
    int l=1050,r=1050,idx=0;
    t[l]=s[idx++];
    // final string is t[l..r]
    F(i,1,s.length()){
        if(s[i]>=t[l]) t[--l] = s[idx++];
        else t[++r] = s[idx++];
    }
    return string(t+l,r-l+1);
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
    F(i,0,t){
        string s;
        cin>>s;

        printf("Case #%d: ",i+1);
        cout<<lex_max(s)<<"\n";
    }
}
