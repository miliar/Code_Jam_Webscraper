#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <string>
#include <algorithm>
#define infinity 2139062143
#define swap(x, y) (x) ^= (y) ^= (x) ^= (y)
#define foreach( i, n ) 	for(int (i) = 0; (i) < (n); ++(i))
#define min( x, y )  ( ((x) < (y)) ? (x) : (y) )
#define max( x, y )  ( ((x) > (y)) ? (x) : (y) )
#define abs( x ) (((x) < 0)? (-x) : (x) )
#define full 100
using namespace std;

bool ispal (char s[], int len) {
	int u = 0, d = len-1;
	while (u <= d) {
		if (s[u] != s[d])
			break;
		u++; d--;
	}
	if (u <= d)
		return false;
	else
		return true;
}

int main () {
	int n, x, y, len, count = 0;
	double lala;
	bool a, b;
	char pal[50], pal2[50];
	scanf("%d", &n);
	foreach (o, n) {
		scanf("%d %d", &x, &y);
		count = 0;
		for (int i = x; i <= y; i++)
		{	
			a=b=false;
			sprintf(pal, "%d", i);
			a = ispal(pal, strlen(pal));
			
			lala = sqrt(i);
			sprintf(pal2, "%f", lala);
			len = strlen(pal2) - 1;
		//	printf("%s\n", pal2);
			while (pal2[len] != '.')
				if (pal2[len--] != '0')
					break;
			if (pal2[len] == '.')
			{
				pal2[len] = '\0';
				b = ispal(pal2, strlen(pal2));
			}
			if (a && b)
				count++;
		}
		printf("Case #%d: %d\n", o+1, count);
	}
	
	return 0;
}


