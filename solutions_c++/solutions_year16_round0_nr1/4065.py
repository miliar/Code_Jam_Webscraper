#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
using namespace std;
vector <int> f(long long n) {
	vector <int> ret;
	while(n) {
		ret.push_back(n % 10);
		n/=10;
	}	
	return ret;
} 
int main() {
	freopen("A-large.in.txt", "r", stdin);
	freopen("A-large.out.txt", "w", stdout);

	int t;
	cin>>t;
	for (int cas = 1; cas <= t; cas++) {
		int num;
		cin>>num;
		if (num == 0) {
			cout << "Case #" << cas << ": " << "INSOMNIA" << endl;
		} else {
			map <int,int> mp;
			long long now = num;
			int cnt = 0;
			while(1) {
				vector <int> p = f(now);
				for (int i=0;i<p.size();i++) {
					if (mp[p[i]] == 0) {
						cnt++;
						mp[p[i]] = 1;
					}
				}
				if (cnt == 10) {
					break;
				}
				now += num;
			}
			cout << "Case #" << cas << ": " << now << endl;
		}
	}
	return 0;
}