//ITNOA
#include<bits/stdc++.h> 

using namespace std;
 
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;

//#define int long long 
#define rep(i, s, e) for(int i = s; i < e; i ++)
#define X first
#define Y second

typedef long long ll;
typedef long double ld;

const int maxN = 2000*1000 + 5;
const int mod = 10429;
const int base = 701;
const int SQ = 500;
const int maxL = 20;



void solve()
{
    string s; cin >> s;
    int ans = 0, fl = 0;
    for(int i = (int)s.size()-1; i >= 0; i --)
    {
	int x = (s[i] == '-');
	if(x ^ fl)
	{
	    ans ++;
	    fl ^= 1;	
	}
    }
    cout << ans << endl;
}

int32_t main()
{
    ios::sync_with_stdio(0); cin.tie(0);
    int N; cin >> N;
    rep(i,1,N+1)
    {
	cout << "Case #" << i << ": ";
	solve();
    }
    return 0;    
}
