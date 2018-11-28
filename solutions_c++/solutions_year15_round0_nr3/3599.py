#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int T = 0;
	cin >> T;

	for (int t = 0; t < T; t++) {
		__int64 L, X;
		string s;
		cin >> L >> X >> s;

		vector<int> v0, v;
		for (auto c : s){
			switch (c){
			case 'i': v0.push_back(1); break;
			case 'j': v0.push_back(2); break;
			case 'k': v0.push_back(3); break;
			}
		}

		for (__int64 i = 0; i < X; i++) {
			v.insert(v.end(), v0.begin(), v0.end());
		}

		const int mul[8][8] = {
			0,1,2,3,4,5,6,7,
			1,4,3,6,5,0,7,2,
			2,7,4,1,6,3,0,5,
			3,2,5,4,7,6,1,0,
			4,5,6,7,0,1,2,3,
			5,0,7,2,1,4,3,6,
			6,3,0,5,2,7,4,1,
			7,6,1,0,3,2,5,4
		};
		const int inv[8] = {0,5,6,7,4,1,2,3};
		
		bool ok = false;
		int sub0 = 0;
		for (size_t i = 0; i < v.size(); i++) {
			sub0 = mul[sub0][v[i]];
			if (sub0 != 1) continue;

			int sub1 = 0, sub2 = 0;
			for (size_t j = i + 1; j < v.size(); j++) {
				sub2 = mul[sub2][v[j]];
			}
			for (size_t j = i + 1; j < v.size(); j++) {
				sub1 = mul[sub1][v[j]];
				sub2 = mul[inv[v[j]]][sub2];
				if (sub1 == 2 && sub2 == 3) {
					ok = true;
				}
			}
		}

		printf("Case #%d: %s\n", t + 1, ok?"YES":"NO");
	}

	return 0;
}