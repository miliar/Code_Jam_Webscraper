#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

#define dump(x)  cerr << #x << " = " << (x) << endl;
#define PB push_back
#define MP make_pair
#define ll long long

inline int toInt(string s){int v;istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x){ostringstream sout;sout<<x;return sout.str();}

vector<ll> ps;

bool isPs(ll arg){
    int n = ceil(log10(arg+1)) + 1, cnt = 0;
    char str[n];
    while(arg > 0){
        str[cnt] = arg % 10 + '0';
        arg /= 10;
        cnt++;
    }
    for(int i=0;i<cnt/2;i++){
        if(str[i] != str[cnt-1-i]){
            return false;
        }
    }
    return true;
}

int main(){
    int cases;
    ll tmp;
    cin >> cases;
    for(int i=0;i<10000001;i++){
        if(isPs(i)){
            tmp = (ll)i*i;
            if(isPs(tmp)){
                ps.push_back(tmp);
            }
        }
    }
    cerr << "calc end" << endl;
    for(int x=1;x<=cases;x++){
        ll a,b;
        cin >> a >> b;
        printf("Case #%d: %d\n", x, upper_bound(ps.begin(),ps.end(), b) - lower_bound(ps.begin(), ps.end(), a));
    }
}
