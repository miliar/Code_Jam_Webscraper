#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
int N, J;
int cnt = 0;
void helper(string s, int idx, int cnt1, int cnt2){
	if(cnt == J) return;
	if(cnt1 == cnt2 && cnt1 == 2){
		cnt++;
		idx++;
		cout << s << " 3 2 3 2 7 2 3 2 3" << endl;
	}
	for(int i = idx + 1; i < N - 1; i++){
		s[i] = '1';
		if(i%2)
			helper(s, i, cnt1+1, cnt2);
		else
			helper(s, i, cnt1, cnt2+1);
		s[i] = '0';
	}
}
int main(){
	int T;
	cin >> T;
	cin >> N >> J;
	cout << "Case #1: " << endl;
	string s(N, '0');
	s[0] = '1';
	s[N-1] = '1';
	helper(s, 0, 0, 0);
}