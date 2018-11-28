#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <functional>
#include <queue>

using namespace std;
//i, j, k, -i, -j, -k, 1, -1
//i, j, k,  l,  m,  n, o,  p
string str;
char mat[8][8];
int cache[3][10001];
char calc(char a, char b) {
	//i, j, k, -i, -j, -k, 1, -1
	//i, j, k,  l,  m,  n, o,  p
	if (a == 'o' && b == 'o') return 'o';
	if (a == 'o' && b == 'i') return 'i';
	if (a == 'o' && b == 'j') return 'j';
	if (a == 'o' && b == 'k') return 'k';

	if (a == 'i' && b == 'o') return 'i';
	if (a == 'i' && b == 'i') return 'p';
	if (a == 'i' && b == 'j') return 'k';
	if (a == 'i' && b == 'k') return 'm';

	if (a == 'j' && b == 'o') return 'j';
	if (a == 'j' && b == 'i') return 'n';
	if (a == 'j' && b == 'j') return 'p';
	if (a == 'j' && b == 'k') return 'i';

	if (a == 'k' && b == 'o') return 'k';
	if (a == 'k' && b == 'i') return 'j';
	if (a == 'k' && b == 'j') return 'l';
	if (a == 'k' && b == 'k') return 'p';


	//i, j, k, -i, -j, -k, 1, -1
	//i, j, k,  l,  m,  n, o,  p
	if (a == 'o' && b == 'p') return 'p';
	if (a == 'o' && b == 'l') return 'l';
	if (a == 'o' && b == 'm') return 'm';
	if (a == 'o' && b == 'n') return 'n';

	if (a == 'i' && b == 'p') return 'l';
	if (a == 'i' && b == 'l') return 'o';
	if (a == 'i' && b == 'm') return 'n';
	if (a == 'i' && b == 'n') return 'j';

	if (a == 'j' && b == 'p') return 'm';//
	if (a == 'j' && b == 'l') return 'k';
	if (a == 'j' && b == 'm') return 'o';
	if (a == 'j' && b == 'n') return 'l';

	if (a == 'k' && b == 'p') return 'n';
	if (a == 'k' && b == 'l') return 'm';
	if (a == 'k' && b == 'm') return 'i';
	if (a == 'k' && b == 'n') return 'o';




	//i, j, k, -i, -j, -k, 1, -1
	//i, j, k,  l,  m,  n, o,  p
	if (a == 'p' && b == 'o') return 'p';
	if (a == 'p' && b == 'i') return 'l';
	if (a == 'p' && b == 'j') return 'm';
	if (a == 'p' && b == 'k') return 'n';

	if (a == 'l' && b == 'o') return 'l';
	if (a == 'l' && b == 'i') return 'o';
	if (a == 'l' && b == 'j') return 'n';
	if (a == 'l' && b == 'k') return 'j';

	if (a == 'm' && b == 'o') return 'm';
	if (a == 'm' && b == 'i') return 'k';
	if (a == 'm' && b == 'j') return 'o';
	if (a == 'm' && b == 'k') return 'l';

	if (a == 'n' && b == 'o') return 'n';
	if (a == 'n' && b == 'i') return 'm';
	if (a == 'n' && b == 'j') return 'i';
	if (a == 'n' && b == 'k') return 'o';


	//i, j, k, -i, -j, -k, 1, -1
	//i, j, k,  l,  m,  n, o,  p
	if (a == 'p' && b == 'p') return 'o';
	if (a == 'p' && b == 'l') return 'i';
	if (a == 'p' && b == 'm') return 'j';
	if (a == 'p' && b == 'n') return 'k';

	if (a == 'l' && b == 'p') return 'i';
	if (a == 'l' && b == 'l') return 'p';
	if (a == 'l' && b == 'm') return 'k';
	if (a == 'l' && b == 'n') return 'm';

	if (a == 'm' && b == 'p') return 'j';
	if (a == 'm' && b == 'l') return 'n';
	if (a == 'm' && b == 'm') return 'p';
	if (a == 'm' && b == 'n') return 'i';

	if (a == 'n' && b == 'p') return 'k';
	if (a == 'n' && b == 'l') return 'j';
	if (a == 'n' && b == 'm') return 'l';
	if (a == 'n' && b == 'n') return 'p';
}
bool recur(char ijk, int index) {
	if (ijk == 'l') {	//모두 완성된 경우
		if (index == str.size()) return true;
		else return false;
	}
	if (index == str.size()) return false;
	int& ret = cache[ijk - 'i'][index];
	if (ret != -1) {
		if (ret == 0)
			return false;
		else if (ret == 1)
			return true;
	}
	char cur = str[index];
	for (int i = index; i < str.size(); ++i) {
		if (i != index)
			//cur = calc(cur, str[i]);
			cur = mat[cur - 'i'][str[i] - 'i'];
		if (cur == ijk) {
			bool check = recur(ijk + 1, i + 1);
			if (check == true) {
				ret = 1;
				return true;
			}
		}
	}
	ret = 0;
	return false;
}

void preCalc() {
	for (int i = 0; i < 8; ++i)
		for (int j = 0; j < 8; ++j)
			mat[i][j] = calc('i' + i, 'i' + j);
}
void main() {
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);
	//freopen("input2.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	preCalc();
	int nCase;
	cin >> nCase;
	for (int cc = 0; cc < nCase; ++cc) {
		memset(cache, -1, sizeof(cache));
		int L, mul;

		string X;
		str = "";
		cin >> L >> mul >> X;
		for (int i = 0; i < mul; ++i) {
			str += X;
		}
		//str = "jijijijijiji";
		bool check = recur('i', 0);
		if (check)
			cout << "Case #" << cc + 1 << ": " << "YES" << endl;
		else
			cout << "Case #" << cc + 1 << ": " << "NO" << endl;
	}
}