#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>
#include <functional>
#include <numeric>
#include <bitset>

using namespace std;

template<typename T> ostream& operator<<(ostream& os, const vector<T>& v){
    os << "{ ";
    for(typename vector<T>::const_iterator it=v.begin(); it!=v.end(); ++it)
        os << '\"' << *it << '\"' << (it+1==v.end() ? "" : ", ");
    os << " }";
    return os;
}

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
#define vv(type,w,h,init) vector<vector<type>>(h,vector<type>(w,init))
typedef vector<string> vs;
typedef long long ll;
typedef unsigned uint;
typedef unsigned long ul;
typedef unsigned long long ull;

#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define loop(i,a,b) for(int i=(a); i<(int)(b); i++)
#define rep(i,b) loop(i,0,b)
#define pb push_back
#define mp make_pair

string const resstr[] = {"Impossible","Possible","No","Yes"};

template<typename T> void output(int n, T const & ans){
    printf("Case #%d: ",n);
    cout << ans << endl;
}

void solve(int n){
    vvi G1(4,vi(4));
    int a1; cin >> a1;
    bitset<17> can1;
    rep(i,4)rep(j,4){
        cin >> G1[i][j];
        if(i==a1-1) can1[G1[i][j]] = true;
    }

    vvi G2(4,vi(4));
    int a2; cin >> a2;
    bitset<17> can2;
    rep(i,4)rep(j,4){
        cin >> G2[i][j];
        if(i==a2-1) can2[G2[i][j]] = true;
    }

    bitset<17> C = can1&can2;
    int ans = C.count();

    if(ans==0){
        output(n,"Volunteer cheated!");
    } else if(ans==1){
        int t = 1;
        loop(i,1,17) if(C[i]) t = i;
        output(n,t);
    } else {
        output(n,"Bad magician!");
    }
}

int main(){
    int n; cin >> n;
    rep(i,n) solve(i+1);
}
