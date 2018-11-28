#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef long double ld;
typedef map<ll,ll>::iterator mapit;
typedef set<pii>::iterator setit;
const int maxn = 3e5 + 5;
const int maxlog = 20;
const int inf = 2e9 + 4;
bool b[maxn];
void ok(ll a){
    while(a){
        ll d = a % 10;
        a /= 10;
        b[d] = true;
    }
}
ll solve(ll a){
    int t = 1000;
    for(int i = 0 ; i < 10 ; i ++ )
        b[i] = false;
    ll cur = a;
    while(t -- ){
        ok(cur);
        bool check = true;
        for(int i = 0 ; i < 10 ; i ++ )
            if(!b[i])
                check = false;
        if(check)
            return cur;
        cur += a;
    }
    return -1;
}
int main()
{
	ios_base::sync_with_stdio(false) , cin.tie(0) , cout.tie(0); cout.precision(20);
	ifstream fin("A-large.in.");
	ofstream fout("c.txt");
	int t;
	fin >> t;
	for(int test = 1 ; test <= t ; test ++ ){
        ll n ;
        fin >> n;
        ll ans = solve(n);
        fout << "Case #" << test << ": ";
        if(ans == -1)
            fout << "INSOMNIA";
        else
            fout << ans;
        fout << endl;
	}
	return 0;
}
