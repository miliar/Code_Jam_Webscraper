#include <bits/stdc++.h>

#define INF (1 << 29)
#define rep2(i,m,n) for(int i=(int)(m);i<(int)(n);i++)
#define rep(i,n) rep2(i,0,n)
#define EPS 1e-10

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> P;

int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};

string itoa(ll n){
    stringstream ss;
    ss << n;
    return ss.str();
}

ll solve(string str){
    ll res = 0;
    int sz = str.size();
    int pos = 0;
    while(pos < sz && str[pos]=='-') pos++;
    if(pos > 0) res++;
    while(pos < sz){
        while(pos<sz && str[pos]=='+') pos++;
        if(pos >= sz) break;
        res++;
        while(pos<sz && str[pos]=='-') pos++;
        res++;
    }
    return res;
}

int main()
{
    int n;
    cin >> n;
    rep(i,n){
        string str;
        cin >> str;
        cout << "Case #" << i+1 << ": " << solve(str) << endl;
    }
    return 0;
}

