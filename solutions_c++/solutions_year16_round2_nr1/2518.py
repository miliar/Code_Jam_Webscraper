#include<iostream>

using namespace std;

#define REP(a, b, c) for(int a=(b); a<(c); a++)

string dig[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int itr_d[10] = {0, 2, 4, 6, 8, 1, 3, 5, 7, 9};
char itr_a[11] = "ZWUXGOTFVI";
int cnt_a[26], cnt_d[10];

int main(){
	int T;
	cin >> T;
	REP(t, 1, T+1){
		string s;
		cin >> s;
		REP(i, 0, 26) cnt_a[i] = 0;
		REP(i, 0, 10) cnt_d[i] = 0;
		REP(i, 0, s.size()) cnt_a[s[i]-'A']++;
		REP(i, 0, 10){
			cnt_d[itr_d[i]] = cnt_a[itr_a[i]-'A'];
			REP(j, 0, dig[itr_d[i]].size()){
				cnt_a[dig[itr_d[i]][j]-'A'] -= cnt_d[itr_d[i]];
			}
		}
		cout << "Case #" << t << ": ";
		REP(i, 0, 10){
			REP(j, 0, cnt_d[i]) cout << i;
		}
		cout << "\n";
	}
	return 0;
}
