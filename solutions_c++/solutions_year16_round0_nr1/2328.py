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

string solve(int n){
    if(n==0) return "INSOMNIA";
    set<int> memo;
    ll tmp = n;
    while(1){
        ll t = tmp;
        while(t>0){
            memo.insert(t%10);
            t /= 10;
        }
        if(memo.size()>=10){
            return itoa(tmp);
        }
        tmp += n;
    }
    return "INSOMNIA";
}

int main()
{
    int n;
    cin >> n;
    rep(i,n){
        int m;
        cin >> m;
        cout << "Case #" << i+1 << ": " << solve(m) << endl;
    }
    return 0;
}

