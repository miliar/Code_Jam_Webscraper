#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
#define ll long long
#define ld long double
#define vi vector<int>
#define pb push_back
#define pii pair<int,int>
#define mp make_pair
#define st first
#define nd second
#define mini(a,b) a=min(a,(b))
#define maxi(a,b) a=max(a,(b))
#define RE(i,n) for(int i=0,_n=(n);i<_n;++i)
#define RI(i,n) for(int i=1,_n=(n);i<=_n;++i)
const int inf=1e9+5, nax=1e6+5;
#define B pair<pii, pii >
#define xlow first.first
#define ylow first.second
#define xhigh second.first
#define yhigh second.second

B t[nax];
int res[nax];

int cmp(int a, int b) {
	if(res[a] != res[b])
		return res[a] > res[b];
	return a > b;
}

int pizza(int a, int x, int y) {
	int dx;
	if(t[a].xhigh < x) dx = x - t[a].xhigh - 1;
	else if(x < t[a].xlow) dx = t[a].xlow - x - 1;
	else dx = 0;
	
	int dy;
	if(t[a].yhigh < y) dy = y - t[a].yhigh - 1;
	else if(y < t[a].ylow) dy = t[a].ylow - y - 1;
	else dy = 0;
	
	return max(dx, dy);
}

int odl(int a, int b) {
	//cout << a << " " << b << "\n";
	int res = inf;
	mini(res, pizza(a, t[b].xlow, t[b].ylow));
	mini(res, pizza(a, t[b].xhigh, t[b].ylow));
	mini(res, pizza(a, t[b].xlow, t[b].yhigh));
	mini(res, pizza(a, t[b].xhigh, t[b].yhigh));
	
	mini(res, pizza(b, t[a].xlow, t[a].ylow));
	mini(res, pizza(b, t[a].xhigh, t[a].ylow));
	mini(res, pizza(b, t[a].xlow, t[a].yhigh));
	mini(res, pizza(b, t[a].xhigh, t[a].yhigh));
	//cout << res << "\n";
	return res;
}

int Test() {
	int W, H, n;
	cin >> W >> H >> n;
	RI(i, n) {
		int a, b, c, d;
		cin >> a >> b >> c >> d;
		// x0, y0, x1, y1
		t[i] = mp(   mp(a, b),   mp(c, d)   );
	}
	t[0] = mp(   mp(-1, -1),    mp(-1, inf)   );
	t[n + 1] = mp(    mp(W, -1),    mp(W, inf)   );
	n += 2;
	// wlasnie ostatni sie zmienil !! 		UWAGA NA TO
	
	RE(i, n) res[i] = inf;
	res[0] = 0;
	
	vi w;
	RE(i, n) w.pb(i);
	sort(w.begin(), w.end(), cmp); // potrzebne, by na koncu byl pierwszy
	
	//RE(i, w.size()) cout << w[i] <<  " ";
	//cout << "\n";
	
	while(!w.empty()) {
		int a = w.back();
		//cout << " > " << a << "\n";
		w.pop_back();
		RE(i, w.size()) {
			int b = w[i];
			res[b] = min(res[b], res[a] + odl(a, b));
		}
		sort(w.begin(), w.end(), cmp);
	}
	return res[n - 1];
}

int main()
{
	ios_base::sync_with_stdio(0);
	int z;
	cin >> z;
	RI(i, z) {
		cout << "Case #" << i << ": " << Test() << "\n";
	}
	return 0;
}
