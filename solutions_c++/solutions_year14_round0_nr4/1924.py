#include "cstdio"
#include "algorithm"
using namespace std;
long double tab1[1005],tab2[1005];
int t,n,w1,w2,x;
bool cmp (long double a, long double b)
{
	if (a>b) return true;
	else return false;
}
int main()
{
	scanf ("%d", &t);
	for (int i=0; i<t; i++)
	{
		scanf ("%d", &n);
		for (int j=0; j<n; j++) scanf ("%Lf", &tab1[j]);
		for (int j=0; j<n; j++) scanf ("%Lf", &tab2[j]);
		sort (tab1,tab1+n,cmp);
		sort (tab2,tab2+n,cmp);
		
		w1=0,x=0;
		for (int j=0; j<n; j++)
		{
			if (tab1[j]>tab2[x]) w1++,x++;
			else x++,j--;
			
			if (x==n) break;
		}
		
		w2=0,x=0;
		for (int j=0; j<n; j++)
		{
			if (tab1[j]>tab2[x]) w2++;
			else x++;
			
			if (x==n) break;
		}
		
		printf ("Case #%d: %d %d\n", i+1, w1, w2);
	}
	
	
	return 0;
}