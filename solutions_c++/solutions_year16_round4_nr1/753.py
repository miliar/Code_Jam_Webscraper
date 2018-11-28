#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>

typedef long long ll;

using namespace std;

string recExplore(int r, int p, int s, string lineup = "") {
	if (r+p+s == 0) {
		string roundd = lineup;
		while (roundd.length() > 1) {
			//printf("%s\n", roundd.c_str());
			string temp = "";
			for (int i=0; i<(int)roundd.size(); i+=2) {
				if (roundd[i] == roundd[i+1])
					return "";
				if ((roundd[i] == 'P' and roundd[i+1] == 'S') or (roundd[i] == 'S' and roundd[i+1] == 'P'))
					temp += "S";
				if ((roundd[i] == 'P' and roundd[i+1] == 'R') or (roundd[i] == 'R' and roundd[i+1] == 'P'))
					temp += "P";
				if ((roundd[i] == 'R' and roundd[i+1] == 'S') or (roundd[i] == 'S' and roundd[i+1] == 'R'))
					temp += "R";
			}
			roundd = temp;
		}
		return lineup;
	}

	if (p > 0) {
		string temp = recExplore(r, p-1, s, lineup + "P");
		if (temp.length()>0)
			return temp;
	}

	if (r > 0) {
		string temp = recExplore(r-1, p, s, lineup + "R");
		if (temp.length()>0)
			return temp;
	}

	if (s > 0) {
		string temp = recExplore(r, p, s-1, lineup + "S");
		if (temp.length()>0)
			return temp;
	}

	return "";
}

int countStr(const string & str, char c) {
	int cnt = 0;
	for (int i=0; i<(int)str.size(); i++)
		if (str[i] == c)
			cnt ++;
	return cnt;
}

int main() {
	int iC=0, nC;
	scanf("%d", &nC);
	for (iC=1; iC<=nC; iC++) {
		int N, R, P, S;
		scanf("%d %d %d %d", &N, &R, &P, &S);

		string strP = "P", strR = "R", strS = "S";
		int l=0;
		while (l < N) {
			string nP = min(strP + strR, strR + strP);
			string nR = min(strS + strR, strR + strS);
			string nS = min(strP + strS, strS + strP);
			strP = nP;
			strR = nR;
			strS = nS;
			l++;
		}

		string best = "";
		if (countStr(strP, 'P') == P and countStr(strP, 'R') == R and countStr(strP, 'S') == S)
			if (best == "" or strP < best)
				best = strP;
		if (countStr(strR, 'P') == P and countStr(strR, 'R') == R and countStr(strR, 'S') == S)
			if (best == "" or strR < best)
				best = strR;
		if (countStr(strS, 'P') == P and countStr(strS, 'R') == R and countStr(strS, 'S') == S)
			if (best == "" or strS < best)
				best = strS;

		if (best == "")
			best = "IMPOSSIBLE";

		printf("Case #%d: %s\n", iC, best.c_str());
	}
	return 0;
}