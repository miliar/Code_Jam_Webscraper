#include <fstream>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <functional>

using namespace std;

int mp[4][4] = {
	{1,2,3,4},
	{2,-1,4,-3},
	{3,-4,-1,2},
	{4,3,-2,-1}
};

int z(char a){
	if (a == '1') return 1;
	if (a == 'i') return 2;
	if (a == 'j') return 3;
	if (a == 'k') return 4;
}

int main(){
	ios_base::sync_with_stdio(false);
	ifstream inf("C-large.in");
	ofstream outf("outputCbig.txt");
	int t, l;
	long long x;
	string s, res;
	inf >> t;
	for (int k = 0; k < t; ++k){
		inf >> l >> x;
		res = "";
		inf >> s;
		for (int i = 0; i < min(1ll*10, x); ++i) res += s;
		int ost = 0;
		if (x > 10) ost = int((x - 10) % (1ll*4));
		for (int i = 0; i < ost; ++i) res += s;
		int ans = 1, ind = -1;
		bool sign = true;
		for (int i = 0; i < (int)res.size(); ++i){
			ans = mp[ans - 1][z(res[i]) - 1];
			if (ans < 0) ans = -ans, sign = !sign;
			if (sign && ans == 2){
				ind = i;
				break;
			}
		}
		if (ans != 2 || !sign){
			outf << "Case #" << k + 1 << ": " << "NO\n";
			continue;
		}
		sign = true, ans = 1;
		for (int i = ind + 1; i < (int)res.size(); ++i){
			ans = mp[ans - 1][z(res[i]) - 1];
			if (ans < 0) ans = -ans, sign = !sign;
			if (sign && ans == 3){
				ind = i;
				break;
			}
		}
		if (ans != 3 || !sign){
			outf << "Case #" << k + 1 << ": " << "NO\n";
			continue;
		}
		sign = true, ans = 1;
		for (int i = ind + 1; i < (int)res.size(); ++i){
			ans = mp[ans - 1][z(res[i]) - 1];
			if (ans < 0) ans = -ans, sign = !sign;
		}
		if (ans == 4 && sign)
			outf << "Case #" << k + 1 << ": " << "YES\n";
		else
			outf << "Case #" << k + 1 << ": " << "NO\n";
	}
}