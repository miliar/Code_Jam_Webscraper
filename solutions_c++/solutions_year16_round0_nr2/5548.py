#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;



int main(){
	ifstream f("date.in");
	ofstream g("date.out");

	int T;
	f >> T;

	for (int t = 1; t <= T; ++t){
		string s;
		f >> s;
		int pasi = 0;

		while (s.size()){
			int m = 0;

			while (m < s.size() && s[m] == '+')
				m++;
			if (m > 0 && m < s.size())
				pasi++;

			while (m < s.size() && s[m] == '-')
				m++;
			if (s[m - 1] == '-')
				pasi++;

			int p = s.size() - 1;
			while (p >= 0 && s[p] == '+')
				p--;

			string s1;
			for (int i = p; i >= m; --i){
				if (s[i] == '+')
					s1.push_back('-');
				else
					s1.push_back('+');
			}
			s = s1;
		}
		g << "Case #" << t << ": " << pasi << "\n";
	}

	f.close();
	g.close();

	return 0;
}
