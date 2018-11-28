#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <cstring>
using namespace std;
char buf[1010];
int main()
{
   //freopen("in.txt", "r", stdin);
   //freopen("out.txt", "w", stdout);
   int t;
   scanf("%d", &t);
   int c = 1;
   while(t--)
   {
	   int s;
	   int res = 0;
	   scanf("%d %s\n", &s, buf);
	   int r = buf[0] - '0';
	   for(int i = 1; i <= s; i++)
	   {
		   int a = buf[i] - '0';
		   if(i > r) 
		   {
			   res += i - r;
			   r += i - r;
		   }
		   r += a;
	   }
	   printf("Case #%d: %d\n", c, res);
	   c++;
   }
   return 0;
}

