#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
	ifstream in("D-small-attempt0.in");
	ofstream out("output.txt");
	int t;
	in >> t;
	for (int i = 1; i <= t; ++i){
		int k, c, s;
		in >> k >> c >> s;
		out << "Case #" << i << ": ";
		for (int j = 1; j <= k; ++j)
			out << j << ' ';
		out << endl;
	}
}
