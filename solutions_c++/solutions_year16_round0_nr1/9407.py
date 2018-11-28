#include <iostream>
#include <fstream>
#include <array>
#include <set>

using namespace std;

bool containsAll(const array<bool, 10>& arr) {
	for(bool b : arr) {
		if(!b){
			return b;
		}
	}
	return true;
}

int main() {
	array<bool, 10> digits;
	ofstream out;
	ifstream in;

	const string name = "large";

	out.open(name+".out");
	in.open(name+".in");

	int T;
	in >> T;

	for(int i = 1; i <= T;i++) {
		digits.fill(false);
		bool flag = false;
		int N, work;
		in >> N;
		work = N;
		set<int> done;
		done.insert(N);
		out << "CASE #" << i << ": ";
		while(!containsAll(digits)) {
			int temp = work;
			while(temp) {
				digits[temp % 10] = true;
				temp = temp / 10;
			}
			work += N;
			pair<set<int>::iterator, bool> ret = done.insert(work);
			if(!ret.second) {
				out << "INSOMNIA\n";
				flag = true;
				break;
			}
		}
		if(!flag)
			out << work-N << endl;
		flag = false;
	}
}