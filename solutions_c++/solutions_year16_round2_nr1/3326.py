#include <iostream>
#include <string>
#include <algorithm>
#include <iterator>
#include <vector>
#include <unordered_map>
using namespace std;

static int d[10] = {320, 226, 250, 376, 316, 298, 244, 385, 369, 298};

string digit(string& word){
	string result = "";
	string re = "";
	unordered_map<char, int> m;
	int total = 0;
	int numn = 0;
	vector<int> map(10, 0);
	for (int i = 0; i < word.size(); i++) {
		m[word[i]]++;
		total += word[i];
		if (word[i] == 'N')
			numn++;
		else if (word[i] == 'Z') {
			map[0]++;
			m['Z']--;
			m['E']--;
			m['R']--;
			m['O']--;
		}
		else if (word[i] == 'W') {
			map[2]++;
			m['T']--;
			m['W']--;
			m['O']--;
		}
		else if (word[i] == 'U') {
			map[4]++;
			m['F']--;
			m['O']--;
			m['U']--;
			m['R']--;
		}
		else if (word[i] == 'X') {
			map[6]++;
			m['S']--;
			m['I']--;
			m['X']--;
		}
		else if (word[i] == 'G') {
			map[8]++;
			m['E']--;
			m['I']--;
			m['G']--;
			m['H']--;
			m['T']--;
		}

	}

	for (int i = 0; i < 10; i++) {
		if (map[i] > 0) {
			re.append(map[i], char(48 + i));
			total -= map[i] * d[i];
		}
	}

	for (auto i = m.begin(); i != m.end(); i++) {
		if (i -> first == 'O' && m['O'] > 0) {
			re.append(m['O'], '1');
			total -= m['O'] * d[1];
			m['O'] = 0;
		}
		else if (i -> first == 'H' && m['H'] > 0) {
			re.append(m['H'], '3');
			total -= m['H'] * d[3];
			m['H'] = 0;
		}
		else if (i -> first == 'F' && m['F'] > 0) {
			re.append(m['F'], '5');
			total -= m['F'] * d[5];
			m['F'] = 0;
		}
		else if (i -> first == 'S' && m['S'] > 0) {
			re.append(m['S'], '7');
			total -= m['S'] * d[7];
			m['S'] = 0;
		}
	}

	if (total > 0) {
		re.append((total/d[9]), '9');
	}
	sort(re.begin(), re.end());
	return re;
}


int main() {
  int numCase;
  cin >> numCase;
  for (int i = 1; i <= numCase; ++i) {
		string word;
	    cin >> word;  // read n.
		cout << "Case #" << i << ": " << digit(word) <<endl;
  }
 return 0;
}