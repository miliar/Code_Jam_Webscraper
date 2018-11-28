/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
 * Created By : Vishwas Tripathi 
 * CSE, MNNIT-ALLAHABAD 
 * vishfrnds@gmail.com
 _._._._._._._._._._._._._._._._._._._._._.*/


#include <iostream>
using namespace std;

#define chk(a) cerr << endl << #a << " : " << a << endl
#define chk2(a,b) cerr << endl << #a << " : " << a << "\t" << #b << " : " << b << endl
#define chk3(a,b,c) cerr << endl << #a << " : " << a << "\t" << #b << " : " << b << "\t" << #c << " : " << c << endl
#define chk4(a,b,c,d) cerr << endl << #a << " : " << a << "\t" << #b << " : " << b << "\t" << #c << " : " << c << "\t" << #d << " : " << d << endl

int main()
{
	int t;
	cin >> t;
	for (int testCase = 1; testCase <= t; testCase++) {
		int smax, x, cur = 0, ans = 0;
		string str;
		cin >> smax >> str;
		for (int i = 0; i < str.length(); i++) {
			x = str[i] - '0';
			if (i <= cur) {
				cur += x;
			}
			else {
				ans += i - cur;
				cur = i + x;
			}
		}
		cout << "Case #" << testCase << ": "  << ans << "\n";
	}
    return 0;
}
