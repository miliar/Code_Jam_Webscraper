#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

#define REP(a, b, c) for(long long a=(b); a<(c); a++)

using namespace std;

int map[8][8] = {{0, 1, 2, 3, 4, 5, 6, 7},
				{1, 4, 3, 6, 5, 0, 7, 2},
				{2, 7, 4, 1, 6, 3, 0, 5},
				{3, 2, 5, 4, 7, 6, 1, 0},
				{4, 5, 6, 7, 0, 1, 2, 3},
				{5, 0, 7, 2, 1, 4, 3, 6},
				{6, 3, 0, 5, 2, 7, 4, 1},
				{7, 6, 1, 0, 3, 2, 5, 4}};

int main(){
	std::ios::sync_with_stdio(false);
	int T;
	cin >> T;
	REP(t, 1, T+1){
		cout << "Case #" << t << ": ";
		int L, X;
		cin >> L >> X;
		string stemp, s;
		cin >> stemp;
		REP(i, 0, X) s += stemp;
		int start_state = 0, next_state, char_to_chk = 0;
		//Search for i
		REP(i, char_to_chk, L*X){
			next_state = s[i] - 'i' + 1;
			start_state = map[start_state][next_state];
			char_to_chk = i + 1;
			if(start_state==1){
				break;
			}
		}
		if(char_to_chk==(L*X)){
			cout << "NO\n";
			continue;
		}else{
			start_state = 0;
		}
		//Search for j
		REP(i, char_to_chk, L*X){
			next_state = s[i] - 'i' + 1;
			start_state = map[start_state][next_state];
			char_to_chk = i + 1;
			if(start_state==2){
				break;
			}
		}
		if(char_to_chk==(L*X)){
			cout << "NO\n";
			continue;
		}else{
			start_state = 0;
		}
		//check k
		REP(i, char_to_chk, L*X){
			next_state = s[i] - 'i' + 1;
			start_state = map[start_state][next_state];
		}
		if(start_state==3){
			cout << "YES\n";
		}else{
			cout << "NO\n";
		}
	}
	return 0;
}

