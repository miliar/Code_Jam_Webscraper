#include <iostream>
#include <algorithm>
using namespace std;

const int MAXN = 1010;

int isCan(int x)
{
	char s[MAXN];
	int top = 0;
	while (x)
	{
		s[top++] = (char)(x % 10 + '0');
		x /= 10;
	}
	
	for (int i = 0, j = top - 1; i <= j; i++, j--)
		if (s[i] != s[j])
			return 0;
	return 1;
}
 
int cal(int a, int b)
{
	int ret = 0;
	for (int i = 1; i * i <= b; i++)
	{
		if (i * i >= a && isCan(i) && isCan(i * i))
		{	
			ret++;
		//	printf ("i=%d i*i=%d\n", i, i*i);
		} 
	}
	return ret;
}

int main()
{
	freopen ("C-small-attempt0.in", "r", stdin);
//	freopen ("A-large.in", "r", stdin); 
 	freopen ("c.out", "w", stdout);
    
	int csnum, cs;
	int a, b;
	scanf ("%d", &csnum);
	for (cs = 1; cs <= csnum; cs++)
	{
		scanf ("%d %d", &a, &b);
		
		printf ("Case #%d: %d\n", cs, cal(a, b));
	}
	
	//while (1);
	return 0;
} 
