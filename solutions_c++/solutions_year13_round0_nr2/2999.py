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

int main () {
	int n, x, y, tab[200][200], val;
	scanf("%d", &n);
	bool erro, top, left;
	foreach (o, n) {
		scanf("%d %d", &x, &y);
		foreach (i, x) {
			foreach (j, y) {
				scanf("%d", &tab[i][j]);
			}
		}
		erro = false;
		for (int i = 0; i < x; i++) {
			for (int j = 0; j < y; j++) {
				top = left = false;
				for (int k = 0; k < x; k++)
					if (tab[i][j] < tab[k][j])
						top = true;
				for (int k = 0; k < y; k++)
					if (tab[i][j] < tab[i][k])
						left = true;
				if (top && left)
				{
					erro = true;
					goto saida;
				}
			}
		}
		saida:
		if (erro)
			printf("Case #%d: NO\n", o+1);
		else
			printf("Case #%d: YES\n", o+1);
	}
	return 0;
}


