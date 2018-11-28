#include <iostream>
#include <cassert>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <ctime>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <string>
#include <bitset>
#include <vector>
#include <complex>
#include <algorithm>
using namespace std;
typedef long long ll;
typedef double db;
typedef pair<int,int> pii;
typedef vector<int> vi;
#define de(x) cout << #x << "=" << x << endl
#define rep(i,a,b) for(int i=a;i<(b);++i)
#define per(i,a,b) for(int i=(b)-1;i>=(a);--i)
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define mp make_pair
#define pb push_back
#define fi first
#define se second

int n,x;
string s;

int main(){
    cin >> n;
    rep(i,0,n){
        cin >> s >> x;
        cout << "Case #" << i+1 << ": ";
        int res=0;
        rep(i,0,sz(s)-x+1) if(s[i]=='-'){
            res++;rep(j,0,x) s[i+j]^='-'^'+';
        }
        rep(i,0,sz(s)) if(s[i]=='-') res=-1;
        if(res==-1) cout<<"IMPOSSIBLE"<<endl;
        else cout<<res<<endl;
    }
    return 0;
}
