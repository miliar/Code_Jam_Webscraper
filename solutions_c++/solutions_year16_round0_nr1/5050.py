#include<fstream>
#include<vector>
#include<unordered_set>
#include<algorithm>
using namespace std;

long numSleep(long);
int main() {

	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int T;
	fin >> T;
	long N;
	int i = 1;
	while (fin >> N) {
		long temp = numSleep(N);
		if(temp!=-1)
			fout << "Case #" << i++ << ": " << temp << endl;
		else
			fout << "Case #" << i++ << ": " << "INSOMNIA" << endl;
	}


}

long numSleep(long N) {
	unordered_set<int> digits;
	if (N == 0) return -1;
	int i = 1;
	while (digits.size() < 10) {
		long temp = N*i++;
		while (temp) {
			digits.insert(temp % 10);
			temp /= 10;
		}
	}
	return N*(i - 1);
}