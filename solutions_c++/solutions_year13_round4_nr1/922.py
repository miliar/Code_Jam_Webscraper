#include "std.h"
#include "debug.h"
#include <string.h>

//int v[128];
int mat[100][100];
char buf[1024];

struct Trip
{
    int o;
    int e;
    int p;
};

bool cmpo(const Trip& t, const Trip& tt)
{
    if (t.o != tt.o) return t.o < tt.o;
    return t.e < tt.e;
}

bool cmpe(const Trip& t, const Trip& tt)
{
    if (t.e != tt.e) return t.e < tt.e;
    return t.o < tt.o;
}

int main() {
    int T;
    cin >> T; cin.getline(buf, sizeof buf);
    FOR(tt, T)
    {
	ull M, N;
	cin >> N >> M; cin.getline(buf, sizeof buf);
	//	cerr << "Case " << tt << V(A) << V(n) << endl;
	
	vector<Trip> vo, ve;
	set<int> s;
	ull price0 = 0, price1 = 0;
	const ull mod = 1000002013;
	FOR(i, M)
	{
	    Trip t;
	    cin >> t.o >> t.e >> t.p;
	    vo.pb(t);
	    assert(t.o < t.e);
	    s.insert(t.o);
	    s.insert(t.e);
	    cin.getline(buf, sizeof buf);
	    ull d = t.e - t.o;
	    ull p0 = N * d - d * (d-1) / 2;
	    price0 += ((p0 % mod) * t.p) % mod;
	}
	ve = vo;
	sort(vo.begin(), vo.end(), cmpo);
	sort(ve.begin(), ve.end(), cmpe);
	map<int, ull> m;	// origin -> total #tickets held
	int oidx = 0, eidx = 0;
	FOREACH(it, s)
	{
	    int loc = *it;
	    assert(oidx == M || loc <= vo[oidx].o);
	    assert(eidx == M || loc <= ve[eidx].e);
	    
	    while (oidx < M && loc == vo[oidx].o)
	    {
		m[loc] += vo[oidx].p;
		oidx++;
	    }

	    while (eidx < M && loc == ve[eidx].e)
	    {
		ull p = ve[eidx].p;
		for(__typeof(m.rbegin()) it=m.rbegin(); it!=m.rend(); it++)
		{
		    ull pp = it->second;
		    ull pused = min(pp, p);
		    int d = loc - it->first;
		    ull p1 = N * d - d * (d-1) / 2;
		    price1 += ((p1 % mod) * pused) % mod;
		    it->second -= pused;
		    p -= pused;
		    if (!p) break;
		}
		assert(!p);
		eidx++;
	    }
	}

	price1 %= mod;
	ull ret = (price0 + mod - price1) % mod;

	cout << "Case #"<<(tt+1)<<": ";

	cout << ret << endl;
    }
    return 0;
}
