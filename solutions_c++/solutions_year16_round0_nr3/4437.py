#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector <int> to2 (long long k) {
	vector <int> ans;
	while (k) {
		ans.push_back(k%2);
		k >>= 1;
	}
	reverse (ans.begin(), ans.end());
	return ans;
}

long long to_base(long long k, long long s) {
	vector <int> temp = to2(k);
	long long ans = 0;
	for (int i = 0; i < temp.size(); ++i) {
		ans *= s;
		ans += temp[i];
	}
	return ans;
}
int main() {
	ifstream cin ("input.txt");
	ofstream cout ("output.txt");
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ": " << endl;
		int n, j;
		cin >> n >> j;
		for (int k = (1<<(n-1))+1; k < (1<<n); k += 2) {
			vector <long long> div;
			for (int s = 2; s <= 10; ++s) {
				long long b = to_base(k, s);
				long long temp = 2;
				while (temp * temp <= b) {
					if (b % temp == 0) {
						div.push_back(temp);
						break;
					}
					++temp;
				}
			}
			if (div.size() == 9) {
				vector <int> ans = to2(k);
				for (int z = 0; z < ans.size(); ++z)
					cout << ans [z];
				cout << " ";
				for (int z = 0; z < div.size(); ++z)
					cout << div[z] << " ";
				cout << endl;
				--j;
				if (j == 0)
					break;
			}
		}
	}
}