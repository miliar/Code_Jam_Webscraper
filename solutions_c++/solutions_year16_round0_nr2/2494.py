#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string minimize_string(string &s)
{
	string ret;
	int len = s.length(), i;
	for(i = len - 1; i >=0 ; i--) {
		if(s[i] =='-') {
			break;
		}
	}
	if(i < len - 1) {
		ret = s.substr(0, i + 1);
	} else {
		ret = s;
	}
	return ret;
}

int find_char_length(string &s, char ch)
{
	int str_len = s.length();
	int i;
	for(i = 0; (i < str_len) && (s[i] == ch); i++) {
		;
	}

	return (i);
}

string flip_string(string &s, int len)
{
	string ret;
	int str_len = s.length();
	for(int i = len - 1; i >=0 ; i--) {
		if(s[i] =='-') {
			ret += '+';
		} else {
			ret += '-';
		}
	}
	if(len < str_len) {
		ret += s.substr(len, str_len - len);
	}
	return ret;
}

int get_flip_min(string &s)
{
	int ret = 0, length;
	string temp = minimize_string(s);

	while (temp.length() > 0) {
		if(temp[0] == '+') {
			length = find_char_length(temp, '+');
			temp = flip_string(temp, length);
			ret++;
		}
		temp = flip_string(temp, temp.length());
		ret++;
		temp = minimize_string(temp);
	}
	return ret;
}

int main(void)
{
	int N, i;
	int test[100];
	string temp;
	cin >> N;

	for(i=0; i<N; i++) {
		cin >> temp;
		test[i] = get_flip_min(temp);
	}
	for(i=0; i<N; i++) {
		cout << "Case #" << (i+1) << ": ";
		cout << test[i] << endl;
	}
}