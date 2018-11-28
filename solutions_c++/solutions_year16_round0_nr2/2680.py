#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>


#define pii pair <int, int>
#define pll pair <ll, ll>
#define rep(i, n) for (int i = 0; i < (int)n; i++)
#define REP(i, n, m) for (int i = (int)n; i < (int)m; i++)
#define prep(i, n) for (int i = 1; i <= (int)n; i++)
#define per(i, n) for (int i = n; i >= 0; i--)
#define pb push_back
#define vi vector <int>
#define vl vector <ll>
#define fi first
#define se second
#define mp make_pair


typedef long long ll;
typedef long double ld;


using namespace std;


//----------------------- DEBUG

#include <bits/stdc++.h>

#define error(args...) { 	vector<string> _v;                       \
							string _s = #args;                       \
							replace(_s.begin(), _s.end(), ',', ' '); \
							splitstr(_s, _v);                        \
							err(_v.begin(), args);                   \
						}

void splitstr(const string &s, vector<string> &v) {
	istringstream in(s);
	copy(istream_iterator<string>(in), istream_iterator<string>(), back_inserter(v));
}

void err(vector<string>::iterator it) {}
template<typename T, typename... Args>
void err(vector<string>::iterator it, T a, Args... args) {
	cerr << *it << " = " << a << '\n';
	err(++it, args...);
}

/** Read */

inline int readChar();
template <class T = int> inline T readInt();
template <class T> inline void writeInt( T x );
inline void writeChar( int x );
inline void flush();


static const int buf_size = 4096;

inline int getChar() {
  static char buf[buf_size];
  static int len = 0, pos = 0;
  if (pos == len)
    pos = 0, len = fread(buf, 1, buf_size, stdin);
  if (pos == len)
    return -1;
  return buf[pos++];
}

inline int readChar() {
  int c = getChar();
  while (c <= 32)
    c = getChar();
  return c;
}

template <class T>
inline T readInt() {
  int s = 1, c = readChar();
  T x = 0;
  if (c == '-')
    s = -1, c = getChar();
  while ('0' <= c && c <= '9')
    x = x * 10 + c - '0', c = getChar();
  return s == 1 ? x : -x;
}

/** Write */

static int write_pos = 0;
static char write_buf[buf_size];

inline void writeChar( int x ) {
  if (write_pos == buf_size)
    fwrite(write_buf, 1, buf_size, stdout), write_pos = 0;
  write_buf[write_pos++] = x;
}

inline void flush() {
  if (write_pos)
    fwrite(write_buf, 1, write_pos, stdout), write_pos = 0;
}

template <class T>
inline void writeInt( T x ) {
  if (x < 0)
    writeChar('-'), x = -x;

  char s[24];
  int n = 0;
  while (x || !n)
    s[n++] = '0' + x % 10, x /= 10;
  while (n--)
    writeChar(s[n]);
}
// end

struct point {
	int x, y;
	double len() {
		return sqrt(x * x + y * y);
	}

	double angel() {
		return atan2(y, x);
	}

	point operator + (const point &o) {
		return {x + o.x, y + o.y};
	}

	point operator * (const int d) {
		return {x * d, y * d};
	}

	int operator * (const point &o) {
		return x * o.x + y * o.y;
	}

	int operator ^ (const point &o) {
        return x * o.y - y * o.x;
	}
};


//----------------------- const

const int maxn = (1e5) + 100;
const ll INF = (1e9) + 7;
const ld EPS = 1e-8;

//----------------------- main
void print(int t, ll n){
    cout << "Case #" << t << ": " << n << "\n";
    return;
}

int main()
{
    //freopen("B-large.in", "r", stdin);
    //freopen("output.txt", "w", stdout);


  //  cout << fixed << setprecision(15);
	ios_base::sync_with_stdio(0);
	cin.tie(0);

    int t;
    cin >> t;
    prep(i, t){
        string s;
        cin >> s;
        int pans = 0;
        prep(i, (int)s.size() - 1){
            if (s[i] != s[i - 1]){
                pans++;
            }
        }
        if (s[s.size() - 1] == '-')
            print(i, pans + 1);
        else
            print(i, pans);
    }


	return 0;
}
