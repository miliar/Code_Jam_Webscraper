#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
	ifstream in("B-large.in");
	ofstream out("output.txt");
	int t;
	in >> t;
	for (int i = 1; i <= t; ++i){
		string s, y;
		in >> s;
		y += s[0];
		char cur = s[0];
		for (int j = 1; j < s.size(); ++j){
			if (s[j] == cur)
				continue;
			else{
				y += s[j];
				cur = s[j];
			}
		}
		if (y.back() == '+')
			y.erase(y.size() - 1);
		out << "Case #" << i << ": " << y.size() << endl;
	}
}
