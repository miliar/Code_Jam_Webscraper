#include <cstdio>
#include <algorithm>
#include <vector>

#define FOR(a,b,c) for (int c = (a), _for = (b); c < _for; ++c)
#define REP(n) for (int _rep = 0, _for = (n); _rep < _for; ++_rep)
#define pb push_back
#define x first
#define y second
#define ll long long

using namespace std;

class quat{
public:
	int v[4];
	quat(int a, int b, int c, int d){
		v[0] = a, v[1] = b, v[2] = c, v[3] = d;
	}
	quat(){FOR(0,4,i) v[i] = 0;}
};
const quat one(1, 0, 0, 0), i(0, 1, 0, 0), j(0, 0, 1, 0), k(0, 0, 0, 1);
quat operator-(quat a){FOR(0,4,i) a.v[i] *= -1; return a;}
quat operator+(quat a, quat b){FOR(0, 4, i) a.v[i] += b.v[i]; return a;}
void operator+=(quat &a, quat b){a = a + b;}
quat MulMat[4][4];
quat operator*(quat a, int b){FOR(0, 4, i) a.v[i] *= b; return a;}
quat operator*(int b, quat a){return a * b;}
quat operator*(quat a, quat b){
	quat r;
	FOR(0, 4, x) FOR(0, 4, y) r += MulMat[x][y] * a.v[x] * b.v[y];
	return r;
}
void operator*=(quat &a, quat b){a = a * b;}
bool operator==(quat a, quat b){FOR(0,4,i) if (a.v[i] != b.v[i]) return false; return true;}
bool operator!=(quat a, quat b){FOR(0,4,i) if (a.v[i] != b.v[i]) return true; return false;}
quat c[256];

char yes[] = "YES", no[] = "NO";

int l, x;
char in[10005];

char* Solve(){
	scanf("%d%d%s", &l, &x, in);
	FOR(0, l, i) FOR(0, x, j) in[l * j + i] = in[i];
	l *= x;
	
	quat Q = one;
	FOR(0, l, i) Q *= c[in[i]]; //printf("%d %d %d %d\n", Q.v[0], Q.v[1], Q.v[2], Q.v[3]);
	if (Q != i * j * k) return no;
	
	Q = one;
	int p = 0;
	int ch = 0;
	for (; p < l; ++p){
		if (Q == i){++ch; break;}
		Q *= c[in[p]];
	}
	for (; p < l; ++p){
		if (Q == i * j){++ch; break;}
		Q *= c[in[p]];
	}
	if (ch == 2) return yes; else return no;
}

int main(){
	
	c['i'] = i;
	c['j'] = j;
	c['k'] = k;
	
	MulMat[0][0] = one;
	MulMat[0][1] = i;
	MulMat[0][2] = j;
	MulMat[0][3] = k;
	
	MulMat[1][0] = i;
	MulMat[1][1] = -one;
	MulMat[1][2] = k;
	MulMat[1][3] = -j;
	
	MulMat[2][0] = j;
	MulMat[2][1] = -k;
	MulMat[2][2] = -one;
	MulMat[2][3] = i;
	
	MulMat[3][0] = k;
	MulMat[3][1] = j;
	MulMat[3][2] = -i;
	MulMat[3][3] = -one;
	
	int t;
	scanf("%d", &t);
	FOR(1, t + 1, i){
		printf("Case #%d: %s\n", i, Solve());
	}
	return 0;
}
