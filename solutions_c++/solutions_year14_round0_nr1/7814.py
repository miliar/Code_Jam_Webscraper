#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <climits>
#include <vector>
#include <list>
#include <cmath>
#include <sstream>
#include <algorithm>
#include <set>
#include <map>
#include <cassert>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;

template<typename T1, typename T2>
ostream &operator << (std::ostream & os,const std::map<T1, T2>& v){
    os << "[";
    for (typename std::map<T1, T2>::const_iterator ii = v.begin(); ii != v.end(); ++ii)
        os << ii->first << ":" << ii->second << " ";
    return os << "]";
}
    
template <class Cntnr>
ostream& c_out(std::ostream& os, const Cntnr& v){
    os << "[";
    for (typename Cntnr::const_iterator ii = v.begin(); ii != v.end(); ++ii)
        os << *ii << " ";
    os << " ]";
    return os;
}
template<typename T>
ostream& operator<<(ostream& o, const vector<T> &c){return c_out(o, c);}
template<typename T>
ostream& operator<<(ostream& o, const list<T> &c){return c_out(o, c);}
template<typename T>
ostream& operator<<(ostream& o, const set<T> &c){return c_out(o, c);}

#define sz(a)                       ((int)(a.size()))
#define forall(i,a,b)               for(int i=(a);i<(int)(b);i++)
#define tr(it, c)                   for( __typeof__( (c).begin()) it = (c).begin();  it != (c).end(); ++it)
#define fill(a,v)                   memset(a, v, sizeof a)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( std::find(a.begin(), a.end(), b) != (a).end())
#define bitcount                    __builtin_popcount
#define D(var)                      cout<< #var" : " << var << "\n";
#define oo                          (int)1e9
#define EPS                         1e-9
#define S(n)                        scanf("%d",&n)
#define INITFROMARR(arr)            (arr, arr + sizeof(arr)/sizeof(arr[0]))
#define gcd                         __gcd

int A[4][4], B[4][4];

int main(){
    int t;
    S(t);
    forall(cs, 1, t+1){
        int r1, r2, cnt = 0, ans;
        S(r1);
        forall(i, 0, 4)
            forall(j, 0, 4)
                S(A[i][j]);
        S(r2);
        forall(i, 0, 4)
            forall(j, 0, 4)
                S(B[i][j]);
        forall(i, 0, 4)
            forall(j, 0, 4)
                if(B[r2-1][i] == A[r1-1][j]){
                    cnt++;
                    ans = B[r2-1][i];
                }
        cout << "Case #" << cs << ": ";
        if(cnt == 1)
            cout << ans << endl;
        else
            cout << ((cnt==0)?"Volunteer cheated!":"Bad magician!") << endl;
    }
    return 0;
}
