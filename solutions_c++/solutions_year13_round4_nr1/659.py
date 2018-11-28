#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <cstring>
#include <complex>
#include <assert.h>
#include <sstream>
#include <map>
#include <omp.h>

using namespace std;

typedef vector<int> vi;
typedef long long ll;
typedef long long i64;
typedef pair<int, int> pi;

#define SQR(A) ((A) * (A))
#define CUBE(A) ((A) * (A) * (A))
#define MIN(A,B) ((A) < (B) ? (A) : (B))
#define MAX(A,B) ((A) > (B) ? (A) : (B))

template <class T>
string cout_str(T data)
{
  stringstream buf;
  buf << data;
  return buf.str();
}

int consonant (char ch)
{
  if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
    return 0;
  else
    return 1;
}

class solver
{
 public:
  long long res;
  long long MOD;
  int n, m;
  vi o, e, p;
  
  void read_data ()
  {
    MOD = 1000002013;
    cin >> n >> m;
    o.resize (m);
    e.resize (m);
    p.resize (m);
    for (int i = 0; i < m; ++i)
      cin >> o[i] >> e[i] >> p[i];
  }
  int solve ()
  {
    vector<pair<int, int> > q;
    long long real_sum = 0;
    long long len = 0;
    for (int i = 0; i < m; ++i)
    {
      q.push_back (make_pair (o[i], -p[i]));
      q.push_back (make_pair (e[i], p[i]));
      len = e[i] - o[i];
      long long cost = (len * n - len * (len - 1) / 2) % MOD;
      real_sum += (long long) p[i] * cost;
      real_sum  = real_sum % MOD;
    }
    sort (q.begin (), q.end ());
    long long sum = 0;
    for (int i = 0; i < q.size (); ++i)
      if (q[i].second > 0)
      {
        for (int j = i - 1; j >= 0; --j)
          if (q[j].second < 0)
          {
            long long size = min (q[i].second, -q[j].second);
            q[i].second -= size;
            q[j].second += size;
            len = q[i].first - q[j].first;
            long long cost = (len * n - len * (len - 1) / 2) % MOD;
            sum += size * cost;
            sum  = sum % MOD;
            if (q[i].second == 0)
              break;
          }
      }
    res = (real_sum - sum + 2 * MOD) % MOD;
    return 0;
  }
  void write_res (int id) {cout << "Case #" << id + 1 << ": " << res << endl;}
};

int main ()
{
#ifdef _WIN32
  freopen ("../data.in", "r", stdin);
  freopen ("../output.txt", "w", stdout);
#else
  freopen ("data.in", "r", stdin);
  freopen ("output.txt", "w", stdout);
#endif

  string case_str;
  getline (cin, case_str);
  int cases = atoi (case_str.c_str ());
  vector<solver> tasks (cases);

  for (int id = 0; id < cases; ++id)
    tasks[id].read_data ();
  
  //#pragma omp parallel for
  for (int id = 0; id < cases; ++id)
    if (tasks[id].solve () < 0)
      std::cerr << "BAD CASE: " << id + 1 << endl;

  for (int id = 0; id < cases; ++id)
    tasks[id].write_res (id);
  
  return 0;
}
