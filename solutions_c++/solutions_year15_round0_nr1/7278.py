#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
	long long p, n;
	string str;
	vector<long long> vec;
	cin >> p;
	for(long long pLoop = 0;pLoop < p;pLoop++){
		vec.clear();
		cin >> n >> str;
		for(long long i = 0;i < n;i++){
			string st = "";
			st += str[i];
			vec.push_back(atoi(st.c_str()));
		}
		long long curUp = 0, invitesNeeded = 0;
		for(long long i = 0;i <= n;i++){
			//cout << "i - " << i << " | curUp - " << curUp << " | invitesNeeded - " << invitesNeeded << "\n";
			if(curUp < i){
				invitesNeeded += i - curUp;
				curUp = i;
			}
			curUp += vec[i];
		}
		cout << "Case #" << pLoop+1 << ": " << invitesNeeded << "\n";
	}
	return 0;
}
