#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <set>
#include <stack>
#include <deque>
#include <queue>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <iomanip>
#include <climits>
#include <cfloat>
#include <cstdio>
#define x first
#define y second
#define IN(x, n) (0 <= (x) && (x) < n)
#define MAX 10010
#define MOD 1000000007
using namespace std;

typedef long long int entero;
typedef pair<int, int> Point;

int vec8[8][2] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};// signo x+
int vec4[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};//signo +

string int_to_string(int n, int base = 10){
	string s = "";
	do{
		s += char((n%base)+'0');
		n /= base;
	}while(n > 0);
	reverse(s.begin(), s.end());
	return s;
}

int gcd(int uno, int dos)/*calculo el maximo comun divisor*/
{
	if(dos == 0)
		return uno;
	return gcd(dos, uno%dos);/*si este es uno los numeros solo tienen a 1 como maximo comun divisor*/
}

int mcm(int x, int y)/*minimo comun multiplo*/
{
   return (x/gcd(x,y))*y;/*es mejor primero dividir para no desbordar*/
}

int Orientacion(Point p, Point q, Point r){
	//devuelve negativo si la orientacion es en el sentido de las manecillas del reloj es decir negativa
    return (q.x*r.y + r.x*p.y + p.x*q.y) - (q.x*p.y + r.x*q.y + p.x*r.y);
}

int v[MAX], used[MAX];

int solve(int n, int cap){
	memset(used, 0, sizeof(used));
	int cont = 0, i, j;
	for(i = n-1; i >= 0; i--){
		if(!used[i]){
			for(j = i-1; j >= 0; j--){
				if(!used[j]){
					if((v[i]+v[j]) <= cap){
						used[i] = used[j] = 1;
						break;
					}
				}
			}
			if(j < 0){
				used[i] = 1;
			}
			cont++;
		}
	}
	return cont;
}

int main(){
	int i, j, n, k, casos, maximo;
	scanf("%d", &casos);
	for(i = 1; i <= casos; i++){
		scanf("%d%d", &n, &maximo);
		for(j = 0; j < n; j++){
			scanf("%d", &v[j]);
		}
		sort(v, v+n);
		printf("Case #%d: %d\n", i, solve(n, maximo));
	}
	return 0;
}
