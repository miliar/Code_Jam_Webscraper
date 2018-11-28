#include <bits/stdc++.h>
using namespace std;
#define forn(i, n) for(int i = 0; i < (int) (n); i++)
#define dforn(i, n) for(int i = (n) - 1; i >= 0; i--)
const int R = 256;

int tc, n, cnt[R], TC;
char best[10];
string dig[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
string s, ans;

int main(){
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	for(char ch = 'A'; ch <= 'Z'; ch++){
		//printf("%c:", ch);
		forn(i, 10){
			forn(j, dig[i].size()){
				char c = dig[i][j];
				if(c == ch){
					//printf(" %d", i);
					break;
				}
			}
		}
		//puts("");
	}
	
	vector<int> gp[4];
	gp[0].push_back(0);
	gp[0].push_back(2);
	gp[0].push_back(4);
	gp[0].push_back(6);
	gp[0].push_back(8);
	
	gp[1].push_back(3);
	gp[1].push_back(5);
	gp[1].push_back(7);
	
	gp[2].push_back(9);
	
	gp[3].push_back(1);
	
	best[0] = 'Z';
	best[1] = 'E';
	best[2] = 'W';
	best[3] = 'H';
	best[4] = 'U';
	best[5] = 'F';
	best[6] = 'X';
	best[7] = 'S';
	best[8] = 'G';
	best[9] = 'I';
	
	scanf("%d", &tc);
	while(tc--){
		cin >> s;
		n = (int) s.size();
		
		memset(cnt, 0, sizeof cnt);
		forn(i, n){
			cnt[ (int) s[i] ]++;
		}
		
		forn(z, 4){
			forn(i, gp[z].size()){
				int ac = gp[z][i];
				while(cnt[ (int) best[ac] ]){
					forn(j, dig[ac].size()){
						char c = dig[ac][j];
						// printf("Deleting %c\n", c);
						cnt[ (int) c]--;
					}
					ans += ac + '0';
				}
			}
		}
		
		sort(ans.begin(), ans.end());
		printf("Case #%d: ", ++TC);
		cout << ans << endl;
		ans.clear();
	}
	return 0;
}
