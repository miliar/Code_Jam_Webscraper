#include <iostream>
#include <string>
using namespace std;

int canflip(string& str, int s, int n, int& flip){
	int s_ = s;
	while(s_ < str.size() && str[s_] == '+'){
		s_++;
	}
	if(s != s_){
		s = s_;
		return s;
	}
	int pivot = s;
	for (int i = s; i < str.size(); i++) {
		if(str[i] == '-') {
			pivot++;
		} else break;
	}
	int cnt = (pivot - s) / n;
	int res = (pivot-s) % n;
	flip += cnt;
	s += n*cnt;
	if (res && str.size() >= s+n+res) {
		for(int i = s+n; i < s+n+res; i++){
			str[i] = str[i] == '-' ? '+' : '-';
		}
		flip += 2;
		return s+res;
	} if (res == 0 && cnt) {
		return s;
	}
	return -1;
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("C:\\Users\\psw\\Desktop\\output.txt", "w", stdout);

	int tc;
	cin >> tc;
	for (int tc_ = 1; tc_ <= tc; tc_++){
		string str;
		int n;
		cin >> str >> n;
		int i = 0, flip = 0, start = 0;
		while(i < str.size()){
			i = canflip(str, i, n, flip);
			if(i == -1) break;
		}
		if (i == -1) cout << "Case #" << tc_ << ": IMPOSSIBLE\n";
		else cout << "Case #" << tc_ << ": " << flip << "\n";
	}
	return 0;
}