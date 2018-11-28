#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <unordered_map>

using namespace std;

template <class AnswerType>
void PrintAnswerToTestCase(size_t caseNumber, AnswerType ans)
{
	cerr << "Case #" << caseNumber << endl;
	cout << "Case #" << caseNumber << ": " << ans << endl;
}

string Rec(char move, int depth) {
    if (depth == 0) {
        return string(1, move);
    }
    string first;
    string second;
    if (move == 'P') {
        first = Rec('R', depth - 1);
        second = Rec('P', depth - 1);
    }
    if (move == 'R') {
        first = Rec('R', depth - 1);
        second = Rec('S', depth - 1);
    }
    if (move == 'S') {
        first = Rec('S', depth - 1);
        second = Rec('P', depth - 1);
    }
    if (first <= second) {
        return first + second;
    }
    return second + first;

}

string SolveTestCase() {
    int n, cr, cp, cs;
    cin >> n >> cr >> cp >> cs;
    string moves = "PRS";
    string res = "IMPOSSIBLE";
    for (char move : moves) {
        string cur = Rec(move, n);
        int tp = 0;
        int tr = 0;
        int ts = 0;
        for (char ch : cur) {
            if (ch == 'P') {
                tp++;
            }
            if (ch == 'R') {
                tr++;
            }
            if (ch == 'S') {
                ts++;
            }
        }
        if (cp == tp && cs == ts && cr == tr) {
            if (res == "IMPOSSIBLE" || res > cur) {
                res = cur;
            }
        }
    }
    return res;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("small.in", "r", stdin);
	freopen("large.in", "r", stdin);

	freopen("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++)
		PrintAnswerToTestCase(caseNumber, SolveTestCase() );

	return 0;
}