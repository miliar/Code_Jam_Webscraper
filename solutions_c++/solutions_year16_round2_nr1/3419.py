#include <unordered_map>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

 static string nums[]
 	= {"ZERO", "ONE", "TWO",
 	"THREE", "FOUR", "FIVE", "SIX",
 	"SEVEN", "EIGHT", "NINE"};

 unordered_map<string, char> numMap;

 void loadNum() {
 	numMap["ZERO"] = '0';
 	numMap["ONE"] = '1';
 	numMap["TWO"] = '2';
 	numMap["THREE"] = '3';
 	numMap["FOUR"] = '4';
 	numMap["FIVE"] = '5';
 	numMap["SIX"] = '6';
 	numMap["SEVEN"] = '7';
 	numMap["EIGHT"] = '8';
 	numMap["NINE"] = '9';
 }

bool dfs(string &phoneNum, unordered_map<char, int> &charMap, int idx) {
	if (charMap.empty())
		return true;
	
	for (int nIdx = idx; nIdx >= 0; nIdx--) {
		string num = nums[nIdx];
		bool isFound = true;
		for (int i = 0; i < num.size(); i++) {
			char c = num[i];
			if (charMap.count(c) > 0) {
				charMap[c]--;
				if (charMap[c] == 0)
					charMap.erase(c);
				//cout << "true " << num << "\t" << c << endl;
			} else {
				//cout << "false " << num << "\t" << c << endl;
				isFound = false;
				while (i--)
					charMap[num[i]]++;
				break;
			}
		}
		if (!isFound)
			continue;
		if (dfs(phoneNum, charMap, nIdx)) {
			phoneNum.push_back(numMap[num]);
			return true;
		} else {
			for (char c : num) {
				charMap[c]++;
				phoneNum.pop_back();
			}
		}
	}
	return false;
}

string analyzePhoneNum(const string &letters) {
	unordered_map<char, int> charMap;
	string phone;
	for (char c : letters)
		charMap[c]++;
	dfs(phone, charMap, 9);
	//sort(phone.begin(), phone.end());
	return phone;
}


int main() {
	loadNum();
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string s;
		cin >> s;
		cout << "Case #" << t <<": " << analyzePhoneNum(s) << endl;
	}
	return 0;
}