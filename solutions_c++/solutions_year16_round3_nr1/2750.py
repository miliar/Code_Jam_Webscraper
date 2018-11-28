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
int ar[30];
int main()
{
   //freopen("in.txt", "r", stdin);
   //freopen("out.txt", "w", stdout);
   int t;
   int cnt = 1;
   scanf("%d", &t);
   while(t--)
   {
	   int n;
	   scanf("%d", &n);
	   for(int i = 0; i < n; i++) 
	   {
		   scanf("%d", &ar[i]);
	   }
	   printf("Case #%d: ", cnt);
	   while(true)
	   {
		   int r = ar[0];
		   int mx = 0;
		   for(int i = 1; i < n; i++)
		   {
			   r += ar[i];
			   if(ar[i] > ar[mx]) mx = i;
		   }
		   int mx2 = -1;
		   for(int i = 0; i < n; i++)
		   {
			   if(i == mx) continue;
			   if(mx2 == -1 || ar[i] > ar[mx2]) mx2 = i;
		   }
		   if(r > 2)
		   {
			   if(ar[mx] == ar[mx2] && r > 3)
			   {
				   ar[mx]--;
				   ar[mx2]--;
				   printf("%c%c ", 'A' + mx,  'A' + mx2);
			   }
			   else
			   {
				   ar[mx]--;
				   printf("%c ", 'A' + mx);
			   }
		   }
		   else 
		   {
			   for(int i = 0; i < n; i++) if(ar[i] == 1) printf("%c", 'A' + i);
			   printf("\n");
			   break;
		   }
	   }
	   cnt++;
   }
   return 0;
}
