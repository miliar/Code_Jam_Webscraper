#include<fstream>
#include<vector>
#include<string>
using namespace std;

int find(string& s, string num, char iden) {
	int count =0;
	for (int i=0; i < s.size(); i++)
		if (s[i] == iden) count++;
	for (int i=0; i < num.size(); i++) {
		int pos = 0;
		for (int j=0; j < count; j++) {
			pos = s.find(num[i], pos);
			s.erase(pos, 1);
		}
	}
	return count;
}

int main()
{
	int T;
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	fin >> T;
	for (int i=0; i < T; i++) {
		string s;
		fin >> s;
		vector<int> v(10);
		v[0] = find(s, "ZERO", 'Z');
		v[2] = find(s, "TWO", 'W');
		v[4] = find(s, "FOUR", 'U');
		v[6] = find(s, "SIX", 'X');
		v[5] = find(s, "FIVE", 'F');
		v[7] = find(s, "SEVEN", 'V');
		v[3] = find(s, "THREE", 'R');
		v[1] = find(s, "ONE", 'O');
		v[8] = find(s, "EIGHT", 'G');
		v[9] = s.length()/4;
		fout << "Case #" << i+1 << ": ";
		for (int j=0; j < v.size(); j++)
			for(int k=0; k < v[j]; k++)
				fout << j;
		fout << endl;
	}
}

