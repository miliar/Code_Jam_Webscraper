#include <bits/stdc++.h>
using namespace std;

// loop, iteration defines
#define SK(a)           int((a).size())
#define ALL(c)          (c).begin(),(c).end()
#define PRESENT(c,x)    ((c).find(x) != (c).end()) 
#define CPRESENT(c,x)   (find(ALL(c),x) != (c).end()) 
#define FOR(i,a,b)      for(int i = (a); i < (b); ++i)
#define REP(i,a)        FOR(i, 0, (a) - 1)
#define FORD(i,n,a)     for(int (i) = (n); (i) >= a; (i)--)
#define FOREACH(it,c)   for(typeof((c).begin()) it=(c).begin(); it != (c).end(); ++it)
#define FILL(a, v)      memset(a, v, sizeof(a));
#define DREP(a)         sort(ALL(a)); a.erase(unique(ALL(a)), a.end()) // will make the vector unique and sorted order

// Short-hand defines
#define fi    first
#define se    second
#define pb    push_back
#define mp    make_pair
#define endl  '\n'

// Types
typedef long long           ll;
typedef long double         ld;
typedef vector <int>        vi;
typedef vector <ll>         vll;
typedef vector <double>     vd;
typedef vector <string>     vs;
typedef vector <vi>         vvi;
typedef pair <int, int>     pii;
typedef pair <ll, ll>       pll;
typedef vector <pii >       vpii;
 
// Constants
#define PI 3.1415926535897932384626


// Debugger
#define DEBUG(args...) \
  {                    \
    dbg, args;         \
    cerr << endl;      \
  }
struct debugger {
  template <typename T>
  debugger& operator, (const T& v) {
    cerr << v << " ";
    return *this;
  }
} dbg;

// speed up cin (but you couldn't use scanf...)
struct _ {
  ios_base::Init i;
  _() {
  cin.sync_with_stdio(0);
  cin.tie(0);
  }
} _;

// cout to handle pair, vector, set and map
template <typename T1, typename T2>
inline std::ostream& operator<<(std::ostream& os, const std::pair<T1, T2>& p) {
  return os << "(" << p.first << ", " << p.second << ")";
}

template <typename T>
inline std::ostream& operator<<(std::ostream& os, const std::vector<T>& v) {
  bool first = true;
  os << "[";
  for (unsigned int i = 0; i < v.size(); i++) {
    if (!first) os << ", ";
    os << v[i];
    first = false;
  }
  return os << "]";
}

template<typename T>
inline std::ostream &operator << (std::ostream & os,const std::set<T>& v) {
  bool first = true;
  os << "[";
  for (typename std::set<T>::const_iterator ii = v.begin(); ii != v.end(); ++ii) {
    if (!first) os << ", ";
    os << *ii;
    first = false;
  }
  return os << "]";
}

template<typename T1, typename T2>
inline std::ostream &operator << (std::ostream & os,const std::map<T1, T2>& v) {
  bool first = true;
  os << "[";
  for (typename std::map<T1, T2>::const_iterator ii = v.begin(); ii != v.end(); ++ii) {
    if (!first) os << ", ";
    os << *ii ;
    first = false;
  }
  return os << "]";
}

//                                                //
//------------------------------------------------//
//                                                //

class Quaternion {
public:
  Quaternion() : I(0), J(0), K(0), H(0) {};
  Quaternion(int h, int i, int j, int k) : H(h), I(i), J(k), K(k) {};
  Quaternion(char c) {
    switch(c) {
      case '1':
        H=1; I=0; J=0; K=0;
        break;
      case 'i':
        H=0; I=1; J=0; K=0;
        break;
      case 'j':
        H=0; I=0; J=1; K=0;
        break;
      case 'k':
        H=0; I=0; J=0; K=1;
        break;
      default:
        H=0; I=0; J=0; K=0;
    }
  }
  
  int H, I, J, K; // 1, i, j, k order
  
  Quaternion& operator = (const Quaternion& other) {
    I = other.I;
    J = other.J;
    K = other.K;
    H = other.H;
    return *this;
  }

  Quaternion operator * (const Quaternion& other) const {
    Quaternion tmp;

    tmp.H = (other.H * H) - (other.I * I) - (other.J * J) - (other.K * K);
    tmp.I = (other.H * I) + (other.I * H) - (other.J * K) + (other.K * J);
    tmp.J = (other.H * J) + (other.J * H) - (other.K * I) + (other.I * K);
    tmp.K = (other.H * K) + (other.K * H) - (other.I * J) + (other.J * I);

    return tmp;
  }

  Quaternion& operator *= (const Quaternion& other) {
    return (*this = (*this) * other);
  }
};

inline std::ostream& operator<<(std::ostream& os, const Quaternion& q) {
  return os << "(" << q.H << ", " << q.I << ", " << q.J << ", " << q.K << ")" << endl;
}

#define MAX_L (40000)
char in[4*(MAX_L+1)];

int main() {
  int Tmax, T = 0;

  Quaternion H('1');  // 1
  Quaternion I('i');  // i
  Quaternion J('j');  // j
  Quaternion K('k');  // k

  cin >> Tmax;
  while (T < Tmax) {
    ll L, X;
    cin >> L >> X;
    cin.ignore();
    FILL(in, 0);
    cin.getline(in, MAX_L);

    if (X >= 2)
      strncpy(in+L, in, L);
    if (X >= 3)
      strncpy(in+2*L, in, L);
    if (X >= 4)
      strncpy(in+3*L, in, L);

    Quaternion tmp = H;
    Quaternion repetition;
    ll first_i = 9999999998;
    bool has_i = false;
    bool has_k = false;
    ll first_k = 9999999998;
    ll last_k = -9999999998;

    ll i = 0;
    while (in[i] != 0) {
      tmp *= Quaternion(in[i]);

//      cout << tmp;
      if (i == L-1)
        repetition = tmp;
      
      if (tmp.K == 1) {
        last_k = i;
        if (has_k == false) {
          first_k = i;
          has_k = true;
        }
      }
      if (has_i == false && tmp.I == 1) {
        first_i = i;
        has_i = true;
      }

      ++i;
    }

    // Calculate last entry
    tmp = H;
    for (int i = 0; i < (X % 4); ++i) {
      tmp *= repetition;
    }

    //cout << "END\n" << repetition << tmp;
    //cout << first_i << ", " << first_k << ", " << last_k << endl;

    if ((tmp.H == -1 && has_i && has_k) && (first_i < last_k || (4 + first_k/(double) L) < X))
      cout << "Case #" << ++T << ": YES" << endl;
    else
      cout << "Case #" << ++T << ": NO" << endl;
  }

  return 0;
}