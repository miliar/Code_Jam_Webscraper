#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;
int main(){
	ifstream in("A-large.in");
	ofstream out("output.txt");
	int t;
	in >> t;
	for (int i = 1; i <= t; ++i){
		long long n, s = 1, o;
		in >> n;
		map<char, int> x;
		while (n != 0 && x.size() != 10){
			o = s*n;
			for (auto j : to_string(o))
				++x[j];
			++s;
		}
		out << "Case #" << i << ": " << (n ? to_string(o) : "INSOMNIA") << endl;
	}
}
