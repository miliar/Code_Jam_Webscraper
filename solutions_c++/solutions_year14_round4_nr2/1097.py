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

vector<int> v;
queue<pair<vector<int>, int> > q;
set<vector<int> > vis;

bool solution(vector<int> aux){
	int i, j, k;
	for(k = 0; k < aux.size(); k++){
		for(i = k-1; i >= 0 && aux[i+1] > aux[i]; i--);
		if(i >= 0)
			continue;
		for(i = k+1; i < aux.size() && aux[i-1] > aux[i]; i++);
		if(i < aux.size())
			continue;
		break;
	}
	if(k == aux.size())
		return false;
	return true;
}

void imprimir(vector<int> v){
	int i;
	for(i = 0; i < v.size(); i++)
		printf("%d%c", v[i], i == (v.size()-1) ? '\n' : ' ');
	return;
}

int solve(int n){
	int i, resp = 0;
	if(n == 1)
		return 0;
	vector<int> aux;
	pair<vector<int>, int> P = pair<vector<int>, int>(v, 0);
	q.push(P);
	vis.insert(v);
	while(!q.empty()){
		P = q.front();
		q.pop();
//		imprimir(P.x);
		if(solution(P.x)){
			while(!q.empty())
				q.pop();
			return P.y;
		}
		for(i = 0; i < (n-1); i++){
			aux = P.x;
			swap(aux[i], aux[i+1]);
			if(vis.find(aux) == vis.end()){
				q.push(pair<vector<int>, int> (aux, P.y+1));
				vis.insert(aux);
			}
		}
	}
	return 0;
}

int main(){
	int i, j, n, k, casos, maximo;
	scanf("%d", &casos);
	for(i = 1; i <= casos; i++){
		scanf("%d", &n);
		for(j = 0; j < n; j++){
			scanf("%d", &k);
			v.push_back(k);
		}
		printf("Case #%d: %d\n", i, solve(n));
		v.clear();
		vis.clear();
	}
	return 0;
}
