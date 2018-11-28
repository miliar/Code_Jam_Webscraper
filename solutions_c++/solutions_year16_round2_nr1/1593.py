
#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int k, len, cnt;
	char buf[3000];
	string s;
	int arr[26];
	vector<int> result(3000);
	
	cin >> k;
	cin.getline(buf, 3000);

	for (int t = 0; t < k; t++) {
		
		for (int i = 0; i < 26; i++) {
			arr[i] = 0;
		}
		
		len = 0;
		cin.getline(buf, 3000);
		s = string(buf);
		for (size_t i = 0; i < s.length(); i++) {
			arr[(int)(s[i] - 'A')]++;
		}
		
		//ZERO
		cnt = arr[(int)('Z' - 'A')];
		for (int i = 0; i < cnt; i++) {
			result[len++] = 0;
			arr[(int)('Z' - 'A')]--;
			arr[(int)('E' - 'A')]--;
			arr[(int)('R' - 'A')]--;
			arr[(int)('O' - 'A')]--;
		}
		//SIX
		cnt = arr[(int)('X' - 'A')];
		for (int i = 0; i < cnt; i++) {
			result[len++] = 6;
			arr[(int)('S' - 'A')]--;
			arr[(int)('I' - 'A')]--;
			arr[(int)('X' - 'A')]--;
		}
		//TWO
		cnt = arr[(int)('W' - 'A')];
		for (int i = 0; i < cnt; i++) {
			result[len++] = 2;
			arr[(int)('T' - 'A')]--;
			arr[(int)('W' - 'A')]--;
			arr[(int)('O' - 'A')]--;
		}
		//FOUR
		cnt = arr[(int)('U' - 'A')];
		for (int i = 0; i < cnt; i++) {
			result[len++] = 4;
			arr[(int)('F' - 'A')]--;
			arr[(int)('O' - 'A')]--;
			arr[(int)('U' - 'A')]--;
			arr[(int)('R' - 'A')]--;
		}
		//EIGHT
		cnt = arr[(int)('G' - 'A')];
		for (int i = 0; i < cnt; i++) {
			result[len++] = 8;
			arr[(int)('E' - 'A')]--;
			arr[(int)('I' - 'A')]--;
			arr[(int)('G' - 'A')]--;
			arr[(int)('H' - 'A')]--;
			arr[(int)('T' - 'A')]--;
		}
		//FIVE
		cnt = arr[(int)('F' - 'A')];
		for (int i = 0; i < cnt; i++) {
			result[len++] = 5;
			arr[(int)('F' - 'A')]--;
			arr[(int)('I' - 'A')]--;
			arr[(int)('V' - 'A')]--;
			arr[(int)('E' - 'A')]--;
		}
		//SEVEN
		cnt = arr[(int)('V' - 'A')];
		for (int i = 0; i < cnt; i++) {
			result[len++] = 7;
			arr[(int)('S' - 'A')]--;
			arr[(int)('E' - 'A')]--;
			arr[(int)('V' - 'A')]--;
			arr[(int)('E' - 'A')]--;
			arr[(int)('N' - 'A')]--;
		}
		//ONE
		cnt = arr[(int)('O' - 'A')];
		for (int i = 0; i < cnt; i++) {
			result[len++] = 1;
			arr[(int)('O' - 'A')]--;
			arr[(int)('N' - 'A')]--;
			arr[(int)('E' - 'A')]--;
		}
		//NINE
		cnt = arr[(int)('I' - 'A')];
		for (int i = 0; i < cnt; i++) {
			result[len++] = 9;
			arr[(int)('N' - 'A')]--;
			arr[(int)('I' - 'A')]--;
			arr[(int)('N' - 'A')]--;
			arr[(int)('E' - 'A')]--;
		}
		//THREE
		cnt = arr[(int)('T' - 'A')];
		for (int i = 0; i < cnt; i++) {
			result[len++] = 3;
		}

		cout << "Case #" << t+1 << ": ";
		sort(result.begin(), result.begin()+len);
		for (int i = 0; i < len; i++) {
			cout << result[i];
		}
		cout << endl;

	}

	cin.close();
	cout.close();

	return 0;
}
