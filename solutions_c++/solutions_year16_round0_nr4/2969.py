#include <fstream>
#include <iterator>
#include <string>

using namespace std;

int main () {
	ifstream fin ("input.txt");
	ofstream fout ("output.txt");

	int T;
   	fin >> T;
   	for (int t = 0; t < T; t++) {
   		int k, c, s;
   		fin >> k >> c >> s;
   		fout << "Case #" << t + 1 << ": ";
   		for (int i = 1; i < k; i++)
   			fout << i << " ";
   		fout << k << endl; 
   	}

    fin.close ();
    fout.close ();
    return 0;
}
