#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

inline char calculate(const string& s, const int beginIndex = 0){
	bool positive = true;
	char cur = '1';
	for (int i = beginIndex; i < s.size(); i++){
		if (cur == '1'){
			cur = s[i];
		}
		else if (cur == 'i'){
			if (s[i] == 'i'){
				positive = !positive;
				cur = '1';
			}
			else if (s[i] == 'j'){
				cur = 'k';
			}
			else if (s[i] == 'k'){
				positive = !positive;
				cur = 'j';
			}
		}
		else if (cur == 'j'){
			if (s[i] == 'i'){
				positive = !positive;
				cur = 'k';
			}
			else if (s[i] == 'j'){
				positive = !positive;
				cur = '1';
			}
			else if (s[i] == 'k'){
				cur = 'i';
			}
		}
		else if (cur == 'k'){
			if (s[i] == 'i'){
				cur = 'j';
			}
			else if (s[i] == 'j'){
				positive = !positive;
				cur = 'i';
			}
			else if (s[i] == 'k'){
				positive = !positive;
				cur = '1';
			}
		}
	}
	if (positive)
		return cur;
	else
		return '-';
}

inline void calculateIncremental(char c, bool& pos, char& cur){
	if (cur == '1'){
		cur = c;
	}
	else if (cur == 'i'){
		if (c == 'i'){
			pos = !pos;
			cur = '1';
		}
		else if (c == 'j'){
			cur = 'k';
		}
		else if (c == 'k'){
			pos = !pos;
			cur = 'j';
		}
	}
	else if (cur == 'j'){
		if (c == 'i'){
			pos = !pos;
			cur = 'k';
		}
		else if (c == 'j'){
			pos = !pos;
			cur = '1';
		}
		else if (c == 'k'){
			cur = 'i';
		}
	}
	else if (cur == 'k'){
		if (c == 'i'){
			cur = 'j';
		}
		else if (c == 'j'){
			pos = !pos;
			cur = 'i';
		}
		else if (c == 'k'){
			pos = !pos;
			cur = '1';
		}
	}
}

int main(){
	ios::sync_with_stdio(false);
	int nbTests;
	cin >> nbTests;
	for (int testNb = 1; testNb <= nbTests; testNb++){
		int L, X;
		cin >> L >> X;
		string s;
		cin >> s;
		string str;
		while (X--){
			str.append(s);
		}
		bool possible = false;
		if (str.size() >= 3){
			vector<int> eindindexendeel1; //exclusief

			bool pos = true; //positief
			char cur = '1';
			for (int i = 1; i < str.size() - 1; i++){
				calculateIncremental(str[i - 1], pos, cur);
				if (pos && cur == 'i'){
					eindindexendeel1.push_back(i);
				}
			}

			if (!eindindexendeel1.empty()){
				vector<int> beginindexendeel3;
				for (int i = str.size() - 1; i >= eindindexendeel1[0]; i--){
					if (calculate(str, i) == 'k'){
						beginindexendeel3.push_back(i);
					}
				}
				if (!beginindexendeel3.empty()){
					sort(beginindexendeel3.begin(), beginindexendeel3.end());
					
					for (int beginI : eindindexendeel1){
						pos = true;
						cur = '1';
						for (int i = beginI; i < beginindexendeel3.back(); i++){
							calculateIncremental(str[i], pos, cur);
							if (binary_search(beginindexendeel3.begin(), beginindexendeel3.end(), i+1) && pos && cur == 'j'){
								possible = true;
								break;
							}
						}
						if(possible)
							break;
					}
				}
			}
		}

		cout << "Case #" << testNb << ": " << (possible ? "YES" : "NO") << '\n';
	}
	return 0;
}