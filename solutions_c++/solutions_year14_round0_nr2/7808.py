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

int main(){
    int t;
    S(t);
    forall(cs, 1, t+1){
        double c, f, x, cur = 0, cps = 2, t = 0;//, tn = 0, td = 0;
        cin >> c >> f >> x;
        while(1){
            //D(cur); D(cps); D(t);
            if(cur >= x)
                break;
            if(cur < c){
                double inc = min(x-cur, c-cur);
                t += inc/cps;
                //D(inc/cps);
                cur += inc;
            }
            else{
                double t1 = (x-cur)/cps, t2 = (x-cur+c)/(cps+f);
                if(t2 < t1){ // buy now
                    cur -= c;
                    cps += f;
                    //cout << "Buy at " << t << " " << cps << endl;
                }
                else{
                    t += t1;
                    cur = x;
                    //D(t1);
                }
            }
        }
        cout << "Case #" << cs << ": ";
        printf("%.7lf\n", t);// << endl;
    }
    return 0;
}
