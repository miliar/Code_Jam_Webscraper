#include <bits/stdc++.h>
using namespace std;

char op (char x){
	if (x == 'C') return 'J';
	return 'C';
}	

void main2(){
	string s; cin >> s;
	int res = 0;
	int st_size = 0;
	char last = '?';
	for (int i=0; i<(int)s.size(); i++){
		if (st_size > 0 && last == s[i]){
			last = op(last);
			st_size--;
			res+=10;
		}else{
			st_size++;
			last = s[i];
		}
	}
	res+= 5 * (st_size/2);
	cout << res << endl;
}

int main(){
	int t; cin >> t;
	for (int o=1; o<=t; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
