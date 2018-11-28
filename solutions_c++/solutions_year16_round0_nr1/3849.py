#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int main() {
	fstream fs;
  fs.open ("input.txt");

	int round_num, n;
	fs >> round_num;

	for(int i = 1; i < round_num+1; i++){
		fs >> n;
		cout << "Case #" << i << ": ";
		if(n==0){
			cout << "INSOMNIA" << endl;
			continue;
		}

		int kn = n;
		int tp = kn;
		vector<bool> digit(10, 0);
		for (int k = 1; find(digit.begin(), digit.end(), 0) !=  digit.end(); k++){
			kn = k*n;
			tp = kn;
			while(tp > 0){
				int d = tp % 10;
				digit[d] = 1;
				tp = tp / 10;
			}
		}
		cout << kn << endl;

	}


	fs.close();


	return 0;
}
