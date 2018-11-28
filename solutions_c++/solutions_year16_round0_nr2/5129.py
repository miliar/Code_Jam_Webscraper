#include<fstream>
#include<vector>
#include<unordered_set>
#include<algorithm>
#include<string>
using namespace std;

int numFlips(vector<bool>&,int);
int main() {

	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int T;
	fin >> T;
	string s;
	int i = 1;
	while (fin >> s) {
		vector<bool> temp;
		for (int i = 0; i < s.size(); i++) temp.push_back((s[i] == '+' ? 1 : 0));
		int res = numFlips(temp,0);
		fout << "Case #" << i++ << ": " << res << endl;
	}


}

bool allOne(vector<bool> &inp) {
	for (int i = 0; i < inp.size(); i++) {
		if (!inp[i]) return 0;
	}
	return 1;
}

int firstZeroFromBot(vector<bool> &inp) {
	for (int i = inp.size()-1; i >=0; i--) {
		if (!inp[i]) return i;
	}
	return 0;
}

int firstOneFromTop(vector<bool> &inp) {
	for (int i = 1; i < inp.size(); i++) {
		if (inp[i])continue;
		else return i - 1;
	}
	return 0;
}

void flip(vector<bool> &inp, int end) {
	for (int i = 0; i <= end; i++){
		inp[i] = !inp[i];
	}
	reverse(inp.begin(), inp.begin() + end+1);
}


int numFlips(vector<bool> &inp, int num) {
		if (allOne(inp)) return num;

	if (inp[0] == 0) {
		int b = firstZeroFromBot(inp);
		flip(inp, b);
	}
	else {
		int b = firstOneFromTop(inp);
		int c = firstZeroFromBot(inp);
		
		if (c < b) {
			flip(inp, 0);
		}
		else {
			flip(inp, b);
		}
	}
	return numFlips(inp, num + 1);
}