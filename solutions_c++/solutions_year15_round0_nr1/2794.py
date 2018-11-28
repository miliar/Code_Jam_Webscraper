#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <utility>
#include <cstring>
using namespace std;

#define rep(i,n) for(int i=0; i<n; i++)
typedef long long ll;

int main() {
	int t;
	cin >> t;
	for(int dt=1; dt<=t; dt++) {
		int smax;
		string in;
		cin >> smax;
		cin >> in;
		int sum=0, need=0;
		rep(i, smax+1) {
			if(sum < i) {
				need += i - sum;
				sum = i;
			}
			sum += (in[i]-'0');
		}
		cout << "Case #" << dt << ": " << need << endl;
	}
	return 0;
}
