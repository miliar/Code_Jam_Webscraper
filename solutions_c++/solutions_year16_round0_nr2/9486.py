#include <iostream>
#include <fstream>
using namespace std;

string str;

int answer(int len, bool neg)
{
	if (len == 0) {
		return 0;
	}
	if (len == 1) {
		if (str[0] == '-') {
			if (neg) {
				return 0;
			} else {
				return 1;
			}
		} else {
			if (neg) {
				return 1;
			} else {
				return 0;
			}
		}
	}
	if (str[len-1] == '-') {
		if (!neg) {
			return min(answer(len-1, true)+1, answer(len-1, false)+2);
		} else {
			return answer(len-1, neg);
		}
	} else {
		if (!neg) {
			return answer(len-1, neg);
		} else {
			return min(answer(len-1, true)+2, answer(len-1, false)+1);
		}
	}
}

int main()
{
	int t, tnum=1;
	ifstream infile("in.txt");
	ofstream outfile("out.txt");
	infile >> t;
	while (tnum <= t) {
		outfile << "Case #" << tnum << ": ";
		infile >> str;
		outfile << answer(str.size(), false) << endl;
		++tnum;
	}
	outfile.close();
	//  test
//		for (int i=1; i<1000001;  ++i) {
//			cout << i << ": " << answer(i) << endl;
//		}
	return 0;
}
