#include<fstream>
#include<vector>
#include<unordered_set>
#include<algorithm>
#include<string>
using namespace std;

int main() {

	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int T;
	fin >> T;
	int a, b, c;
	int i = 1;
	while (fin >> a>>b>>c) {
		fout << "Case #" << i++ << ": ";
		for (int i = 1; i < a; i++) fout << i<<" ";
		fout << a << endl;
	}


}
