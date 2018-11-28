#include <iostream>
#include <string>

using namespace std;

int main() {

	int n;
	cin >> n;
	int count = 0;
	while (count++<n) {
		int n;
		string s[100];
		char c[100][100] = {0};//character
		int o[100][100] = {0};// occurence

		cin >> n;
		for (int i=0; i<n; i++) {
			cin >> s[i];
			char lastchar = 0;
			int k=-1;
			for (int j=0; j<s[i].length(); j++) {
				if (s[i][j] != lastchar) {
					lastchar = s[i][j];
					c[i][++k] = lastchar;
				}
				++o[i][k];
			}
			/*for (int j=0; j<=k; j++)
				cout << c[i][j] << "*" << o[i][j] << " ";
			cout << endl;*/
		}
		bool ok=true;
		for (int i=0; i<100 && ok; i++)
			for (int j=0; j<n-1 && ok; j++)
				for (int k=j+1; k<n && ok; k++)
					if (c[j][i] != c[k][i])
						ok = false;
		if (!ok) {
			cout << "Case #" << count << ": Fegla Won" << endl;
			continue;
		}
		
		int correction = 0;
		for (int i=0; i<100; i++) {
			double sum = 0.5;
			for (int j=0; j<n; j++)
				sum += o[j][i];
			int med = (int) (sum / n);
			for (int j=0; j<n; j++)
				correction += (o[j][i] > med ? o[j][i] - med : med - o[j][i]);
		}

		cout << "Case #" << count << ": " << correction << endl;
	}

	return 0;
}