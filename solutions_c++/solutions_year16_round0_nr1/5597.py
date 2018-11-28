#include <cstdio>
#include <iostream>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cstring>
#include <bitset>
#include <deque>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>
#include <string>
#include <climits>
#include <cmath>

#define  each(v,c)  for(typeof((c).begin()) v = (c).begin(); v != (c).end(); ++v)
#define  sync(x)    ios_base::sync_with_stdio(x)
#define  sz(a)      ((int)(a.size()))
#define  all(a)     (a).begin(), (a).end()
#define  pb         push_back
#define  mp         make_pair
#define  fi         first
#define  se         second
using namespace std;

#define debug(a,n)    cerr << "["; for(int i = 0; i < n; ++i) cerr << a[i] << " ";cerr << "\b]\n";
#define dbg(args...)  {debug1,args; cerr<<endl;}
#define pause()       cin.get();cin.get();

struct debugger {
    template<typename T> debugger& operator , (const T& v) {
        cerr<<v<<" "; return *this;
    }
} debug1;

template <typename T1, typename T2>
inline ostream& operator << (ostream& os, const pair<T1, T2>& p) {
    return os << "(" << p.first << ", " << p.second << ")";
}

template<typename T>
inline ostream &operator << (ostream & os,const vector<T>& v) {
    bool first = true; os << "[";
    for (typename vector<T>::const_iterator ii = v.begin(); ii != v.end(); ++ii) {
        if(!first) os << ", ";
        os << *ii; first = false;
    }
    return os << "]";
}

typedef long long LL;
typedef pair<int,int> pii;
typedef pair<int,pii> piii;
typedef vector<int> vi;
const int inf = 0x7fffffff;

void modify(int &mask, long long sum)
{
	while ( sum ) {
		long long dig = sum % 10;
		mask |= (1 << dig);
		sum /= 10;
	}
	return;
}

int main()
{
	long long sum;
	int mask, n,t;
	cin >> t;
	for ( int i = 1; i <= t; i++ ) {
		cin >> n;
		cout << "Case #" << i << ": ";
		if ( n == 0 ) {
			puts("INSOMNIA");
			continue;
		}
		sum = mask = 0;
		
		while ( mask != (1 << 10) - 1 ) {
			sum += n;
			modify(mask, sum); 
		}
		cout << sum << endl;
	}
	return 0;
}