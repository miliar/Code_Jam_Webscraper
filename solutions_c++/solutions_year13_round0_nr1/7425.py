
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
	int n, i, x, y, l[4],c[4], d1, d2, p;
	char w[4][4];
	
	scanf("%d", &n);
	for(i = 0; i<n; i++){
		for(x=0;x<4;x++){
			l[x] = 0;
			c[x] = 0;
		}
		p = d1 = d2 = 0;
				
		for(x = 0; x<4; x++){
			for(y = 0; y < 4; y++){
				scanf(" %c", &w[x][y]);
				if(w[x][y] == '.'){
					p++;
					l[x] += 100;
					c[y] += 100;
				}
			}
		}
		/*Inicio do teste*/
		for(x = 0; x<4; x++){
			for(y = 0; y < 4; y++){
				if(w[x][y] != '.'){
					if(w[x][y] == 'X'){
						l[x] += 10;
						c[y] += 10;
					}else
						if(w[x][y] == 'O'){
							l[x] += 2;
							c[y] += 2;
						}
				}
				if(x == y){
					if(w[x][y] == 'X')
						d2 += 10;
					else
						if(w[x][y] == 'O')
							d2 += 2;
						else
							if(w[x][y] == '.')
								d2 += 100;
				}
			}
		}
		/*Verificando diagonal  inversa*/
		if(w[3][0] == 'X')
			d1 += 10;
		else
			if(w[3][0] == 'O')
				d1 += 2;
			else
				if(w[3][0] == '.')
					d1 += 100;

		if(w[2][1] == 'X')
			d1 += 10;
		else
			if(w[2][1] == 'O')
				d1 += 2;
			else
				if(w[2][1] == '.')
					d1+= 100;
		if(w[1][2] == 'X')
			d1 += 10;
		else
			if(w[1][2] == 'O')
				d1 += 2;
			else
				if(w[1][2] == '.')
					d1+= 100;
		if(w[0][3] == 'X')
			d1 += 10;
		else
			if(w[0][3] == 'O')
				d1 += 2;
			else
				if(w[0][3] == '.')
					d1+= 100;
		if(d1%10 == 0 && d1 < 100)
			printf("Case #%d: X won\n",i+1);
		else
			if(d1%2 == 0 && d1 <= 8)
				printf("Case #%d: O won\n",i+1);
				else
					if(d2%10 == 0 && d2 < 100)
						printf("Case #%d: X won\n",i+1);
					else
						if(d2%2 == 0 && d2 <= 8)
							printf("Case #%d: O won\n",i+1);
						else
							for(x = 0; x<4; x++){		
								if((l[x]%10 == 0 && l[x] < 100) || (c[x]%10 == 0 && c[x] < 100)){
									printf("Case #%d: X won\n",i+1);
									break;
								}
								else{
									if((l[x]%2 == 0 && l[x] <= 8) || (c[x]%2 == 0 && c[x] <= 8)){
										printf("Case #%d: O won\n",i+1);
										break;
									}
									else
										if(p > 0 && x == 3){
											printf("Case #%d: Game has not completed\n",i+1);
											break;
										}
										else
											if(x == 3){
												printf("Case #%d: Draw\n",i+1);	
												break;
											}
								}
							}
	}
	return 0;
}
