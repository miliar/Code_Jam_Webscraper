#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long int ulli;
typedef long long int lli;
#define pb push_back
#define ft first
#define se second
#define mp make_pair

vector<int> extract(lli n){
	vector<int> res;
	if(n == 0){
		res.push_back(0);
		return res;
	}
	while(n > 0){
		res.push_back(n % 10);
		n /= 10;
	}
	return res;
}

int main(){
	int t;
	cin >> t;
	for(int no = 1; no <= t; no++){
		lli n;
		cin >> n;
		lli tmp = n;
		set<int> digits;
		bool flag = true;
		if(n == 0) flag = false;
		vector<int> vtmp = extract(tmp);
		for(int i = 0; i < vtmp.size(); i++) digits.insert(vtmp[i]);
		if(digits.size() == 10) flag = false;
		while(flag){
			tmp += n;
			vtmp = extract(tmp);
			for(int i = 0; i < vtmp.size(); i++) digits.insert(vtmp[i]);
			if(digits.size() == 10) flag = false;
		}
		if(n != 0) cout << "Case #" << no << ": " << tmp << endl;
		else cout << "Case #" << no << ": INSOMNIA" << endl;
	}
}