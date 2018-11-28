#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <queue>
#include <vector>
#include <set>
#include <iterator>
using namespace std;
ifstream in("A-large.in");
ofstream out("A-large.out");
int n;
int g(vector<int> a) {
	int s = 0;
	for (int i = 0; i < n; i++) {
		s += a[i];
	}
	return s;
}
int main(){
	int t;
	in >> t;
	int q = 1;
	while (q<=t) {
		string s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		in >> n;
		vector<int> a(n);
		for (int i = 0; i < n; i++) {
			in >> a[i];
		}
		out << "Case #" << q << ": ";
		cout << "Case #" << q << ": ";
		while (g(a)) {
			if (g(a) != n) {
				string str_out = "";
				int max = a[0];
				for (int i = 1; i < n; i++)
					if (max < a[i]) max = a[i];
				int q = 0;
				for (int i = 0; i < n; i++)
					if (a[i] == max) q++;
				if (q == 2) {
					for (int i = 0; i < n; i++)
						if (a[i] == max) {
							str_out += s[i];
							a[i]--;
						}
				}
				else {
					int k = 0;
					for (int i = 0; i < n&&k < 2; i++)
						if (a[i] == max) {
							str_out += s[i];
							a[i]--;
							k++;
						}
				}
				out << str_out << " ";
				cout << str_out << " ";
			}else{
				for(int i=n-1;i>1;i--)
					if (a[i] == 1) {
						cout << s[i] << " ";
						out << s[i] << " ";
						a[i]--;
					}
				cout << s[1] << s[0] << " ";
				out << s[1] << s[0] << " ";
				a[1]--;
				a[0]--;
			}
		}
		q++;
		out << endl; cout << endl;
	}
	return 0;
}