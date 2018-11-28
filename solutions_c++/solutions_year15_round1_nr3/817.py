/*
TASK: <Task>
LANG: C++
*/
#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
#define EPS 1e-9
#define ALL(x) (x).begin(),(x).end()
#define mp(x,y) make_pair((x),(y))
#define pb(x) push_back((x))
#define FOR(i,st,ed) for(int (i)=(st);(i)<(ed);(i)++)
typedef pair<int,int> PII;
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
typedef long long LL;
typedef long long CoordType;

// from lib
struct Point {
	CoordType x, y;

	bool operator <(const Point &p) const {
		return x < p.x || (x == p.x && y < p.y);
	}
};

// 2D cross product.
// Return a positive value, if OAB makes a counter-clockwise turn,
// negative for clockwise turn, and zero if the points are collinear.
CoordType cross(const Point &O, const Point &A, const Point &B)
{
	return (A.x - O.x) * (B.y - O.y) - (A.y - O.y) * (B.x - O.x);
}

// Returns a list of points on the convex hull in counter-clockwise order.
// Note: the last point in the returned list is the same as the first one.
vector<Point> convexHull(vector<Point> P)
{
	int n = P.size(), k = 0;
	vector<Point> H(2*n);

	// Sort points lexicographically
	sort(P.begin(), P.end());

	// Build lower hull
	for (int i = 0; i < n; i++) {
		while (k >= 2 && cross(H[k-2], H[k-1], P[i]) < 0) k--;
		H[k++] = P[i];
	}

	// Build upper hull
	for (int i = n-2, t = k+1; i >= 0; i--) {
		while (k >= t && cross(H[k-2], H[k-1], P[i]) < 0) k--;
		H[k++] = P[i];
	}

	H.resize(k);
	return H;
}

int N,M,T;
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen("C-small-attempt0.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
    cin >> T;
    int tt=0;
    while(T--)
    {
        cin >> N;
        vector<Point> a(N),b,c;
        for(i=0;i<N;i++)
        {
            cin >> j >> k;
            a[i].x=j;
            a[i].y=k;
        }
//        c=convexHull(a);
//        printf("---\n");
//        for(i=0;i<c.size();i++)
//            printf("%I64d %I64d\n",c[i].x,c[i].y);
//        printf("---\n");
        tt++;
        printf("Case #%d:\n",tt);
        int x,y,z;
        for(i=0;i<N;i++)
        {
            int Mc=22,temp;
            for(j=0;j<(1<<N);j++)
            {
                z=N-__builtin_popcount(j);
                b.resize(z);

                k=0;
                for(y=0;y<N;y++)
                {
                    if(j&(1<<y))
                        continue;

                    b[k].x=a[y].x;
                    b[k].y=a[y].y;

                    k++;
                }

                c=convexHull(b);
                bool ok=false;
                for(k=0;k<c.size();k++)
                {
                    if(c[k].x==a[i].x && c[k].y==a[i].y)
                    {
                        ok=true;
                        break;
                    }
                }
                if(ok)
                {
//                    if(Mc>__builtin_popcount(j))
//                        temp=j;
                    Mc=min(Mc,__builtin_popcount(j));
                }
            }
            printf("%d\n",Mc);
        }
    }
}
