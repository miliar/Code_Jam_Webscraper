#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef pair<ii, int> iii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<int, int> mii;
typedef map<string, int> msi;

#define FOR(i, a, b) \
for (int i = int(a); i <= int(b); i++) // a to b, and variable i is local!
#define FORD(i, a, b) \
for (int i = int(a); i >= int(b); i--) // a to b, and variable i is local!
#define TRvi(c, it) \
for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) \
for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) \
for (msi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmii(c, it) \
for (mii::iterator it = (c).begin(); it != (c).end(); it++)
#define INF 2000000000
#define MEMSET_INF 127
#define MEMSET_HALF_INF 63
#define zero(arr) memset((arr), 0, sizeof (arr))
#define init(arr) memset((arr), -1, sizeof (arr))
#define ff first
#define ss second
#define pb push_back
#define LSOne(S) (S & (-S))

//memset(dist, MEMSET_INF, sizeof dist);
//memset(dp_memo, -1, sizeof dp_memo);
//memset(arr, 0, sizeof arr);

class UnionFind {
	private: vi p, rank;
	public:
		UnionFind(int N) {
			rank.assign(N,0);
			p.assign(N,0);
			for (int i=0;i<N;i++) {
				p[i]=i;
			}
		}
		int findSet(int i) {
			return (p[i]==i) ? i : (p[i]=findSet(p[i]));
		}
		bool isSameSet(int i, int j) {
			return findSet(i)==findSet(j);
		}
		void unionSet(int i, int j) {
			if (!isSameSet(i,j)) {
				int x = findSet(i), y = findSet(j);
				if (rank[x] > rank[y])
					p[y]=x;
				else {
					p[x]=y;
					if (rank[x]==rank[y])
						rank[y]++;
				}
			}
		}
};

class SegmentTree {         
private:
  vi st, A;
  int n;
  int left (int p) { return p << 1; }     
  int right(int p) { return (p << 1) + 1; }

  void build(int p, int L, int R) {                         
    if (L == R)                            
      st[p] = L;                                         
    else {
      build(left(p) , L              , (L + R) / 2);
      build(right(p), (L + R) / 2 + 1, R          );
      int p1 = st[left(p)], p2 = st[right(p)];
      st[p] = (A[p1] <= A[p2]) ? p1 : p2;
  } }

  int rmq(int p, int L, int R, int i, int j) {                  
    if (i >  R || j <  L) return -1; 
    if (L >= i && R <= j) return st[p];              

     
    int p1 = rmq(left(p) , L              , (L+R) / 2, i, j);
    int p2 = rmq(right(p), (L+R) / 2 + 1, R          , i, j);

    if (p1 == -1) return p2;   
    if (p2 == -1) return p1;                              
    return (A[p1] <= A[p2]) ? p1 : p2; }          

  int update_point(int p, int L, int R, int idx, int new_value) {
    int i = idx, j = idx;

    if (i > R || j < L)
      return st[p];

    if (L == i && R == j) {
      A[i] = new_value; 
      return st[p] = L; 
    }

    int p1, p2;
    p1 = update_point(left(p) , L              , (L + R) / 2, idx, new_value);
    p2 = update_point(right(p), (L + R) / 2 + 1, R          , idx, new_value);

    return st[p] = (A[p1] <= A[p2]) ? p1 : p2;
  }

public:
  SegmentTree(const vi &_A) {
    A = _A; n = (int)A.size();              
    st.assign(4 * n, 0);            
    build(1, 0, n - 1);                                 
  }

  int rmq(int i, int j) { return rmq(1, 0, n - 1, i, j); }  

  int update_point(int idx, int new_value) {
    return update_point(1, 0, n - 1, idx, new_value); }
};

class FenwickTree {
	private:
		vi ft;
	public:
		FenwickTree(int n) {
			ft.assign(n+1, 0);
		}
		int rsq(int b) {
			int sum = 0;
			for (; b; b -= LSOne(b))
				sum += ft[b];
			return sum;
		}
		void adjust(int k, int v) {
			for (; k < (int)ft.size(); k += LSOne(k)) {
				ft[k] += v;
			}
		}
};

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	
	int n;
	
	cin>>n;
	
	FOR(i, 1, n) {
		ll a;
		cin>>a;
		if(a == 0) {
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;	
			continue;
		}
		
		ll bit = 0;		
		ll mul = 2;
		ll b = a;
		while(1) {
			ll tmp = b;
			ll chk = 0;
			while(tmp>0) {
				bit |= 1LL<<(tmp%10);
				tmp/=10;
				if(bit == (1LL<<10)-1) {
					chk = 1;
					break;
				}
			}
			if(chk)
				break;
			b = a*mul;
			mul++;
		}
		
		cout<<"Case #"<<i<<": "<<b<<endl;
		
	}
	return 0;
}



