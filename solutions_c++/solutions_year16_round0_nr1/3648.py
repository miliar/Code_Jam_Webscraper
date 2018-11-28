#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <cstring>
#include <fstream>
#define ll long long int
using namespace std;
int ar[15];
int main()
{
   //freopen("in.txt", "r", stdin);
   //freopen("out.txt", "w", stdout);
   int t;
   scanf("%d", &t);
   for(int i = 1; i <= t; i++)
   {
	   memset(ar, 0, 10*sizeof(int));
	   ll n;
	   scanf("%I64d", &n);
	   ll a = n;
	   if(n == 0)
	   {
		   printf("Case #%d: INSOMNIA\n", i);
		   continue;
	   }
	   int c = 0;
	   while(c < 10)
	   {
		   ll b = n;
		   while(b != 0)
		   {
			   if(ar[b%10] == 0)
			   {
				   c++;
				   ar[b%10] = 1;
			   }
			   b /= 10;
		   }
		   if(c == 10) break;
		   n += a;
	   }
	   printf("Case #%d: %I64d\n", i, n);
   }
   return 0;
}
