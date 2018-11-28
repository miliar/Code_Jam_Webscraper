#include <cstdio>
#include <map>

using namespace std;
typedef unsigned long long ull;

map<ull, int> count;

bool isPalin(const ull n)
{
  ull m = n;
  ull t = 0;
  while ( m>0 ) {
    t = t*10 + m%10;
    m /= 10;
  }
  return t==n;
}

void prepare()
{
  int curr_count = 0;
  for ( ull root=1; root<=10000000ULL; ++root ) {
    if ( isPalin(root) ) {
      ull square = root*root;
      if ( isPalin(square) ) {
	count[square] = ++curr_count;
      }
    }
  }
}

int getCount(ull x)
{
  if ( count.count(x) )
    return count[x];
  else {
    //printf("  want x  = %llu\n", x);
    map<ull,int>::iterator it = count.lower_bound(x);
    --it;
    //printf("  from x' = %llu\n", it->first);
    return it->second;
  }
}

int solve(const ull &A, const ull &B)
{
  //printf("A=%llu, B=%llu\n", A, B);
  if ( A==1 ) {
    int B_count = getCount(B);
    //printf("B_count = %d\n", B_count);
    return B_count;
  }
  else {
    int A1_count = getCount(A-1);
    int B_count  = getCount(B);
    /*
    printf("A1_count = %d, B_count = %d, diff = %d\n", 
	   A1_count,
	   B_count, 
	   B_count-A1_count);
    */
    return B_count-A1_count;
  }
}

int main()
{
  prepare();

  int T;
  scanf("%d", &T);
  for ( int i=1; i<=T; ++i ) {
    ull A, B;
    scanf("%llu %llu", &A, &B);
    printf("Case #%d: %d\n", i, solve(A,B));
  }
}
