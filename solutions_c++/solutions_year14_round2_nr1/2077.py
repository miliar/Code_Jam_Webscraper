#include <iostream>
#include <string>	
#include <vector>

#define MAX 100
#define ABS(a) (a > 0 ? a : -a)

using namespace std;

string reduce (string s, int a[]) {
	a[0] = 1;
	string v = "";
	v += s[0];
	for (int i = 1, j = 0; i < s.size(); ++i)
	{
		if (s[i] == s[i-1]) a[j]++;
		else{
			j++;
			a[j] = 1;
			v += s[i];
		}
	}

	return v;
}

int main () {
	int t, n;
	string s, r;
	int a[MAX], b[MAX], count;

	cin >> t;
	int ca = 1;
	while (t--) {
		cin >> n;

		cin >> s >> r;

		count = 0;

		string c = reduce (s, a);
		string d = reduce (r, b);

		if (d != c) {
			cout << "Case #"<< ca++ <<": Fegla Won" << endl;
			continue;
		}

		for (int i = 0; i < c.size(); i++) {
			count += ABS((a[i]-b[i]));
		}

		cout <<"Case #"<< ca++ << ": "<< count << endl;
	}
	
	return 0;
}
