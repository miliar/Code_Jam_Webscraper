#include <iostream>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <ctime>
#include <math.h>
#include <algorithm>
#include <iomanip>
#include <assert.h>
#include <map>
#include <queue>
#include <cstring>
#include <set>
#include <stack>
#include <numeric>
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
#define ifBit(n,i) ( ((n) >> (i)) & 1 )
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

int main()
{
	int T;
	cin >> T;
	int n;
	for(int t = 1 ; t <= T ; t++) {
		cin >> n;
		double a[n], b[n];
		for(int i = 0 ; i < n ; i++) {
			cin >> a[i];
		}
		for(int i = 0 ; i < n ; i++) {
			cin >> b[i];
		}

		int y = 0, z = 0;
		bool seen[n];
		memset(seen, false, sizeof seen);
		for(int i = 0 ; i < n ; i++) {
			int above = -1, below = -1;
			for(int j = 0 ; j < n ; j++) {
				if( seen[j] ) {
					continue;
				}
				if( b[j] > a[i] ) {
					if( above < 0 || b[above] > b[j] ) {
						above = j;
					}
				} else if( below < 0 || b[below] > b[j] ) {
					below = j;
				}
			}

			if( above >= 0 ) {
				y++;
				seen[above] = true;
			} else {
				seen[below] = true;
			}
		}


		sort(a, a + n);
		sort(b, b + n);
		int j = 0;
		int ken = 0;
		for(int i = 0 ; i < n ; i++) {
			while(j < n && b[j] < a[i]) {
				j++;
				ken++;
			}
			if( ken > 0 ) {
				ken--;
			} else {
				z++;
			}
		}

		printf("Case #%d: %d %d\n", t, n - z, n - y);
	}
}