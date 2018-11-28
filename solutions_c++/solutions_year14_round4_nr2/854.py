#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long int ull;
typedef long long int ll;
#define vi vector<int>
#define vvi vector< vector<int> >
#define vd vector<double>
#define vb vector<bool>
#define vs vector<string>
#define pi pair<int,int>
#define pb push_back
#define out(a) cout<<(a)<<endl
#define pout(a) cout<<(a).first<<' '<<(a).second<<endl
#define sz(c) (int)(c).size()
#define fr(n,i) for(int (i)=0;(i)<(n);(i)++)
#define rng(s,e,i) for(int (i)=(s);(i)<=(e);(i)++)
#define all(c) (c).begin(),(c).end()
#define isBit(n,i) ( ((n) >> (i)) & 1 )
#define fill(arr, v) memset(arr, v, sizeof(arr))
#define mp make_pair
template<typename typ> void vout(vector<typ>& v){for(int vint=0;vint<sz(v);vint++){cout<<(v)[vint];if(vint==sz(v)-1) cout<<endl;else cout<<' ';}}
template<typename typ> void arrout(typ* arr,int l){for(int i=0;i<l;i++){cout<<arr[i];if(i<l-1) cout <<' ';else cout<<endl;}}

#ifdef DEBUG
	#define debug(args...)            {dbg,args; cerr<<endl;}
#else
	#define debug(args...)              // Just strip off all debug tokens
#endif

struct debugger
{
	template<typename T> debugger& operator , (const T& v)
	{
		cerr<<v<<" ";
		return *this;
	}
}dbg;

int a[10001];
int n;

int main()
{
	int T;
	cin >> T;
	for(int t = 1 ; t <= T ; t++) {
		cin >> n;
		for(int i = 0 ; i < n ; i++) {
			cin >> a[i];
		}

		int ans = 0;
		bool used[n];
		fill(used, false);
		for(int i = 0 ; i < n ; i++) {
			int mn = -1, left = 0, seen = 0;
			for(int j = 0 ; j < n ; j++) {
				if( !used[j] ) {
					seen++;
					if( mn == -1 || a[j] < a[mn] ) {
						mn = j;
						left = seen;
					}
				}
			}

			used[mn] = true;
			ans += min(left - 1, n - i -left);
		}
		printf("Case #%d: %d\n", t, ans);
	}
}