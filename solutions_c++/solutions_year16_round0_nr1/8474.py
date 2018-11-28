#include <iostream>
#include <vector>
#include <sstream>
#include <cstdio>
using namespace std;

vector<bool> mark;

bool check() {
	for(int i = 0; i < 10; i++)
		if(!mark[i])
			return false;
	return true;
}

void updateMark(string s) {
	for(int i = 0; i < s.size(); i++)
		mark[s[i] - '0'] = true;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	cin>>T;
	unsigned long long n, m;
	stringstream ss;
	string temp;
	for(int k = 1; k <= T; k++) {
		cin>>n;
		m = 0;
		mark = vector<bool>(10,false);
		if(n == 0) {
			cout<<"Case #"<<k<<": INSOMNIA"<<endl;
			continue;
		}
		while(++m) {
			ss.clear();
			ss<<(m*n);
			ss>>temp;
			updateMark(temp);
			if(check())
				break;
		}
		cout<<"Case #"<<k<<": "<<(n*m)<<endl;
	}

	return 0;
}