#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
#include <fstream>
#include <tuple>
#include <map>

typedef long long ll;

const ll maxS = 4096;

// N R P
int ok[13][maxS][maxS] = {0};

void fill()
{
	ok[0][1][0] = ok[0][0][1] = ok[0][0][0] = true;
	for (int N = 1; N < 13; ++N)
	{
		int Np = N - 1;
		for (int R = 0; R <= (1 << Np); ++R)
		{
			for (int P = 0; R + P <= (1 << Np); ++P)
			{
				int S = (1 << Np) - P - R;
				if (ok[Np][R][P])
				{
					ok[N][P + R][P + S] = true;
				}
			}
		}
	}
}


std::string bb[13][3];

bool fill2()
{
	bb[0][0] = "R";
	bb[0][1] = "P";
	bb[0][2] = "S";
	for (int i = 1; i < 13; ++i)
	{
		auto pR = bb[i - 1][0],
		     pP = bb[i - 1][1],
		     pS = bb[i - 1][2];
		auto R1 = pR + pS,
			 R2 = pS + pR;
		bb[i][0] = R1 < R2 ? R1 : R2;
		auto P1 = pR + pP,
			 P2 = pP + pR;
		bb[i][1] = P1 < P2 ? P1 : P2;
		auto S1 = pP + pS,
			 S2 = pS + pP;
		bb[i][2] = S1 < S2 ? S1 : S2;
	}
}

bool check(std::string& s, int R, int P, int S)
{
	std::map<char, int> cnt;
	for (auto& c: s)
		cnt[c]++;
	if (R == cnt['R'] && P == cnt['P'] && S == cnt['S'])
		return true;
	return false;
}



bool play(const std::string &s)
{
	if (s.size() == 1)
		return true;
	std::string prev;
	prev.resize(s.size() / 2);
	for (int i = 0; i < s.size(); i += 2)
	{
		if (s[i] == s[i + 1])
			return false;
		int R = 0, P = 0, S = 0;
		if (s[i] == 'R') R++;
		if (s[i+1] == 'R') R++;
		if (s[i] == 'S') S++;
		if (s[i+1] == 'S') S++;
		if (s[i] == 'P') P++;
		if (s[i+1] == 'P') P++;
		
		if (R == 1 && P == 1)
			prev[i / 2] = 'P';
		if (S == 1 && P == 1)
			prev[i / 2] = 'S';
		if (R == 1 && S == 1)
			prev[i / 2] = 'R';
	}
	return play(prev);
}

int main(int argc, char **argv)
{
	ll N, R, P, S;
	fill();
	fill2();

	int T;

	std::ifstream ifs;
	std::ofstream ofs;
	ifs.open(argv[1], std::ios_base::in);
	ofs.open(argv[2], std::ios_base::out);

	ifs >> T;
	for (int i = 1; i <= T; ++i)
	{
		ifs >> N >> R >> P >> S;
		ofs << "Case #" << i << ": ";
		if (!ok[N][R][P])
		{
			ofs << "IMPOSSIBLE" << std::endl;
			continue;
		}
		std::vector<std::string> pos;
		for (int iii = 0; iii < 3; ++iii)
			if (check(bb[N][iii], R, P, S))
				pos.push_back(bb[N][iii]);
		std::sort(pos.begin(), pos.end());
		ofs << pos[0] << std::endl;
	}
	return 0;
}
