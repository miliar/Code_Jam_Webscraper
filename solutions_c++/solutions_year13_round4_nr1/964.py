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
#define MAX 1010
#define MOD 1000000007
using namespace std;

int vec8[8][2] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};// signo x+
int vec4[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};//signo +

void int_to_char(int n, char s[], int base = 10){
	int i = 0;
	do{
		s[i++] = (n%base)+'0';
		n /= base;
	}while(n > 0);
	reverse(s, s+i);
	return;
}

string int_to_string(int n, int base = 10){
	string s = "";
	int i = 0;
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

typedef long long int entero;
typedef pair<entero, entero> Point;
typedef pair<entero, Point> Tri;

int n, m;
entero N;
map<entero, Point > v;
map<entero, Point >::iterator it;
stack<Point> q;

entero solve(entero original){
	Tri actual;
	entero cont, resp = 0, d;
	Point p;
	for(it = v.begin(); it != v.end(); it++){
		actual = (*it);
//		cout << "va = " << actual.x << endl;
		//si entran
		if(actual.y.x>0){
			//los meto en la pila
			q.push(Point(actual.x, actual.y.x));
		}
		if(actual.y.y > 0){
			for(cont = actual.y.y; cont > 0; ){
				
				p = q.top();
				q.pop();
//				cout << "cont = " << cont << " " << p.x << " " << p.y << endl;
				if(p.y <= cont){
					cont-=p.y;
					d = actual.x-p.x;
					resp += ((d*N)-((d*(d-1))>>1))*p.y;
				}
				else{
					p.y-=cont;
					d = actual.x-p.x;
					resp += ((d*N)-((d*(d-1))>>1))*cont;
					q.push(p);
					cont = 0;
				}
//				cout << "resp = " << resp << endl;
			}
		}
	}
	if(!q.empty()){
		cout << "Error" << endl;
	}
//	cout << original << " + " << resp <<endl;
	return original-resp;
}

int main(){
	int a, b, personas, i, j, k, casos;
	entero original, d;
	scanf("%d", &casos);
	for(i = 0; i < casos; i++){
		original = 0;
		scanf("%d%d", &n, &m);
		N = n;
		for(j = 0; j < m; j++){
			scanf("%d%d%d", &a, &b, &personas);
			d = (b-a);
			original += ((d*N)-((d*(d-1))>>1))*personas;
			if(v.find(a) == v.end()){
				v[a] = Point(personas, 0);
			}
			else{
				v[a].x+=personas;
			}
			if(v.find(b) == v.end()){
				v[b] = Point(0, personas);
			}
			else{
				v[b].y+=personas;
			}
		}
		printf("Case #%d: ", i+1);
//		cout << endl;
		cout << solve(original) << endl;
		v.clear();
		
	}
	return 0;
}
