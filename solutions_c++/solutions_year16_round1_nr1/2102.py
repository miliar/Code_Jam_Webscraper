#include<iostream>
#include<vector>
#include<fstream>
#include<sstream>
#include<deque>
using namespace std;
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int testCount = 0;
	scanf("%d", &testCount);
	for (int i = 0; i < testCount; i++) {
		char word[1001];
		scanf("%s", word);
		int len = strlen(word);
		deque<char>res;
		for (int j = 0; j < len; j++) {
			if (res.empty())res.push_back(word[j]);
			else if (res.front() > word[j])res.push_back(word[j]);
			else res.push_front(word[j]);
		}
		ostringstream ostr;
		for (auto c : res)ostr << c;
		cout << "Case #" << (i + 1) << ": " << ostr.str() << endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}