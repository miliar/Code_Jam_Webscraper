#include <bits/stdc++.h>
#include <cassert>
#include <climits>
#include <cfloat>
#include <prettyprint98>

using namespace std;

#define _ std::ios_base::Init i; std::ios_base::sync_with_stdio(0); std::cin.tie(0);

typedef long long LL;
typedef unsigned long long ULL;

/*
srand((unsigned)time(NULL));
inline unsigned int rand16(){return ((rand()) << 15) ^ rand();}
inline unsigned int rand32(){return (rand16() << 16) | rand16();}
inline ULL rand64(){return ((LL)rand32() << 32) | rand32();}
inline ULL random(LL l, LL r){return l == r ? l : rand64() % (r - l) + l;}
*/

const int INF = 0x3f3f3f3f;
const LL INFF = 1LL << 60;
const double EPS = 1e-9;
const double PI = acos(-1.0); //2*acos(0.0); //M_PI;

//4 dirs: int dx[]={1,0,-1,0}, dy[]={0,1,0,-1};
//8 dirs: int dx[]={1,1,0,-1,-1,-1,0,1}, dy[]={0,1,1,1,0,-1,-1,-1};
//hex: int dx[6]={2,1,-1,-2,-1,1}, dy[6]={0,1,1,0,-1,-1};
//knight: int dx[]={2,1,-1,-2,-2,-1,1,2}, dy[]={1,2,2,1,-1,-2,-2,-1};

#define FOR(i,a,b)   for(int(i)=int(a);(i)<int(b);(i)++)
#define FOREQ(i,a,b) for(int(i)=int(a);(i)<=int(b);(i)++)
#define RFOR(i,a,b)  for(int(i)=(a),_b(b);(i)>=_b;--(i))
#define FOREACH(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

#define FILL(arr,val) memset((arr),(val),sizeof(arr))
#define CLR(a)        memset((a),0,sizeof(a))
#define CPY(dest,src) memcpy((dest),(src),sizeof(dest))

#define ALL(a)       (a).begin(),(a).end()
#define SZ(a)        ((int)(a).size())
#define UNIQ(a)      sort(ALL(a)); (a).erase(unique(ALL(a)),(a).end())
#define IDX(arr,ind) (lower_bound(ALL(arr),ind)-arr.begin())

#define fst first
#define snd second
#define pb  push_back
#define mp  make_pair

template< typename T, size_t N >
inline void print_ary(T(&ary)[N], int er)
	{for(int r = 0; r < er; r++) {cout << ary[r] << " ";}cout<<endl;}
template< typename T, size_t N >
inline void print_ary_eq(T(&ary)[N], int er)
	{for(int r = 1; r <= er; r++) {cout << ary[r] << " ";}cout<<endl;}
template< typename T, size_t N, size_t M >
inline void print_ary_2d(T(&ary)[N][M], int er, int ec)
	{for(int r = 0; r < er; r++) {for(int c = 0; c < ec; c++) {cout << ary[r][c] << " ";}cout<<endl;}}
template< typename T, size_t N, size_t M >
inline void print_ary_2d_eq(T(&ary)[N][M], int er, int ec)
	{for(int r = 1; r <= er; r++) {for(int c = 1; c <= ec; c++) {cout << ary[r][c] << " ";}cout<<endl;}}
inline LL lcm(LL a, LL b)
	{return a*b/__gcd(a,b);}
inline double dist(double x1, double y1, double x2, double y2)
	{return hypot(x1-x2,y1-y2);}

int cnt[105][105] = {0};

int main()
{//_
	int T; cin >> T;
	FOREQ(t,1,T)
	{
		vector<string> as;
		int N; cin >> N;
		FOR(i,0,N)
		{
			string a; cin >> a;
			as.pb(a);
		}
		FOR(i,0,N) FOR(j,0,105) cnt[i][j] = 0;
		string c;
		bool first = false;
		bool possible = true;
		int idx = 0;
		FOREACH(as, itr)
		{
			int idxc = 0;
			string cc;

			cc += (*itr)[0];
			cnt[idx][idxc] = 1;

			int len = SZ(*itr);
			FOR(i,1,len)
			{
				if ((*itr)[i] != (*itr)[i-1])
				{
					cc += (*itr)[i];
					idxc++;
					cnt[idx][idxc] = 1;
				}
				else
				{
					cnt[idx][idxc]++;
				}
			}
			if (!first)
			{
				c = cc;
				first = true;
			} else {
				if (cc != c)
				{
					possible = false;
					break;
				}
			}
			idx++;
		}

		if (!possible)
		{
			cout << "Case #" << t << ": Fegla Won" << endl;
		}
		else
		{
			int ans = 0;
			int len = SZ(c);
			//FOR(i,0,N) {FOR(j,0,len) {cout<<cnt[i][j]<<" ";} cout<<endl;}
			FOR(i,0,len)
			{
				int mean = 0;
				FOR(j,0,N)
				{
					mean += cnt[j][i];
				}
				//cout << "total = " << mean << "; N = " << N << endl;
				mean = (mean+(N/2))/N;
				//mean = round(mean/double(N));
				//cout << "mean = " << mean << endl;
				FOR(j,0,N) {
					ans += abs(cnt[j][i] - mean);
				}
			}
/*
				int aa = 0, last = -1, minn = INT_MAX;
				bool all_same = true;
				FOR(j,0,len) {
					printf("%d ", cnt[i][j]);
					aa += cnt[i][j];
					if (last == -1) last = cnt[i][j];
					else { if (last != cnt[i][j]) {
						all_same = false;
					}}
					minn = min(minn, cnt[i][j]);
				}
				printf("\n");
				if (!all_same) ans += (aa-N*minn)/N;
*/
			cout << "Case #" << t << ": " << ans << endl;
		}
		//printf("Case #%d: \n", t);
	}
	return 0;
}
