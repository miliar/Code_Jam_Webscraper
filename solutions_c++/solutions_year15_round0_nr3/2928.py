#include <iostream>
#include <stdio.h>
#include <queue>
using namespace std;

int main() {
	freopen("/mnt/S/Code/in.txt", "rt", stdin);
	freopen("/mnt/S/Code/out.txt", "wt", stdout);

	int n, l, x;
	string s;
	// l is the length of the string
	// x is how many times it will be repeated
	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		cin >> l >> x >> s;
		string dummy = s;
		for (int i = 0; i < x - 1; ++i)
		{
			s.append(dummy);
		}
		string c = "1";
		int cnt = 0;
		for (int i = 0; i < x * l; ++i)
		{
			if (c == "1")
			{
				if (s[i] == 'i')c = "i";
				else if (s[i] == 'j')c = "j";
				else if (s[i] == 'k')c = "k";
			}
			else if (c == "-1")
			{
				if (s[i] == 'i')c = "-i";
				else if (s[i] == 'j')c = "-j";
				else if (s[i] == 'k')c = "-k";
			}
			else if (c == "i")
			{
				if (s[i] == 'i')c = "-1";
				else if (s[i] == 'j')c = "k";
				else if (s[i] == 'k')c = "-j";
			}
			else if (c == "-i")
			{
				if (s[i] == 'i')c = "1";
				else if (s[i] == 'j')c = "-k";
				else if (s[i] == 'k')c = "j";
			}
			else if (c == "j")
			{
				if (s[i] == 'i')c = "-k";
				else if (s[i] == 'j')c = "-1";
				else if (s[i] == 'k')c = "i";
			}
			else if (c == "-j")
			{
				if (s[i] == 'i')c = "k";
				else if (s[i] == 'j')c = "1";
				else if (s[i] == 'k')c = "-i";
			}
			else if (c == "k")
			{
				if (s[i] == 'i')c = "j";
				else if (s[i] == 'j')c = "-i";
				else if (s[i] == 'k')c = "-1";
			}
			else if (c == "-k")
			{
				if (s[i] == 'i')c = "-j";
				else if (s[i] == 'j')c = "i";
				else if (s[i] == 'k')c = "1";
			}

			if (cnt == 0) {
				if (c[0] == 'i') {
					cnt++;
					c = "1";
				}
			} else if (cnt == 1) {
				if (c[0] == 'j') {
					cnt++;
					c = "1";
				}
		} else if (cnt == 2) {
				if (c[0] == 'k') {
					cnt++;
				}
			}
		}
		cout << "Case #" << i + 1 << ": ";		
		if (cnt == 3 && c[0] == 'k') {
			cout << "YES"<<endl;
		} else {
			cout << "NO"<<endl;
		}
	}
	return 0;
}



