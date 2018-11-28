#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <deque>


using namespace std;


int main(){
	ifstream f("date.in");
	ofstream g("date.out");

	int T;
	f >> T;
	for (int t = 1; t <= T; ++t){
		deque <char> Q;
		string s;
		f >> s;

		Q.push_back(s[0]);
		for (int i = 1; i < s.size(); ++i)
			if (s[i] >= Q.front())
				Q.push_front(s[i]);
			else
				Q.push_back(s[i]);

		g << "Case #" << t << ": ";
		while (!Q.empty()){
			g << Q.front();
			Q.pop_front();
		}
		g << "\n";
	}
	f.close();
	g.close();

	return 0;
}