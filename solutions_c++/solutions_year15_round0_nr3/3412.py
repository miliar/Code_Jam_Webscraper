//~In The Name Of Allah~//
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <iomanip>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <cmath>
#include <string.h>
#include <sstream>
#include <cstring>
#include <fstream>
#include <functional>
#include <cstdio>
#include <stack>
#include <utility> 
#include <set>
#include <list>
#include <queue>
#include <bitset>
using namespace std;

#define all(S) S.begin(), S.end()
#define rall(S) S.rbegin(), S.rend()
#define mem(C, V) memset(C, V, sizeof C)
#define sp(N) setprecision(N)<<fixed
#define siz(S) (int)S.size()
#define rz(S, N) S.resize(N)
#define rep(i, j) for (int i = 0; i < int(j); i++)
#define Rep(i, j, k) for (int i = (int)j; i < (int)k; i++)
#define srep(S) for (auto it:S)
#define Theta(A) acos((double)A)*180.0 / Pi
#define getdis(xa, ya, xb, yb) double(sqrt((xa - xb)*(xa - xb) + (ya - yb)*(ya - yb)))
#define slope(xa, ya, xb, yb) ((double)yb-(double)ya)/((double)xb-(double)xa)

#define Read() freopen("input.txt", "r", stdin)
#define Write() freopen("output.txt", "w", stdout)

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<ll> vll;
typedef vector<string> vs;

const double Pi = 2.0 * acos(0.0);

const double Ex = 2.7182818284;
const int Mod = 1000000007;
const int oo = 2e9 + 1;

int di[] = { 0, 1, 0, -1 };
int dj[] = { 1, 0, -1, 0 };
int dik[] = { 1, 1, 2, 2, -1, -1, -2, -2 };
int djk[] = { 2, -2, 1, -1, -2, 2, -1, 1 };

ll gcd(ll x, ll y){ return !y ? x : gcd(y, x%y); }

int main(){
	Read(), Write();
	int test, n, k;
	map<pair<char, char>, string> mat;
	mat[make_pair('1', '1')] = "1";
	mat[make_pair('1', 'i')] = "i";
	mat[make_pair('1', 'j')] = "j";
	mat[make_pair('1', 'k')] = "k";

	mat[make_pair('i', '1')] = "i";
	mat[make_pair('i', 'i')] = "-1";
	mat[make_pair('i', 'j')] = "k";
	mat[make_pair('i', 'k')] = "-j";

	mat[make_pair('j', '1')] = "j";
	mat[make_pair('j', 'i')] = "-k";
	mat[make_pair('j', 'j')] = "-1";
	mat[make_pair('j', 'k')] = "i";

	mat[make_pair('k', '1')] = "k";
	mat[make_pair('k', 'i')] = "j";
	mat[make_pair('k', 'j')] = "-i";
	mat[make_pair('k', 'k')] = "-1";

	scanf("%d", &test);
	int idx = 0;
	while (test-- && scanf("%d%d", &n, &k)){
		string str, add, hopei, hopej, hopek;
		int ni, nj, nk, idxi, idxj, idxk;
		ni = nj = nk = 0;
		idxi = idxj = idxk = -1;
		cin >> str, add = str, str = "";
		printf("Case #%d: ", ++idx);
		while (k--) str += add;
		if (str == "ijk"){
			printf("YES\n");
			continue;
		}
		Rep(i, 1, siz(str)){
			string tmp = mat[make_pair(str[i - 1], str[i])];
			char hope;
			if (siz(tmp) == 2) hope = tmp[1], ni++;
			else hope = tmp[0];
			if (hope == 'i'  && ni % 2 == 0){
				idxi = i + 1;
				break;
			}
			str[i] = hope;
		}
		if (idxi == -1){
			printf("NO\n");
			continue;
		}
		Rep(i, idxi + 1, siz(str)){
			string tmp = mat[make_pair(str[i - 1], str[i])];
			char hope;
			if (siz(tmp) == 2) hope = tmp[1], nj++;
			else hope = tmp[0];
			if (hope == 'j'  && nj % 2 == 0){
				idxj = i + 1;
				break;
			}
			str[i] = hope;
		}
		if (idxj == -1){
			printf("NO\n");
			continue;
		}
		Rep(i, idxj + 1, siz(str)){
			string tmp = mat[make_pair(str[i - 1], str[i])];
			char hope;
			if (siz(tmp) == 2) hope = tmp[1], nk++;
			else hope = tmp[0];
			if (hope == 'k'  && nk % 2 == 0){
				idxk = max(i + 1, idxk);
			}
			str[i] = hope;
		}
		if (idxk != siz(str)){
			printf("NO\n");
			continue;
		}
		printf("YES\n");
	}
	return 0;
}