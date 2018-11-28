#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

vector <int> convert_vector(string &s)
{
	vector <int> ret(26);
	int size = s.size();

	for(int i = 0; i < size; i++) {
		int index = s[i] - 'A';
		ret[index]++;
	}
	return ret;
}

bool even_is_done(vector <int> &pre_result)
{
	bool ret = true;
	if( (pre_result['Z' - 'A'] > 0) || (pre_result['W' - 'A'] > 0) \
		|| (pre_result['U' - 'A'] > 0) || (pre_result['X' - 'A'] > 0) \
		|| (pre_result['G' - 'A'] > 0) ) {
		ret = false;
	}
	return ret;
}

bool odd_is_done(vector <int> &pre_result)
{
	bool ret = true;
	if( (pre_result['O' - 'A'] > 0) || (pre_result['T' - 'A'] > 0) \
		|| (pre_result['F' - 'A'] > 0) || (pre_result['S' - 'A'] > 0) ) {
		ret = false;
	}
	return ret;
}

void get_telephone_num(string &s, int index)
{
	vector <int> result;
	vector <int> pre_result = convert_vector(s);
	
	while (even_is_done(pre_result) == false) {
		if(pre_result['Z' - 'A'] > 0) {
			result.push_back(0);
			pre_result['Z' - 'A']--;
			pre_result['E' - 'A']--;
			pre_result['R' - 'A']--;
			pre_result['O' - 'A']--;		
		}
		if(pre_result['W' - 'A'] > 0) {
			result.push_back(2);
			pre_result['T' - 'A']--;
			pre_result['W' - 'A']--;
			pre_result['O' - 'A']--;		
		}
		if(pre_result['U' - 'A'] > 0) {
			result.push_back(4);
			pre_result['F' - 'A']--;
			pre_result['O' - 'A']--;
			pre_result['U' - 'A']--;
			pre_result['R' - 'A']--;		
		}
		if(pre_result['X' - 'A'] > 0) {
			result.push_back(6);
			pre_result['S' - 'A']--;
			pre_result['I' - 'A']--;
			pre_result['X' - 'A']--;		
		}
		if(pre_result['G' - 'A'] > 0) {
			result.push_back(8);
			pre_result['E' - 'A']--;
			pre_result['I' - 'A']--;
			pre_result['G' - 'A']--;
			pre_result['H' - 'A']--;
			pre_result['T' - 'A']--;	
		}	
	}

	while (odd_is_done(pre_result) == false) {
		if(pre_result['O' - 'A'] > 0) {
			result.push_back(1);
			pre_result['O' - 'A']--;
			pre_result['N' - 'A']--;
			pre_result['E' - 'A']--;
		}
		if(pre_result['T' - 'A'] > 0) {
			result.push_back(3);
			pre_result['T' - 'A']--;
			pre_result['H' - 'A']--;
			pre_result['R' - 'A']--;
			pre_result['E' - 'A']-=2;
		}
		if(pre_result['F' - 'A'] > 0) {
			result.push_back(5);
			pre_result['F' - 'A']--;
			pre_result['I' - 'A']--;
			pre_result['V' - 'A']--;
			pre_result['E' - 'A']--;		
		}
		if(pre_result['S' - 'A'] > 0) {
			result.push_back(7);
			pre_result['S' - 'A']--;
			pre_result['E' - 'A']-=2;
			pre_result['V' - 'A']--;
			pre_result['N' - 'A']--;	
		}	
	}

	int nine_num = pre_result['N' - 'A'] / 2;

	for(int i = 0; i < nine_num; i++) {
		result.push_back(9);
	}
	sort(result.begin(), result.end());

	cout << "Case #" << (index+1) << ": ";
	for(int i = 0; i < result.size(); i++) {
		cout << result[i];
	}
	cout << endl;
}

int main(void)
{
	int N, i;
	string temp;
	cin >> N;

	for(i=0; i<N; i++) {
		cin >> temp;
		get_telephone_num(temp, i);
	}
}