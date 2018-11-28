/*
 * brief:
 *
 * qointe, 2014-04-12, qointe@yahoo.in
 */
#include<iostream>
#include<string>
#include<algorithm>
#include<fstream>
#include<map>
#include<stack>
#include<list>
#include<set>
#include<vector>
#include<queue>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<cmath>
using namespace std;

#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)

#define INF                         (int)1e9
#define EPS                         1e-9

#define bitcount                    __buitlin_popcount
#define gcd                         __gcd

#define forall(i,a,b)               for(int i=a;i<b; i++)
#define forallr(j,a,b)              for(int j=a;j>=b;j--)
#define foreach(v, c)               for(typeof((c).begin()) v = (c).begin(); v!=(c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ((b).find(a) != (b).end())
#define pb                          push_back
#define fill                        memset(a,v,sizeof a)
#define sz                          ((int)(a.size()))
#define mp                          make_pair
#define fi                          first
#define se                          second

#define maX(a,b)                    ((a)>(b)?(a):(b))
#define miN(a,b)                    ((a)<(b)?(a):(b))
#define checkbit(n,b)               ((n>>b)&1)
#define DREP(a)                     sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)              (lower_cound(all(arr),ind)-arr.begin())

#ifdef DEBUG
#define debug(args...)              {dbg,args;cerr<<endl;}
#else
#define debug(args...)              // Just strip off all debug tokens
#endif

struct debugger { template<typename T> debugger& operator , (const T& v) { cerr<<v<<" "; return *this; } } dgb;
template <typename T1, typename T2> inline std::ostream& operator << (std::ostream& os, const std::pair<T1, T2>& p) { return os << "(" << p.first << ", " << p.second << ")"; }
template <typename T> inline std::ostream& operator << (std::ostream& os, const std::vector<T>& v) { bool first = true; os << "["; for(unsigned int i=0; i<v.size(); i++) { if(!first) os << ", "; os << v[i]; first = false; } return os << "]"; }
template <typename T> inline std::ostream& operator << (std::ostream& os, const std::set<T>& v) { bool first = true; os << "["; for(typename std::set<T>::const_iterator ii=v.begin(); ii!=v.end(); ++ii) { if(!first) os << ", "; os << *ii; first = false; } return os << "]"; }
template <typename T1, typename T2> inline std::ostream& operator << (std::ostream& os, const std::map<T1, T2>& v) { bool first = true; os << "["; for(typename std::map<T1, T2>::const_iterator ii=v.begin(); ii!=v.end(); ++ii) { if(!first) os << ", "; os << *ii; first = false; } return os << "]"; }
template<class T> void isort(T a[], int len, bool INC) { // If INC set, sort in increasing order // else in decreasing order.
    forall(i, 1, len) forallr(j, i-1, 0) if((INC && (a[j+1] < a[j])) || (!INC && (a[j+1] > a[j]))) swap(&a[j+1], &a[j]); return; }
template<class T> void readArr(T a[], int len) { forall(i, 0, len) cin >> a[i]; return; }
template<class T> void printArr(T a[], int len) { forall(i, 0, len) cout << a[i] << " "; cout << endl; return; }
template<class T> vector<T> slice(vector<T> v, int i, int j) { vector<T> b; forall(k, i, j) b.pb(v[k]); return b; }
template<class T> T* slice(T a[], int i, int j) { int size = j - i; T b[size]; forall(k, i, j) b[k-i] = a[k]; return b; }

int main()
{
    ifstream fin ("A-small-attempt2.in");
    //ofstream fout ("asmall.out");
    int times;
    fin >> times;
    forall(i, 1, times+1) {
        int r1, r2, t;
        vector<int> a1, a2;
        fin >> r1; forall(j, 0, 16) { fin >> t; a1.pb(t); }
        fin >> r2; forall(j, 0, 16) { fin >> t; a2.pb(t); }
        int count = 0, x;
        forall(j, (r1-1)*4, (r1-1)*4+4)
            forall(k, (r2-1)*4, (r2-1)*4+4)
                if(a1[j] == a2[k]) { x=a1[j]; count++; }
        cout << "Case #" << i << ": ";
        if(count > 1)
            cout << "Bad magician!" << endl;
        else if(count < 1)
            cout << "Volunteer cheated!" << endl;
        else
            cout << x << endl;
    }
    return 0;
}
