#include <cstdio>
#include <iostream>

#include <memory.h>

#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>

#include <algorithm>
#include <functional>

#include <cmath>


using namespace std;
int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }

typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

int main( )
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	
	int n = ni();
	
	for(int i = 0; i < n; ++i)
	{
	   int msl = ni();
	   
	   ns();
	   
	   int ppl = 0;
	   int guests = 0;
	   
	   for(int j = 0; j <= msl; ++j)
	   {
	      char ms[2] = {sbuf[j], 0};
	      
	      int k = atoi(ms);  
	      
	      if(0 == j)
	      {		
		ppl = k;
	      }
	      else
	      {
		if(ppl < j)
		{
		  int inv = (j - ppl);
		  guests += inv;
		  
		  ppl += inv;
		}
		
		if(ppl > 0)
		{
		  ppl += k;
		}
	      }
	   }
	   
	   printf("Case #%d: %d\n", (i+1), guests);
	}


	return 0;
}
