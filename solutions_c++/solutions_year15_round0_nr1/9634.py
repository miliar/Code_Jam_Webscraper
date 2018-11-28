#define WU2

#include <iostream>
#include <functional>
#include <algorithm>
#include <utility>
#include <string>
#include <vector>
#include <set>
#include <map>
//#include <unordered_set>
//#include <unordered_map>

using namespace std;

typedef long long ll;




int main() {
#ifdef WU
	freopen("C://Users//wu//Desktop//in.txt", "r", stdin);
#endif
#ifdef WU2
	string file_name = "A-small-attempt0";
	freopen(("C://Users//wu//Desktop//" + file_name + ".in").c_str(), "r", stdin);
	freopen(("C://Users//wu//Desktop//" + file_name + ".out").c_str(), "w", stdout);
#endif

	int T, t = 0;
	cin >> T;

	while (T - (t++)) {
		int s_max;
		char s[1999];
		cin >> s_max;
		int num = 0;
		int addition = 0;
		for (int i = 0; i <= s_max; i++) {
			cin >> s[i];
			while (num < i){
				num++;
				addition++;
			}
			num += s[i] - '0';

		}
		cout << "Case #" << t << ": ";
		cout << addition << endl;


	}
}


