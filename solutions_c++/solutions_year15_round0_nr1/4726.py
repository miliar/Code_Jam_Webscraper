#include <algorithm>
#include <functional>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <bitset>
#include <climits>

#define all(c) (c).begin(), (c).end()
#define rep(i,n) for(int i=0;i<(n);i++)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)
#define fr first
#define sc second

const int INF=100000000;
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};
using namespace std;
typedef pair<int ,int > P;
typedef long long ll;

bool ok(int k,string s) {
    rep(i,s.size()) {
        if(i>k) return false;
        k+=s[i]-'0';
    }
    return true;
}

void small() {
    int n;
    string s;
    cin>>n;
    cin>>s;
    rep(i,2000) if(ok(i,s)) {
        cout<<i<<endl;
        return;
    }
}

int main() {
    int T;
    cin>>T;
    rep(i,T) {
        printf("Case #%d: ",i+1);
        small();
    }
    return 0;
}

