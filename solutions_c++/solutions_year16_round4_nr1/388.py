// run: $exec < a-large.in > a-large.out
#include <iostream>
#include <string>

int n, r, p, s;

bool ok(std::string const& str)
{
	int tr = 0, tp = 0, ts = 0;
	for (auto ch : str)
		if (ch == 'R') tr++;
		else if (ch == 'P') tp++;
		else ts++;
	return (r == tr && s == ts && p == tp);
}

std::string back(std::string str, int d)
{
	if (d == 0) return str;
	std::string ret = str;
	if (ret[0] == 'P') {
		std::string t1 = back("P", d - 1);
		std::string t2 = back("R", d - 1);
		if (t1 + t2 < t2 + t1) return t1 + t2;
		else return t2 + t1;
	} else if (ret[0] == 'R') {
		std::string t1 = back("S", d - 1);
		std::string t2 = back("R", d - 1);
		if (t1 + t2 < t2 + t1) return t1 + t2;
		else return t2 + t1;
	} else {
		std::string t1 = back("S", d - 1);
		std::string t2 = back("P", d - 1);
		if (t1 + t2 < t2 + t1) return t1 + t2;
		else return t2 + t1;
	}
}

int main()
{
	int T; std::cin >> T;
	for (int ti = 1; ti <= T; ti++) {
		std::cout << "Case #" << ti << ": ";
		std::cin >> n >> r >> p >> s;
		std::string t1 = back("R", n);
		std::string t2 = back("P", n);
		std::string t3 = back("S", n);
		std::string ans(1 << n, 'z');
		if (ok(t1)) ans = std::min(ans, t1);
		if (ok(t2)) ans = std::min(ans, t2);
		if (ok(t3)) ans = std::min(ans, t3);
		if (ans[0] == 'z') std::cout << "IMPOSSIBLE\n";
		else std::cout << ans << '\n';
	}
}

