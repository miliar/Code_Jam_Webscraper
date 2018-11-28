#include <iostream>
#include <vector>
#include <set>

using namespace std;

int sleep_count(int n)
{
	if (n == 0) return -1;
	set<int> s;
	int t, d, num, i;

	t = n;
	while (t) {
		d = t % 10;
		if (s.find(d) == s.end()) s.insert(d);
		t = t / 10;
	}

	i = 2;
	num = n;
	while (s.size() != 10) {
		num = i * n;
		t = num;
		while (t) {
			d = t % 10;
			if (s.find(d) == s.end()) s.insert(d);
			t = t/10;
		}
		i++;
	}
	return num;
}


int main()
{
	int T, n;
	vector<int> res;
	cin >> T;

	while (T--) {
		cin >> n;
		res.push_back(sleep_count(n));
	}

	for (int i = 0; i < res.size(); i++) {
		cout << "Case #" << i+1 << ": ";
		if (res[i] == -1)
			cout << "INSOMNIA";
		else 
			cout << res[i];
		cout << endl;
	}

	return 0;
}
