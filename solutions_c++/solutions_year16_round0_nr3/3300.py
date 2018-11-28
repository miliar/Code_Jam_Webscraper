
/****** BISMILLAH HIR RAHMANIR RAHIM ******/

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned int ul;
typedef unsigned long long ull;
typedef vector <int> vi;
typedef map<string,string> mss;
typedef map<int, vector<int> > mvii;
typedef map<int, int> mii;
typedef queue <int> qi;
typedef map <int, vector<string> > mvis;
typedef map <string, vector<int> > mvsi;
typedef vector <string> vs;
typedef pair <int, int> pii;

#define MP make_pair
#define SORT(a) sort (a.begin(), a.end())
#define REVERSE(a) reverse (a.begin(), a.end())
#define ALL(a) a.begin(), a.end()
#define PI acos(-1)
#define ms(x,y) memset (x, y, sizeof (x))
#define INF 2000000000
#define pb push_back
#define MAX 100002
#define debug cout<<"A"<<"\n"
#define prnt(a) cout<<a<<"\n"
#define mod 1000000007LL
#define FOR(i,a,b) for (int i=(a); i<(b); i++)
#define FORr(i,a,b) for (int i=(a); i>=b; i--)
#define itrALL(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define lc ((node)<<1)
#define rc ((node)<<1|1)
#define VecPrnt(v) FOR(j,0,v.size()) cout<<v[j]<<" "; cout<<endl
#define endl "\n"
#define PrintPair(x) cout<<x.first<<" "<<x.second<<endl


/* Direction Array */

// int fx[]={1,-1,0,0};
// int fy[]={0,0,1,-1};
// int fx[]={0,0,1,-1,-1,1,-1,1};
// int fy[]={-1,1,0,0,1,1,-1,-1};

template <class T> inline T bigmod(T p,T e,T M)
{
    ll ret = 1;
    for(; e > 0; e >>= 1)
    {
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    } return (T)ret;
}

template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}
template <class T> inline T lcm(T a,T b) {a=abs(a);b=abs(b); return (a/gcd(a,b))*b;}
template <class T, class X> inline bool getbit(T a, X i) { T t=1; return ((a&(t<<i))>0);}
template <class T, class X> inline T setbit(T a, X i) { T t=1;return (a|(t<<i)); }
template <class T, class X> inline T resetbit(T a, X i) { T t=1;return (a&(~(t<<i)));}

inline ll power(ll a, ll b)
{
	ll multiply=1;
	FOR(i,0,b)
	{
		multiply*=a;
	}
	return multiply;
}

/****** END OF HEADER ******/

string toBin(ll n)
{
	string temp="";

	while(n)
	{
		int r=n%2;
		temp=char(r+'0')+temp;
		n/=2;
	}

	return temp;
}

set<string> all;

int main()
{
	// ios_base::sync_with_stdio(0); 
	// cin.tie(NULL); cout.tie(NULL);
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	// prnt(toBin(5));
	int test;
	cin>>test;

	int n, j;

	cin>>n>>j;

	string now="1";

	for(int i=0; i<n-6; i++)
	{
		now+='0';
	}

	now+="11111";

	// prnt(now);

	prnt("Case #1:");

	do
	{
		bool flag=false;

		int cnt1=0, cnt2=0;

		FOR(i,1,now.size()-1)
		{
			if(now[i]=='0') continue;
			if(i%2) cnt1++;
			else cnt2++;
		}
		if(cnt1==cnt2)
			all.insert(now);
		if(all.size()==j) break;
	} while(next_permutation(now.begin()+1,now.end()-1));

	for(auto it: all)
	{
		// prnt(it);
		cout<<it;

		FOR(i,2,11) cout<<" "<<i+1;
		cout<<endl;
	}

	return 0;
}







