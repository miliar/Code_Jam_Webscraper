#include<iostream>
#include<string>
using namespace std;

string work(string in) {
	string ret;
	for (int i = 0; i < in.size(); ++i) {
		if (i == 0) {
			ret += in[i];
		}
		else {
			if (in[i] >= ret[0]) {
				ret = in[i] + ret;
			}
			else {
				ret += in[i];
			}
		}
	}
	return ret;
}

int main() {
	freopen("A-large.in", "r", stdin);  
    freopen("A-large.out", "w", stdout);
	string str;
	int Cases;
	scanf("%d", &Cases);
	for (int i = 1; i <= Cases; ++i) {
		cin>>str;
		cout << "Case #" << i << ": " << work(str) << endl;
	}
	return 0;
}
