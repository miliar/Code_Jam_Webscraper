#include <iostream>
#include <fstream>
#include <set>
using namespace std;

ifstream fin("A.in");
ofstream fout("A.out");

int T;
long long N;

int main()
{
	fin >> T;
	for(int i = 1; i <= T; i++) {
		fin >> N;
		fout << "Case #" << i << ": ";
		if(N == 0) {
			fout << "INSOMNIA\n";
			continue;
		}
		set<char> s;
		int mult = 1;
		long long num;
		while(s.size() != 10) {
			num = N * mult;
			string str = to_string(num);
			for(int j = 0; j < str.length(); j++) {
				s.insert(str[j]);
			}
			mult++;
		}
		fout << num << "\n";
	}
	return 0;
}