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

int exceed(int a,int tot){
    return (tot%2==0)?(a>tot/2):(a>=tot/2);
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
        int n;
        cin>>n;
        vi p(n);
        cin>>p;
        int total=0;
        F(i,0,n) total+=p[i];
        printf("Case #%d:",tt+1);
        while(total>0){
            int highest = max_element(all(p))-p.begin();
            p[highest]--;total--;
            int s_highest = max_element(all(p))-p.begin();
            p[s_highest]--;total--;
            int ok=true;
            F(i,0,n) if(exceed(p[i],total)) ok=false;
            if(ok) printf("%c%c ",'A'+highest,'A'+s_highest);
            else {
                printf("%c ",'A'+highest);
                p[s_highest]++;total++;
            }
        }
        printf("\n");
    }
}
