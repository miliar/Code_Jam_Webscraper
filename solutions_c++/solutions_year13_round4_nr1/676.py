#include <algorithm>
#include <fstream>
#include <iostream>

using namespace std;

long long o[1000], e[1000], p[1000];

struct node {
	int a, b;
	long long c;
} tmp[1000000];

bool operator < (node a, node b) {
	return(a.c < b.c);
}

int main() {
	ifstream fin("a.in");
	ofstream fout("a.out");
	int t, m, x, et, tt, i, j, k;
	long long n, y;
	fin >> t;
	for(x = 1; x <= t; x++) {
		fin >> n >> m;
		for(i = 0; i < m; i++) {
			fin >> o[i] >> e[i] >> p[i];
			for(j = 0; j < i; j++) if(o[j] > o[i] || ((o[j] == o[i]) && (e[j] > e[i]))) {
				tt = o[i];
				o[i] = o[j];
				o[j] = tt;
				tt = e[i];
				e[i] = e[j];
				e[j] = tt;
				tt = p[i];
				p[i] = p[j];
				p[j] = tt;
			}
		}
		et = 0; 
		for(i = 0; i + 1 < m; i++) for(j = i + 1; j < m; j++) if(o[i] < o[j] && o[j] <= e[i] && e[i] < e[j]) {
			tmp[et].a = i;
			tmp[et].b = j;
			tmp[et].c = (o[j] - o[i]) * (e[j] - e[i]) % 1000002013;
			et++;
		}
		if(et > 0) sort(tmp, tmp + et);
		y = 0;
		for(i = 0; i < et; i++) if(p[tmp[i].a] > 0 && p[tmp[i].b] > 0) {
			if(p[tmp[i].a] > p[tmp[i].b]) {
				y = (y + p[tmp[i].b] * tmp[i].c % 1000002013) % 1000002013;
				p[tmp[i].a] -= p[tmp[i].b];
				p[tmp[i].b] -= p[tmp[i].b];
			}
			else {
				y = (y + p[tmp[i].a] * tmp[i].c % 1000002013) % 1000002013;
				p[tmp[i].a] -= p[tmp[i].a];
				p[tmp[i].b] -= p[tmp[i].a];
			}
		}
		fout << "Case #" << x << ": " << y << "\n";
	}
	return 0;
} 
