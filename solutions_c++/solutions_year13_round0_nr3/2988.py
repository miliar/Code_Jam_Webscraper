#include <fstream>
#include <vector>

using namespace std;

vector<int> digits;

bool is_palindrome(long long x) 
{
	if(!x)
		return false;

	digits.clear();
	while(x) {
		digits.push_back(x % 10);
		x /= 10;
	}

	int len = digits.size();
	for(int i = 0; i < len / 2; ++i) {
		if(digits[i] != digits[len - i - 1])
			return false;
	}

	return true;
}

int main()
{
	ifstream in("C-small-attempt0.in");
	ofstream out("out.txt");

	vector<int> tenth_power;
	tenth_power.push_back(1);
	for(int i = 0; i < 10; ++i)
		tenth_power.push_back(10 * tenth_power[i]);

	int k;
	in >> k;

	vector<vector<long long>> coeff(8);
	coeff[0].push_back(0);
	coeff[1].push_back(1);
	coeff[2].push_back(11);
	coeff[3].push_back(10); coeff[3].push_back(101); 
	coeff[4].push_back(110); coeff[4].push_back(1001); 
	coeff[5].push_back(100); coeff[5].push_back(1010); coeff[5].push_back(10001); 
	coeff[6].push_back(1100); coeff[6].push_back(10010); coeff[6].push_back(100001); 
	coeff[7].push_back(1000); coeff[7].push_back(10100); coeff[7].push_back(100010); coeff[7].push_back(1000001); 

	vector<long long> cc;
	vector<long long> dd;
	for(int i = 1; i <= 4; ++i) {
		for(int pp = tenth_power[i-1]; pp < tenth_power[i]; ++pp) {
			dd.clear();
			int x = pp;
			while(x) {
				dd.push_back(x % 10);
				x /= 10;
			}

			long long cand1 = 0, cand2 = 0;

			for(int abc = 0; abc < dd.size(); ++abc) {
				cand1 += dd[abc] * coeff[2*i-1][abc];

				if(i != 4)
					cand2 += dd[abc] * coeff[2*i][abc];
			}

			cand1 *= cand1;
			cand2 *= cand2;

			if(is_palindrome(cand1))
				cc.push_back(cand1);
			if(is_palindrome(cand2))
				cc.push_back(cand2);
		}
	}

	for(int p = 1; p <= k; ++p) {
		int a, b;
		in >> a >> b;

		int ans = 0;

		for(int i = 0; i < cc.size(); ++i) {
			if(cc[i] >= a && cc[i] <= b) {
				++ans;
			}
		}

		out << "Case #" << p << ": " << ans << endl;
	}

	system("pause");
	return 0;
}

/*

*/
