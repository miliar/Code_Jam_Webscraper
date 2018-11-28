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

bool mark[10];
int cnt = 0;
void add(ll x)
{
    while(x)
    {
	if(mark[x % 10] == 0)
	{
	    mark[x % 10] = 1;
	    cnt ++;
	}
	x /= 10;
    }    
}

void solve()
{
    ll n; cin >> n;
    if(n == 0) { cout << "INSOMNIA" << endl; return; }
    memset(mark,0,sizeof mark);
    cnt = 0;

    ll tmp = 0;
    while(cnt < 10)
    {
	tmp ++;
	add(tmp * n);
    }   
    cout << tmp * n << endl;	        
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
