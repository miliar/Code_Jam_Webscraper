#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string result[100];

void convert_win_string(string &s, int index)
{
	string ret;
	int len = s.length();
	ret += s[0];

	for(int i = 1; i < len; i++) {
		if(ret[0] <= s[i]) {
			ret.insert(0, 1, s[i]);
		} else {
			ret += s[i];
		}
	}
	result[index] = ret;
}

int main(void)
{
	int N, i;
	string temp;
	cin >> N;

	for(i=0; i<N; i++) {
		cin >> temp;
		convert_win_string(temp, i);
	}
	for(i=0; i<N; i++) {
		cout << "Case #" << (i+1) << ": ";
		cout << result[i] << endl;
	}
}