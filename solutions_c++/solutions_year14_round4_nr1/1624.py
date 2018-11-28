#include <bits/stdc++.h>
#define make_it_fast ios_base::sync_with_stdio(0);cin.tie(0);

using namespace std;

const double eps=1e-11;
//const double pi=acos(-1.0);
typedef long long ll;
typedef long long int lli;
typedef unsigned long long ull;
typedef long double ld;

#define ff first
#define ss second
#define pb push_back
#define mkp make_pair
typedef std::pair<int,int> pii ;
typedef std::vector<int> vi ;
#define lpu(i,s,e) for(i=s;i<e;i++)
#define lpd(i,s,e) for(i=s;i>e;i--)
#define lpui(i,s,e) for(i=s;i<=e;i++)
#define lpdi(i,s,e) for(i=s;i>=e;i--)
#define abs(a) (a<0?-(a):a)
#define nl() cout << '\n'
#define nlf() cout << endl

class TimeTracker {
	clock_t start, end;
public:
	TimeTracker() {
		start = clock();
	}
	~TimeTracker() {
		end = clock();
		fprintf(stderr, "%.3lf s\n", (double)(end - start) / CLOCKS_PER_SEC);
	}
};

template <class T> inline void swap(T& a,T &b){ a^=b; b^=a; a^=b; }
template <class T> inline T min(T& a,T &b){ if(a<b) { return a; } else return b; }
template <class T> inline T max(T& a,T &b){ if(a>b) { return a; } else return b; }

# define getcx getchar_unlocked

template <class T>
void inp(T& n)//fast input function
{
	n=0;
	int ch=getcx();
	int sign=1;
	while( ch < '0' || ch > '9' )
		{if(ch=='-')sign=-1; ch=getcx();}
	while( ch >= '0' && ch <= '9' )
		n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
	n=n*sign;
}

template <class T>
void oup(T x)
{
	if(x<0)
	{
		putchar('-');
		x=-x;
	}
	int len=0,data[25];
	while(x)
	{
		data[len++]=x%10;
		x/=10;
	}
	if(!len)
		data[len++]=0;
	while(len--)
		putchar(data[len]+48);
	putchar('\n');
}


int main()
{
	// make_it_fast
	#ifdef LOCAL
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
		TimeTracker trk;
	#endif

	int t,tp; inp(t); int s,i,j,n,x; int a,jt;
	vector<int> v;
	int mrk[10001];
	tp=0;
	while(tp<t){
		inp(n); inp(x); a=0;
		v.clear();
		lpu(i,0,n) mrk[i]=0;
		lpu(i,0,n) {
			inp(s); v.pb(s);
		}
		sort(v.begin(),v.end());
		lpdi(i,v.size()-1,0) {
			if(mrk[i]==1) continue;
			else{
				mrk[i]=1; jt=-1;
				lpu(j,0,i){
					if(v[i]+v[j]<=x && mrk[j]!=1) jt=j;
				}
			}
			// if(mrk[i]==1) cout << "ERROR" << endl;
			// cout << i << ' ' << jt << endl;
			if(jt!=-1) { a++; mrk[jt]=1; }
			else a++;
		}
		tp++;
		cout << "Case #" << tp << ": " << a << endl;
	}
	return 0;
}