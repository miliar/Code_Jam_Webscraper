#include<bits/stdc++.h>
using namespace std;
#define For(i, n) for (i = 0; i < (n); ++i)
#define Forr(i, start, n) for (i = start; i < (n); ++i)
#define Forrr(i, start, n, step) for (i = start; i < (n); i += (step))
#define rFor(i, n) for (i = (n); i >= 0; --i)
#define rForr(i, n, end) for (i = n; i >= (end); --i)
#define rForrr(i, n, end, step) for (i = n; i >= (end); i -= (step))
#define loop(a) for (it = a.begin(); it != a.end(); ++it)
typedef long long ll;
#define mem(a, num) memset(a, num, sizeof(a))
#define cpy(a, b) memcpy(a, b, sizeof(a))
typedef unsigned long long ull;
#define SS(s) scanf("%s", s);
#define SI(a) scanf("%d", &a)
#define SII(a, b) scanf("%d%d", &a, &b)
#define SIII(a, b, c) scanf("%d%d%d", &a, &b, &c)
#define SIIII(a, b, c, d) scanf("%d%d%d%d", &a, &b, &c, &d)
#define SL(a) scanf("%lld", &a)
#define SLL(a, b) scanf("%lld%lld", &a, &b)
#define SLLL(a, b, c) scanf("%lld%lld%lld", &a, &b, &c)
#define SD(a) scanf("%lf", &a)
#define SDD(a, b) scanf("%lf%lf", &a, &b)
#define SDDD(a, b, c) scanf("%lf%lf%lf", &a, &b, &c)
#define SA(a, i, n) For(i, n) scanf("%d", a + i) /// ������չ
#define SAA(a, i, n, j, m) For(i, n) For(j, m) SI(a[i][j])
typedef vector<int>::iterator viter;
#define PI(a) printf("%d\n", a)
#define PII(a, b) printf("%d %d\n", a, b)
#define PIII(a, b, c) printf("%d %d %d\n", a, b, c)
#define PL(a) printf("%lld\n", a)
#define PLL(a, b) printf("%lld %lld\n", a, b)
#define PLLL(a, b, c) printf("%lld %lld %lld\n", a, b, c)
#define PD(a) printf("%f\n", a)
#define PDD(a, b) printf("%f %f\n", a, b)
#define PDDD(a, b, c) printf("%f %f %f\n", a, b, c)
#define PA(a, i, n) For(i, (n) - 1) printf("%d ", a[i]); PI(a[n - 1]) /// ����Ҫ֧��STL���������ͣ��ʲ���+����ʽ����Ҫʱ���ֶ�Forr
#define PAn(a, i, n) For(i, n) PI(a[i])
#define PiA(a, i, n) For(i, n) PII(i, a[i]) /// debug��
#define rPA(a, i, n) rForr(i, n - 1, 1) printf("%d ", a[i]); PI(a[0])
#define rPAn(a, i, n) rFor(i, n - 1) PI(a[i])
#define PB push_back
#define MP make_pair
typedef set<int>::iterator siter;
typedef map<int, int>::iterator miter;
#define sq(x) (x * x)
#define all(a) a.begin(), a.end()
#define Uni(a) a.resize(unique(all(a)) - a.begin())
#define Cnt1(n) (__builtin_popcount(n))
typedef multiset<int>::iterator msiter;
typedef multimap<int, int>::iterator mmter;
#define Acc(a, n) (accumulate(a, a + (n), 0))
#define Min(a, n) (*min_element(a, a + (n)))
#define Max(a, n) (*max_element(a, a + (n)))
#define Minpos(a, n) (min_element(a, a + (n)) - a)
#define Maxpos(a, n) (max_element(a, a + (n)) - a)
#define Lowpos(a, n, x) (lower_bound(a, a + (n), x) - a)
#define Upppos(a, n, x) (upper_bound(a, a + (n), x) - a)
#define BS(a, n, x) binary_search(a, a + (n), x)
#define Range(a, n, x) equal_range(a, a + (n), x)
typedef pair<int, int> p2;
#define Inter(v, a, n, b, m) v.resize(set_intersection(a, a + (n), b, b + (m), v.begin()) - v.begin())
#define SInter(v, a, n, b, m) v.resize((n) + (m)); sort(a, a + (n)); sort(b, b + (m)); Inter(v, a, n, b, m)
#define Union(v, a, n, b, m) v.resize(set_union(a, a + (n), b, b + (m), v.begin()) - v.begin());
#define SUnion(v, a, n, b, m) v.resize((n) + (m)); sort(a, a + (n)); sort(b, b + (m)); Union(v, a, n, b, m)
#define Diff(v, a, n, b, m) v.resize(set_difference(a, a + (n), b, b + (m), v.begin()) - v.begin())
#define SDiff(v, a, n, b, m) v.resize((n) + (m)); sort(a, a + (n)); sort(b, b + (m)); Diff(v, a, n, b, m)
#define Sym(v, a, n, b, m) v.resize(set_symmetric_difference(a, a + (n), b, b + (m) v.begin()) - v.begin())
#define SSym(v, a, n, b, m) v.resize((n) + (m)); sort(a, a + (n)); sort(b, b + (m)); Sym(v, a, n, b, m)
typedef pair<int, pair<int, int> > p3;
#define Fin(f) freopen(f, "r", stdin)
#define Fout(f) freopen(f, "w", stdout)
const int dir[4][2] = {1, 0, 0, 1, -1, 0, 0, -1};
const int inf = 0x3f3f3f3f; /// 1.06e9 (INT_MAXΪ2.147e9)
const double pi = acos(-1.0);
const double eps = 1e-8;
typedef long double ld;
// const int mod = 1000000007; /// 1e9+7
// const double tens[11] = {0.0, 1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9, 1e-10};
// reverse_copy: http://www.cplusplus.com/reference/algorithm/reverse_copy/

///����ʹ�����¼�ӱ����֣�time, write
/// �����gets(s)����WA�Ļ�������SS(s)����
/// ��main()�г�ʼ��STL������������

const int mx = 15;

int n;
string org[mx], fin[mx], tmp[mx];

bool ok(int mask)
{
	int i,j;
	For(i, n) tmp[i]=org[i];
	i=0;
	while(mask)
    {
        if(mask&1)
        {
            For(j,n) tmp[j][i]='0'+(1-(tmp[j][i]&15));
        }
        mask>>=1;
        ++i;
    }
    sort(tmp,tmp+n);
    For(i,n) if(tmp[i]!=fin[i]) return 0;
    return 1;
}

int main()
{
	Fin("A-small-attempt0.in");
	Fout("A-small-attempt0.out");
	int t,cas,l,i,ans;
	SI(t);
	Forr(cas, 1, t + 1)
	{
		SII(n, l);
		For(i, n) cin >> org[i];
		For(i, n) cin >> fin[i];
		sort(fin, fin + n);
		ans = inf;
		For(i, 1 << l) if (ok(i)) ans = min(ans, Cnt1(i));
		printf("Case #%d: ", cas);
		if (ans == inf) puts("NOT POSSIBLE");
		else PI(ans);
	}
	return 0;
}
