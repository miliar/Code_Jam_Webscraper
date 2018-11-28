#include <bits/stdc++.h>

using namespace std;

#define rep(i,n)    for(int (i)=0; (i)<(int)(n); ++(i))
#define each(itr,c) for(__typeof((c).begin()) itr=(c).begin(); itr!=(c).end(); ++itr)
#define all(a)      a.begin(), a.end()
#define mp          make_pair
#define pb          push_back
#define F           first
#define S           second
#define mod         1000000009
typedef long long               ll;
typedef unsigned int            uint;
typedef unsigned long long      ull;

int solve(vector<int> & s){
    int j=0;
    rep(i, s.size()){
        while(s[i]>j){
            ++j;
        }
        ++j;
    }
    return j-s.size();
}

int main(){
    vector<int> qcase;
    int cases;
    int res;
    cin>>cases;
    rep(i,cases){
        int smax;
        string scount;
        cin>>smax>>scount;
        rep(j,smax+1){
            rep(k,scount[j]-'0'){
                qcase.pb(j);
            }
        }
        res=solve(qcase);
        qcase.clear();
        cout<<"Case #"<<i+1<<": "<<res<<"\n";
    }
    return 0;
}
