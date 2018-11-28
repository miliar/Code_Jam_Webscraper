#include <iostream>
#include <cstdio>
#include <iomanip>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <stack>
#include <utility>
#include <numeric>
#include <algorithm>
#include <functional>
#include <cctype>
#include <complex>
#include <string>
#include <sstream>

using namespace std;

#define all(c) c.begin(),c.end()
#define rall(c) c.rbegin(),c.rend()
#define rep(i,n) for(int i=0;i<(n);i++)
#define tr(it,container) for(typeof(container.begin()) it = container.begin(); \
                                                  it != container.end(); ++it)
#define mp(a,b) make_pair((a),(b))
#define eq ==

typedef long long ll;
typedef complex<double> point;
typedef pair<int,int> pii;

// →↑←↓
const int dx[] = {1,0,-1,0};
const int dy[] = {0,-1,0,1};


const double EPS = 1e-9;



bool ispalin(ll t){
    stringstream ss;
    ss << t;
    string s;
    ss >> s;
    for(int j=0;j<(int)s.size();j++){
        if(s[j] != s[s.size()-1-j]){
            return false;
        }
    }
    return true;
}

int main(){
    vector<ll> target;
    const ll MAX = 10000000;
    for(ll i=1;i<=MAX;i++){
        ll t;
        if(ispalin(i) and ispalin(t=i*i)){
            target.push_back(t);
        }
    }

    /*
    cout << target.size() << endl;
    for(int i=0;i<target.size();i++){
        cout << target[i] << " ";
    }
    cout << endl;

    */
    int T;
    cin >> T;
    for(int casei=1;casei<=T;casei++){
        ll A,B;
        cin >> A >> B;
        int cnt = upper_bound(all(target),B) - lower_bound(all(target),A);
        cout << "Case #" << casei << ": " << cnt << endl;
    }
    return 0;
}
