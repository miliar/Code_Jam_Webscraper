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
  long long n, p;
  long long y, z;
  
  void read_data ()
  {
    cin >> n >> p;
  }

  int solve ()
  {
    long long max_place = 0;
    long long k = 0;

    if (p == (1<<n))
      y = (1<<n) - 1;
    else
      {
        vi bin_arr;
        long long pp = p - 1;
        for (int i = 0; i < n; ++i)
        {
          bin_arr.push_back (pp % 2);
          pp /= 2;
        }
        reverse (bin_arr.begin (), bin_arr.end ());
        
        
        for (int i = 0; i < n && bin_arr[i] == 1; ++i)
         k++;

        y = (1<<(k+1)) - 2;
      }
    long long min_place = 1<<n;
    k = 1;
    while (min_place > p)
    {
      min_place -= 1<<(n - k); 
      k++;
    }
    
    z = (1<<n) - (1<<(k - 1));
    return 0;
  }
  void write_res (int id) {cout << "Case #" << id + 1 << ": " << y << " " << z << endl;}
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
