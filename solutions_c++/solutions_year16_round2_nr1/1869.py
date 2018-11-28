#include <cstdio>
#include <algorithm>
#include <cstring>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <iostream>
#include <set>
#include <cmath>
#include <cassert>
#include <ctime>
#include <string>

using namespace std;

#define db(x) cout << #x " == " << x << endl
#define _ << ", " <<
#define fr(a,b,c) for(int a = b; a < c; a++)
#define rp(a,b) fr(a,0,b)
#define fre(a,b) for(int a = ant[b]; ~a; a = ant[a])
#define cl(a,b) memset(a,b,sizeof(a))

#define st first
#define nd second
#define mp make_pair
#define pb push_back
#define add_edge(a,b,c) to[z] = b; ant[z] = adj[a]; adj[a] = z, capa[z] = c; z++
#define oo 0x3f3f3f3f
#define EPS 1e-8
#define MOD 1000000007

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair<int, pii> dist_pos;
typedef pair<ll, ll> pll;
typedef pair<int, char> pic;
typedef pair<double, int> pdi;

const int MAXS = 2010;

int T, N, len;
char S[MAXS];
int qtd[30];
char sear[10] = {'Z', 'X', 'W', 'G', 'U', 'S', 'O', 'V', 'N', 'T'};
vector<int> ans;

void hasChar(char c){
	while(qtd[c-'A'] > 0) {
		qtd[c-'A']--;
		if (c == 'Z'){
			ans.push_back(0);
			qtd['E'-'A']--;
			qtd['R'-'A']--;
			qtd['O'-'A']--;
		}
		if (c == 'X') {
			ans.push_back(6);
			qtd['S'-'A']--;
			qtd['I'-'A']--;
		}
		if (c == 'W') {
			ans.push_back(2);
			qtd['T'-'A']--;
			qtd['O'-'A']--;
		}
		if (c == 'G') {
			ans.push_back(8);
			qtd['E'-'A']--;
			qtd['I'-'A']--;
			qtd['H'-'A']--;
			qtd['T'-'A']--;
		}
		if (c == 'U') {
			ans.push_back(4);
			qtd['F'-'A']--;
			qtd['O'-'A']--;
			qtd['R'-'A']--;
		}
		if (c == 'S') {
			ans.push_back(7);
			qtd['E'-'A']--;
			qtd['V'-'A']--;
			qtd['E'-'A']--;
			qtd['N'-'A']--;
		}
		if (c == 'O') {
			ans.push_back(1);
			qtd['N'-'A']--;
			qtd['E'-'A']--;
		}
		if (c == 'V') {
			ans.push_back(5);
			qtd['F'-'A']--;
			qtd['I'-'A']--;
			qtd['E'-'A']--;
		}
		if (c == 'N') {
			ans.push_back(9);
			qtd['E'-'A']--;
			qtd['I'-'A']--;
			qtd['N'-'A']--;
		}
		if (c == 'T') {
			ans.push_back(3);
			qtd['H'-'A']--;
			qtd['R'-'A']--;
			qtd['E'-'A']--;
			qtd['E'-'A']--;
		}
	}
}

int main(){
	scanf("%d\n", &T);
	rp(t, T){
		ans = vector<int>();
		memset(qtd, 0, sizeof(qtd));
		scanf("%s\n", S);
		len = strlen(S);
		rp(i, len) qtd[S[i]-'A']++;
		printf("Case #%d: ", t+1);
		rp(i, 10) hasChar(sear[i]);
		sort(ans.begin(), ans.end());
		for(vector<int>::iterator it = ans.begin(); it != ans.end(); it++)
			printf("%d", *it);
		printf("\n");
	}
}
