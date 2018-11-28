#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <cstring>
using namespace std;
int res = 9;
int ar[100];
void func(int n, int r)
{
	if(r >= res) return;
	bool b = false;
	for(int i = 0; i < n; i++)
	{
		if(ar[i] > 0) b = true;
		ar[i]--;
	}
	if(!b) 
	{
		res = min(res, r);
		for(int i = 0; i < n; i++) ar[i]++;
		return;
	}
	else func(n, r + 1);
	int mx = -1;
	for(int i = 0; i < n; i++) 
	{
		ar[i]++;
		if(ar[i] > 1 && (mx == - 1 || ar[mx] < ar[i])) mx = i;
	}
	if(mx != -1)
	{
		int t = ar[mx];
		ar[mx]--;
		ar[n] = 1;
		while(ar[mx] >= ar[n])
		{
			func(n+1, r+1);
			ar[mx]--;
			ar[n]++;
		}
		ar[mx] = t;
	}
}
int main()
{
   //freopen("in.txt", "r", stdin);
   //freopen("out.txt", "w", stdout);
   int t;
   scanf("%d", &t);
   int c = 1;
   while(t--)
   {
	   int n;
	   res = 9;
	   scanf("%d", &n);
	   for(int i = 0; i < n; i++) scanf("%d", &ar[i]);
	   func(n, 0);
	   printf("Case #%d: %d\n", c, res);
	   c++;
   }
   return 0;
}

