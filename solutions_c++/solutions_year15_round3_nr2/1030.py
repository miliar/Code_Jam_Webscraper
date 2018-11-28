#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

typedef long double ld;

int
gcd(int a, int b)
{
	int c;
	while (a != 0) {
		c = a; a = b%a;  b = c;
	}
	return b;
}

void getPossible(string letters,string current, int n,int max, vector<string>* total){
	if (n == max){
		total->push_back(current);
	}
	else{
		for (int i = 0; i < letters.size(); i++){
			string t = current + letters[i];
			getPossible(letters, t, n + 1,max, total);
		}
	}
}

int countTarget(string s, string t){
	int count = 0;
	for (int i = 0; i < s.size(); i++){
		string v = s.substr(i, t.size());
		if (v == t){
			count++;
		}
	}
	return count;
}

int main(){
	ifstream fin("B-small-attempt0.in");
	ofstream fout("output.txt");

	int T;
	fin >> T;
	for (int t = 1; t <= T; t++){
		int k, l, s;
		fin >> k >> l >> s;
		string keyboard, target;
		fin >> keyboard >> target;
		vector<string> p;
		getPossible(keyboard,"",0,s,&p);
		int count = 0;
		int max = 0;
		for (auto& it : p){
			int v = countTarget(it, target);
			if (v > max) max = v;
			count += v;
		}
		ld expected_give = count / (ld)p.size();
		ld start = max;
		ld expected_keep = start - expected_give;
		fout << "Case #" << t << ": " << setprecision(10) << expected_keep << endl;
	}
	fout.close();
	return 0;
}