#include<cstdio>
#include<iostream>
#include<string>
#include<map>

using namespace std;

map<int, char> map_unique_char = {
    {0, 'Z'}, {2, 'W'}, {4, 'U'}, {5, 'F'}, {6, 'X'}, {7, 'S'}, {8, 'G'}, {9, 'I'}, {3, 'T'}, {1, 'O'}
};

map<int, string> map_number_string = {
	{0, "ZERO"}, {1, "ONE"}, {2, "TWO"}, {3, "THREE"}, {4, "FOUR"}, {5, "FIVE"}, {6, "SIX"}, {7, "SEVEN"}, {8, "EIGHT"}, {9, "NINE"}
};

void write_case(int c) {
	cout << "Case #" << to_string(c) << ": ";
}

pair<int, string> find_count_of(int number, string s) {
	int count = 0;
	for (auto c: s) {
		if (c == map_unique_char[number]) {
			count++;
		}
	}
	for (int i = 0; i < count; i++) {
		for (auto c: map_number_string[number]) {
			for (int i = 0; i < (int)s.size(); i++) {
				if (s[i] == c) {
//					cout << "we erase symbol " << i;
					s.erase(i, 1);
//					cout << " and get " << s << endl;
					break;
				}
			}
		}
	}
	return (make_pair(count, s));
}

int number[10];

int main()
{
	freopen("a.txt", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int t;
	scanf("%d", &t);
	for (int j = 0; j < t; j++) {
		write_case(j + 1);
		string s;
		cin >> s;
		for (int i = 0; i < 10; i++) {
			if (i != 3 and i != 1) {
//				cout << "before handle " << i << " we have string " << s << endl;
				pair<int, string> res = find_count_of(i, s);
				s = res.second;
//				cout << "after handle " << i << " we get string " << s << endl;
				number[i] = res.first;
			}
		}
		pair<int, string> res_3 = find_count_of(3, s);
		s = res_3.second;
		number[3] = res_3.first;
		pair<int, string> res_1 = find_count_of(1, s);
		s = res_1.second;
		number[1] = res_1.first;
		if (s != "") {
//			cout << s << endl;
			throw;
		}
		for (int i = 0; i < 10; i++) {
			for (int l = 0; l < number[i]; l++) {
				cout << i;
			}
		} 
		for (int i = 0; i < 10; i++) {
			number[i] = 0;
		} 
		cout << endl;
	}

	return 0;
}
