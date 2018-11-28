#include <bits/stdc++.h>

using namespace std;

enum { R, S, P };

const char* basicEle[] = { "R", "S", "P" };

string gen_answer(int winner, int rounds)
{
    if (rounds == 0) return string(basicEle[winner]);
    string a, b;
    switch (winner) {
    case R: a = gen_answer(S, rounds - 1); b = gen_answer(R, rounds - 1); break;
    case S: a = gen_answer(P, rounds - 1); b = gen_answer(S, rounds - 1); break;
    case P: a = gen_answer(R, rounds - 1); b = gen_answer(P, rounds - 1); break;
    default: assert(false);
    }
    return min(a, b) + max(a, b);
}

bool check(const string& ans, int R, int P, int S)
{
    if (count(ans.begin(), ans.end(), 'R') != R) return false;
    if (count(ans.begin(), ans.end(), 'P') != P) return false;
    if (count(ans.begin(), ans.end(), 'S') != S) return false;
    return true;
}

int main(void)
{
    int T = 0;
    int TK = 0;
    scanf("%d", &T);
    while (T--) {
	printf("Case #%d: ", ++TK);

	int N, nR, nP, nS;
	scanf("%d %d %d %d", &N, &nR, &nP, &nS);

	string aR = gen_answer(R, N);
	string aS = gen_answer(S, N);
	string aP = gen_answer(P, N);
	//cout << aR << endl << aS << endl << aP << endl;
	string result = string(23333, 'Z');
	if (check(aR, nR, nP, nS)) result = min(aR, result);
	if (check(aS, nR, nP, nS)) result = min(aS, result);
	if (check(aP, nR, nP, nS)) result = min(aP, result);

	if (result[0] == 'Z') result = "IMPOSSIBLE";

	printf("%s\n", result.c_str());
    }
    return 0;
}