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

vector<string> v;
vector<string> caso[4];
Point mejor (-1, 0);

int arboles(int &n){
	int i, j, k, cont = 0;
	set<string> q;
	string r;

	for(i = 0; i < n; i++)
		if(caso[i].size() == 0)
			return -1;
//	cout << "arboles" << endl;
	for(i = 0; i < n; i++){
		for(j = 0; j < caso[i].size(); j++){
			for(k = 0, r = ""; k < caso[i][j].size(); k++){
				r += char(caso[i][j][k]);
//				cout << r << endl;
				q.insert(r);
			}
		}
		cont += q.size()+1;
//		cout << i << " " << q.size() << endl;
		q.clear();
	}
	return cont;
}

void rec(int m, int &n){
	if(m < 0){
		int cuenta = arboles(n);
		if(cuenta > mejor.x)
			mejor = Point(cuenta, 1);
		else if(cuenta == mejor.x)
			mejor.y++;
		return;
	}
	for(int i = 0; i < n; i++){
		caso[i].push_back(v[m]);
		rec(m-1, n);
		caso[i].erase(caso[i].begin()+(caso[i].size()-1));
	}
	return;
}

Point solve(int m, int n){
	rec(m-1, n);
	return mejor;
}

int main(){
	int i, j, n, m, casos;
	Point p;
	string s;
	scanf("%d", &casos);
	for(i = 1; i <= casos; i++){
		scanf("%d%d", &m, &n);
		for(j = 0; j < m; j++){
			cin >> s;
			v.push_back(s);
		}
		mejor = Point(-1, -1);
		p = solve(m, n);
		printf("Case #%d: %d %d\n", i, p.x, p.y);
		v.clear();
	}
	return 0;
}
