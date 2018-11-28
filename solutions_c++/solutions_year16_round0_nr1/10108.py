#include <iostream>
#include <fstream>
#include <set>

using namespace std;

int main() {
	int n;
	ifstream fin("input.txt");
	fin >> n;
	ofstream fout("output.txt");
	long long p;
	long long count = 1;
	set<int> hash;
    long long temp = 0, x = 0;
	cout << "Test cases: " << n << "\n";
	for (int i = 0; i < n; i++) {
		fin >> p;
		if(p==0) {
		    fout<<"Case #"<<(i+1)<<": INSOMNIA"<<endl;
		    continue;
		}
		count = 1;
		hash.clear();
		while (hash.size() != 10) {
			x = p * count;
			count++;
			temp = x;
			while (temp != 0) {
				hash.insert(temp % 10);
				temp /= 10;
			}
		}
		fout<<"Case #"<<(i+1)<<": "<<x<<endl;
	}
	return 0;
}