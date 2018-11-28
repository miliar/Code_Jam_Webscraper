#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <functional>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <utility>
#include <bitset>
#include <list>
#define FOR(i, a, b) 	for (i=a; i<b; i++)
#define REV(i, a, b) 	for (i=a; i>=b; i--)
#define TR(tipo, c, it) for (tipo::iterator it=(c).begin(); it!=(c).end(); it++)
#define SET(var, c)		memset(var, c, sizeof(var))
#define READ(file)		freopen(file, "r", stdin)
#define WRITE(file)		freopen(file, "w", stdout)
#define pb 				push_back
#define mp              make_pair
#define X				first
#define Y				second
#define PI				(acos(0.0)*2.0)
#define EPS             1e-10
#define INF 			1000000000
#define LIM             100001

using namespace std;
typedef long long 		ll;
typedef vector<int> 	vi;
typedef pair<int, int> 	ii;
typedef vector<ii> 		vii;

double mem[LIM], c, f, x;

int main(void){
	int i, caso, ncasos;
	double mx, curr;
	setvbuf(stdin, NULL, _IOFBF, 1<<18);
	setvbuf(stdout, NULL, _IOFBF, 1<<18);
	READ("B-large.in");
	WRITE("B-large.out");
	scanf("%d", &ncasos);
	fprintf(stderr, "%d\n", ncasos);
	FOR(caso, 0, ncasos){
		scanf("%lf %lf %lf", &c, &f, &x);
		SET(mem, 0);
		i=0; curr=mx=x;
		while(i<LIM && curr<=mx){
			curr=x/(2.0+i*f)+mem[i];
			if (mx>curr) mx=curr;
			mem[i+1]=mem[i]+c/(2.0+i*f);
			i++;
		}
		printf("Case #%d: %.7lf\n", 1+caso, mx);
		fprintf(stderr, "Case #%d: %.7lf\n", 1+caso, mx);
	}
	return 0;
}


