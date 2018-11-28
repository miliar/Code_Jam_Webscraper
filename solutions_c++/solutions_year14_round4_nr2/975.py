#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long LL;

vector<int>x;


inline int min2(int a, int b) {
	if (a<b)	return a;

	return b;
}

inline vector<int>::iterator gao(int &pos) {
	vector<int>::iterator index = x.begin();
	vector<int>::iterator i;
	int ii;
	for (i=x.begin(), ii=0; i!=x.end(); i++, ii++) {
		if (*i < *index) {
			index = i;
			pos = ii;
		}
	}

	return index;
}

int main()
{
	freopen("E:\\Projects\\VS2010\\gcj2014\\gcj2014\\Round2\\B\\B--large.in", "r", stdin);
	freopen("E:\\Projects\\VS2010\\gcj2014\\gcj2014\\Round2\\B\\B.out", "w", stdout);
	int T;

	cin >>T;

	for (int t=1; t<=T; t++) {
		cout << "Case #" << t << ": ";

		int n;
		cin >> n;
		x = vector<int>(n);

		for (int i=0; i<n; i++) {
			cin >> x[i];
		}

		LL result = 0;
		while (x.size()) {
			int pos = 0;
			vector<int>::iterator in = gao(pos);

			result += min2(pos, x.size()-1-pos);

			x.erase(in);
		}

		cout << result << endl;
		
	}
	return 0;
}