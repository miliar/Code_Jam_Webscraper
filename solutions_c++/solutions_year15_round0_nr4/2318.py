#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <cstring>
using namespace std;
int main()
{
   //freopen("in.txt", "r", stdin);
   //freopen("out.txt", "w", stdout);
   int t;
   scanf("%d", &t);
   int c2 = 1;
   while(t--)
   {
	   int x, r, c;
	   scanf("%d %d %d", &x, &r, &c);
	   bool b = true;
	   if(x == 1) b = false;
	   else if(x == 2)
	   {
		   if((r * c) % 2 == 0) b = false;
	   }
	   else if(x == 3)
	   {
		   int mn = min(r, c);
		   int mx = max(r, c);
		   if((mn == 2 && mx == 3) || mn == 3) b = false;
	   }
	   else if(x == 4)
	   {
		   int mn = min(r, c);
		   int mx = max(r, c);
		   if((mn == 3 && mx == 4) || mn == 4) b = false;
	   }
	   if(b) printf("Case #%d: RICHARD\n", c2);
	   else printf("Case #%d: GABRIEL\n", c2);
	   c2++;
   }
   return 0;
}

