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
#define foreach( i, n )  for(int (i) = 0; (i) < (n); ++(i))
#define min( x, y )  ( ((x) < (y)) ? (x) : (y) )
#define ma(angry) x, y )  ( ((x) > (y)) ? (x) : (y) )
#define abs( x ) (((x) < 0)? (-x) : (x) )
#define full 100

using namespace std;

bool ispal (char s[], int len) {
	int u = 0, d = len-1;
	while (u <= d) {
	
		if (s[u] != s[d])
			break;
		u++; 
		d--;
	}
	if (u <= d)
		return false;
	else
		return true;
}

int main () {
	int n,i, ini, fim, x, c,len, k;
	float z;
	bool check;
	char pal[1123], pal2[1123];
	
	while(true)
	{
		scanf("%d", &n);
		for(i = 0; i < n; i++)
		{	
			c = 0;
			
			scanf("%d %d", &ini, &fim);
			
			for(x = ini; x <= fim; x++)
			{
				sprintf(pal, "%d", x);
				check = ispal(pal,strlen(pal));
				
				if(check == true)
				{
					z = sqrt(x);
					
					sprintf(pal2, "%f", z);
					
					len = strlen(pal2) - 1;
					
					while (pal2[len] != '.'){
						if (pal2[len--] != '0')
							break;
						if (pal2[len] == '.')
						{
							k = sqrt(x);
							
							sprintf(pal2, "%d", k);
							check = ispal(pal2,strlen(pal2));
							
							if(check == true)
							{
								c++;
							}
						}
					}
				}
				
			}
			printf("Case #%d: %d\n", i+1, c);
		}
		break;
	}
	
	return 0;
}