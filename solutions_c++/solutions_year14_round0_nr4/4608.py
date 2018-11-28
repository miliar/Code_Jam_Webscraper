#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector> 
#include<cstring>
#include<set>
#include<string>
#define mp make_pair
#define scn second
#define frs first
#define pb push_back
#define NAME "a"
#define fop freopen(NAME ".in", "r", stdin); freopen(NAME ".txt", "w", stdout); 
using namespace std;

typedef unsigned long long ull;
typedef long long ll;    	
typedef pair<int, int> pi;

void dout() { cerr << endl; }
template <typename Head, typename... Tail>
void dout(Head H, Tail... T) {
  cerr << H << ' ';
  dout(T...);
}

int main(){
	#ifdef LocalHost
		fop;
	#endif
		int t;
	scanf("%d", &t);
	int yt = 1;
	while (t --> 0) {
		set<double> g, b, b1, g1;
		vector<double> o, p;
	    int n;
	    double s;
	    scanf("%d", &n);                  
	    for (int i = 0; i < n; ++i)
	    	scanf("%lf", &s), g.insert(-s), g1.insert(s), o.pb(s);
	    for (int i = 0; i < n; ++i)
	    	scanf("%lf", &s), b.insert(-s), b1.insert(s), p.pb(s);
	    int ans1 = 0;
	    while (g.size() > 0) {
	   		while (g.size() > 0 && -(*g.begin()) < -(*b.begin())) {
	   			double now = -(*g.begin());
	   			double h = *g1.begin();
	   			g.erase(-h);
	   			g1.erase(h);
	   			now = *(b1.upper_bound(now));
	   			b.erase(-now);
	   			b1.erase(now);
	   		}
	   		if (g.size() > 0) {
	   			++ans1;
	   			double now = *b1.begin();
	   			b1.erase(now);
	   			b.erase(-now);
	   			double now1 = *(g1.upper_bound(now));
	   			g1.erase(now1);
	   			g.erase(-now1);	
	   		}	
		}	                     
		sort(o.begin(), o.end());
		sort(p.begin(), p.end());
		int u = 0, ans2 = 0;
		for (int i = 0; i < p.size(); ++i) {
			if (p[i] > o[u])
				++ans2, ++u;
		}

		printf("Case #%d: %d %d\n", yt, ans1, n - ans2);
		++yt;
	}
		
	return 0;



}