#include <bits/stdc++.h>
typedef long long LL;
using namespace std;


LL solve(LL n){
	set<LL> inputs;
	int i = 1;
	LL j;
	for(;; j=(i*n), ++i){
		if(i==1000)return -1;
		LL tmp = j;
		while(tmp>0){
			inputs.insert(tmp%10);
			if(inputs.size() == 10) return j;	
			tmp /= 10;
		}	}
}


int main() {
	ofstream out("output1.txt");
	LL t, n, i = 1;
	cin >> t;
	while(i <= t){
		cin >> n;
		LL res = solve(n);

		out << "Case #" << i++ << ": ";
		if(res != -1) out << res << endl;
		else out << "INSOMNIA" << endl;
	}}

