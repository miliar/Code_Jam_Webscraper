#include <iostream>
#include <string>
#include <set>

using namespace std;
class Solution {
public:
	void findLastWord(string lwstr, int pos, string curstr, set<string> &lwset) {
		if (pos == 0) {
			findLastWord(lwstr, pos + 1, lwstr.substr(pos, 1), lwset);
		}
		else if(pos < lwstr.size()){
			string newStr = curstr;
			newStr.append(lwstr.substr(pos, 1));
			findLastWord(lwstr, pos + 1, newStr, lwset);
			newStr.clear();
			newStr = lwstr.substr(pos, 1);
			newStr.append(curstr);
			findLastWord(lwstr, pos + 1, newStr, lwset);
		}
		else {
			if (!curstr.empty())
			lwset.insert(curstr);
		}
	}
};
void readInput() {
	int t;
	string lastWordString;
	set<string> lastWordSet;
	int pos;

	cin >> t;
	for (int i = 1; i <= t; ++i) {
		Solution s;
		lastWordString.clear();
		lastWordSet.clear();
		cin >> lastWordString;  // read n
		s.findLastWord(lastWordString, 0, "", lastWordSet);
		set<string>::iterator it = lastWordSet.end();

		cout << "Case #" << i << ": " << *(--it)  << endl;
	}
}
int main(int argc, char *argv[]) {
	readInput();
}