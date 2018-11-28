#include <iostream>
#include <vector>
#include <string>

using namespace std;

int compute_steps(string& s) {
	int sz = s.size();
	vector<int> tmp(sz,0);
	int ctr = 0;
	for(int i=0; i<sz; i++){
		if (s[i]=='+') tmp[i]=1;
	}
	for(int i=sz-1; i>=0; i--){
		if (!(ctr&1) && tmp[i]) continue;
		else if (!(ctr&1) && !tmp[i]) ctr++;
		else if ((ctr&1) && tmp[i]) ctr++;
		else if ((ctr&1) && !tmp[i]) continue;
	}
	return ctr;
}

int main(int argc, char *argv[])
{
	int T, res;
	cin >> T;
	string s;
	for(int i=1; i<=T; i++){
		cin >> s;
		res = compute_steps(s);
		cout << "Case #" << i << ": " << res << endl;
	}
    return 0;
}
