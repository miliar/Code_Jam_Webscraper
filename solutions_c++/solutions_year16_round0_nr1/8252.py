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

int time_taken(int n){
    int count=0;
    vi digs(10);
    if(n==0) return -1;
    int i=0;
    while(count<10){
        i++;
        int m=i*n,d;
        while(m>0){
            d=m%10;
            m/=10;
            if(!digs[d]) digs[d]=1,count++;
        }
    }
    return i*n;
}

int main(int argc, const char * argv[]) {
#ifdef local_test
// input
//    freopen("input","w",stdout);
//    cout<<"1000000\n";
    F(i,0,1000000) cout<<i<<"\n";
    freopen("input","r",stdin);
    freopen("output","w",stdout);
#endif

    int t;
    cin>>t;
    F(i,0,t){
        int n;
        cin>>n;
        printf("Case #%d: ",i+1);
        int time=time_taken(n);
        if(time==-1) printf("INSOMNIA\n");
        else printf("%d\n",time);
    }
}
