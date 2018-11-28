#include<cstdio>
using namespace std;
char x[1005];
int main()
{
  int z;
  scanf ( "%d", &z );
  for ( int t = 1; t <= z; t ++ )
  {
	int k, ile = 0, ans = 0;
	scanf ( "%d %s", &k, x );
	for ( int i = 0; i <= k; i ++ )
	{
	  int a = x[i] - '0';
	  if ( ile < i ) 
	  {
		int fr = i - ile;
		ans += fr;
		ile += fr;
	  }
	  ile += a;
	}
	printf ( "Case #%d: %d\n", t, ans );
  }
}