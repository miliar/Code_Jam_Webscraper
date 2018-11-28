#include<bits/stdc++.h>

using namespace std;

typedef pair<int, int> pii;
typedef long long int LL;
typedef vector<int> VI;

#define sd(x) scanf("%d", &x)
#define MP make_pair
#define PB push_back
#define F first
#define S second
#define MOD 1000000007
#define D double
#define LD long double
double EPS = 1e-12;

#define N 1123

string s[N];

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("aout.txt", "w", stdout);
	int t;
	sd(t);
	for(int cas = 0; cas < t; cas++){
		printf("Case #%d: ", cas + 1);
		int r, c;
		bool pf, tf;
		int i, j, k;
		int ans = 0;
		int c1, c2, c3, c4;
		sd(r); sd(c);
		for(i = 0; i < r; i++){
			cin>>s[i];
		}
		pf = false;
		for(i = 0; i < r; i++){
			for(j = 0; j < c; j++){
				if(s[i][j] != '.'){
					c1 = 0;
					for(k = 0; k < i; k++){
						if(k != i){
							if(s[k][j] != '.'){
								c1++;
							}
						}
					}
					c2 = 0;
					for(k = i + 1; k < r; k++){
						if(k != i){
							if(s[k][j] != '.'){
								c2++;
							}
						}
					}
					c3 = 0;
					for(k = 0; k < j; k++){
						if(k != j){
							if(s[i][k] != '.'){
								c3++;
							}
						}
					}
					c4 = 0;
					for(k = j + 1; k < c; k++){
						if(k != j){
							if(s[i][k] != '.'){
								c4++;
							}
						}
					}
					if(c1 + c2 + c3 + c4 == 0){
						pf = true;
					}
					if(s[i][j] == '^'){
						if(c1 == 0){
							ans++;
						}
					}
					if(s[i][j] == 'v'){
						if(c2 == 0){
							ans++;
						}
					}
					if(s[i][j] == '<'){
						if(c3 == 0){
							ans++;
						}
					}
					if(s[i][j] == '>'){
						if(c4 == 0){
							ans++;
						}
					}
				}
			}
		}
		if(pf){
			printf("IMPOSSIBLE\n");
		}
		else{
			printf("%d\n", ans);
		}
	}
	return 0;
}

