#include <iostream>
using namespace std;

int at(const std::string& s, int i)
{
	return s[i] - '0';
}

int main(int ac, char* av[])
{
	int N;
	cin >> N;
	for (int I=1; I<=N; ++I) {
		int n;
		string s;
		cin >> n >> s;
		int r = 0;
		int t = 0;
		for (int i=0; i<=n; ++i) {
			if (i == 0) {
				t += at(s, i);
				continue;
			}
			if (t < i) {
				r += (i-t);
				t += (i-t);
			}
			t += at(s, i);
		}
		cout << "Case #" << I << ": " << r << endl;
	}
	return 0;
}

