#include <iostream>
#include <vector>
using namespace std;

int solve(string s){
	int result = 0;
	for (int i = 0; i < s.size(); i++){
		if (i > 0 && s[i -1 ] != s[i])
			result++;

		if (i == s.size() - 1 && s[i] == '-')
			result++;
	}
	return result;
	
}
int main(int argc, char **argv)
{
	int test_cnt = 0;
	vector<string> strings;
        scanf("%d", &test_cnt);
	string s;
	getline(cin, s);
	for (int i = 0; i < test_cnt; i++){
		getline(cin, s);
		strings.push_back(s);
	}
        for (int i = 0; i < test_cnt; i++){
		int cnt = solve(strings[i]);
		cout << "Case #"<<i+1<< ": "<< cnt << endl;
	}
	return 0;
}

