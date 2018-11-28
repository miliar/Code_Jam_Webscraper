#include <bits/stdc++.h>
using namespace std;

string solve (char x, int level){
	if (level == 0)
		return string(1, x);
	string a = "";
	string b = "";
	if (x == 'R'){
		a = solve('R', level-1);
		b = solve('S', level-1);
	}else if (x == 'P'){
		a = solve('P', level-1);
		b = solve('R', level-1);
	}else if (x == 'S'){
		a = solve('P', level-1);
		b = solve('S', level-1);
	}else
		assert(false);
	return a<b ? a+b : b+a;
}

void main2(){
	int n,r,s,p;
	cin >> n >> r >> p >> s;
	vector<string> q;
	q.push_back(solve('R', n));
	q.push_back(solve('P', n));
	q.push_back(solve('S', n));
	sort(q.begin(), q.end());
	for (int i=0; i<(int)q.size(); i++){
		int cnt_r=0, cnt_p=0, cnt_s=0;
		for (int j=0; j<(int)q[i].size(); j++){
			if (q[i][j] == 'R') cnt_r++;
			if (q[i][j] == 'P') cnt_p++;
			if (q[i][j] == 'S') cnt_s++;
		}
		if (cnt_r==r && cnt_s==s && cnt_p==p){
			cout << q[i] << endl;
			return;
		}
			
	}
	cout << "IMPOSSIBLE" << endl;
}

int main(){
	int t; cin >> t;
	for (int o=1; o<=t; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
