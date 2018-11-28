#pragma comment(linker, "/stack:256000000")

#include <algorithm>
#include <iostream>
#include <cassert>
#include <iomanip>
#include <climits>
#include <utility>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <bitset>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <set>
#include <map>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(a, b) make_pair((a), (b))
#define x first
#define y second
#define ft first
#define sc second

using namespace std;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = INT_MAX / 2;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

const int N = 10 + 1;

int n;
int a[N];

inline bool read()
{
	if (scanf("%d", &n) != 1)
		return false;

	forn(i, n)
		assert(scanf("%d", &a[i]) == 1);

    return true;
}

inline int hash(const vector<int> &a)
{
	int h = 0;

	forn(i, sz(a))
		h = (h * int(1000 * 1000 * 1000 + 7)) + int(a[i]);

	return h;
}

map<int, int> z;
map<int, int> RES;

inline int finish(const vector<int>& a)
{
	int i = 0;

	while(i < n)
	{
		if (i + 1 == n || a[i] < a[i + 1])
			i++;
		else
			break;
	}

	while(i < n)
	{
		if (i + 1 == n || a[i] > a[i + 1])
			i++;
		else
			break;
	}

	return i == n;
}

inline int solve(const vector<int>& s)
{
	queue< vector<int> > q;
	q.push(s);
	z[hash(s)] = 0;

	while(!q.empty())
	{
		vector<int> a = q.front();
		q.pop();

		li ha = hash(a);

		int dv = z[ha];

		if (finish(a))
			return dv;

		vector<int> next = a;

		forn(i, n - 1)
		{
			swap(next[i], next[i + 1]);

			int hnext = hash(next);
			if (!z.count(hnext))
			{
				z[hnext] = dv + 1;
				q.push(next);
			}

			swap(next[i], next[i + 1]);
		}
	}

	throw;
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);

	z.clear();
	vector<int> start;
	forn(i, n)
		start.pb(a[i]);

	int ans;
	if (RES.count(hash(start)))
		ans = RES[hash(start)];
	else
	{
		 ans = solve(start);
		 RES[ hash(start) ] = ans;
	}

	cout << ans << endl;
	cerr << test + 1 << endl;
}

inline void precalc()
{
RES[477788433] = 10;
RES[-1884744005] = 12;
RES[1487382330] = 6;
RES[254319777] = 2;
RES[1628479554] = 0;
RES[-802228414] = 0;
RES[-1011102616] = 1;
RES[-1405021117] = 12;
RES[-1644605736] = 11;
RES[-864455649] = 1;
RES[-290246410] = 1;
RES[1144624451] = 2;
RES[-978553449] = 6;
RES[-666632506] = 0;
RES[-1123153412] = 0;
RES[394052572] = 0;
RES[-452723177] = 9;
RES[-2017112179] = 8;
RES[-1661296352] = 20;
RES[1256207144] = 0;
RES[1741466904] = 8;
RES[-1481364447] = 12;
RES[1745537422] = 9;
RES[995949899] = 0;
RES[-402098242] = 20;
RES[1794199785] = 8;
RES[-230582884] = 0;
RES[117373359] = 4;
RES[1627867671] = 0;
RES[-2079366947] = 10;
RES[-1338723297] = 12;
RES[-367322786] = 8;
RES[-1291121606] = 0;
RES[-1833259770] = 16;
RES[82421065] = 3;
RES[-1552263153] = 0;
RES[-1519821543] = 7;
RES[-712305728] = 0;
RES[-2027368313] = 12;
RES[-1287804519] = 8;
RES[-2048154567] = 20;
RES[-1518777565] = 0;
RES[1362190244] = 4;
RES[619546954] = 7;
RES[137401109] = 6;
RES[463489367] = 0;
RES[-1632562971] = 20;
RES[-585535509] = 7;
RES[524959513] = 20;
RES[-624274953] = 6;
RES[162817861] = 11;
RES[-1081922554] = 10;
RES[-1162586563] = 16;
RES[-2018553737] = 0;
RES[319594441] = 16;
RES[1053039939] = 11;
RES[968240989] = 7;
RES[1470283871] = 20;
RES[-257971541] = 3;
RES[2010997922] = 8;
RES[-1126530368] = 7;
RES[-31468792] = 3;
RES[-1437994141] = 9;
RES[-311576676] = 13;
RES[-833116158] = 7;
RES[1646061000] = 20;
RES[-827024646] = 10;
RES[-568731948] = 9;
RES[-1918421365] = 7;
RES[-1459079409] = 20;
RES[594599095] = 20;
RES[224711289] = 12;
RES[1975532078] = 7;
RES[521966918] = 9;
RES[848347080] = 8;
RES[2126664618] = 20;
RES[-1685500244] = 20;
RES[-747501111] = 6;
RES[-1554322139] = 15;
RES[2114952542] = 6;
RES[1267202948] = 20;
RES[903329710] = 13;
RES[2047725110] = 5;
RES[-1351066569] = 0;
RES[899342004] = 6;
RES[-1495984437] = 12;
RES[-1537461089] = 2;
RES[2126310937] = 10;
RES[-525902089] = 0;
RES[-1436502441] = 4;
RES[-850704557] = 6;
RES[517153303] = 13;
RES[-414050920] = 0;
RES[1424577418] = 16;
RES[-1176702324] = 4;
RES[-2067767444] = 0;
RES[-724279423] = 1;
RES[1647760178] = 15;
RES[858049316] = 7;
RES[1505948257] = 7;

RES[1385913529] = 20;
RES[-789233839] = 4;
RES[-1669807580] = 16;
RES[767958820] = 0;
RES[-1747280498] = 10;
RES[-1879157881] = 2;
RES[-250742926] = 7;
RES[-1269064798] = 20;
RES[494026272] = 7;
RES[69174714] = 2;
RES[-479720492] = 1;
RES[1680225597] = 9;
RES[-752063473] = 6;
RES[-1107579270] = 4;
RES[-1944955205] = 9;
RES[-92132921] = 20;
RES[963855668] = 10;
RES[1266775669] = 11;
RES[1203904480] = 10;
RES[1142154912] = 0;
RES[-1037295775] = 5;
RES[1044124661] = 12;
RES[-294210149] = 7;
RES[345260043] = 8;
RES[-1881242561] = 20;
RES[1750109155] = 9;
RES[1016066271] = 1;
RES[919684134] = 20;
RES[-1513500784] = 20;
RES[405854720] = 7;
RES[-1518475295] = 0;
RES[-733583033] = 13;
RES[-862057842] = 6;
RES[-1959798084] = 14;
RES[528477682] = 8;
RES[-281680549] = 1;
RES[-776178920] = 0;
RES[-866549817] = 8;
RES[-693403361] = 1;
RES[1826174029] = 20;
RES[698220078] = 9;
RES[-709324436] = 20;
RES[1020505126] = 7;
RES[-1743945475] = 7;
RES[-98614139] = 2;
RES[1917916609] = 11;
RES[1408199821] = 0;
RES[-391945164] = 0;
RES[1225388493] = 9;
RES[-886404654] = 12;
RES[-840396678] = 0;
RES[-885784882] = 8;
RES[1691894480] = 7;
RES[1292610057] = 7;
RES[-596787755] = 9;
RES[-1784748742] = 11;
RES[-1237619061] = 20;
RES[1671408748] = 4;
RES[-1097469014] = 20;
RES[-1351505341] = 20;
RES[968921369] = 3;
RES[451519835] = 0;
RES[718340073] = 11;
RES[609087741] = 5;
RES[-846205264] = 11;
RES[-2101753162] = 0;
RES[70014351] = 12;
RES[385110293] = 11;
RES[2085308727] = 5;
RES[1988912954] = 10;
RES[-451145741] = 8;
RES[908107342] = 6;
RES[-1922172659] = 3;
RES[1000888201] = 6;
RES[-1653016037] = 6;
RES[-1071467560] = 20;
RES[-467782374] = 2;
RES[-1880238501] = 7;
RES[-1902339436] = 3;
RES[-1358224682] = 7;
RES[209662440] = 4;
RES[-1676218689] = 7;
RES[-2146899069] = 6;
RES[1802775474] = 0;
RES[-1934779904] = 8;
RES[1674854189] = 16;
RES[505619372] = 0;
RES[1042366686] = 6;
RES[1387772435] = 11;
RES[1096773442] = 12;
RES[805907956] = 4;
RES[-1508674159] = 11;
RES[1353899522] = 13;
RES[483847181] = 3;
RES[-1478306571] = 0;
RES[-165821310] = 13;
RES[976566701] = 9;
RES[2055588240] = 9;
}

int main()
{
#ifdef HP
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif

	int testCnt;
	assert(scanf("%d", &testCnt) == 1);

	precalc();

	forn(test, testCnt)
	{
	    assert(read());
    	solve(test);
	}

    return 0;
}

