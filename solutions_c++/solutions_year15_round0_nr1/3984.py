#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
	int n = 0, index = 0, smax = 0, count = 0;
	string str("");
	//ifstream infile("A-small-attempt0.in");
	ifstream infile("A-large.in");
	ofstream outfile("A-small.out");
	streambuf *oldinbuf = cin.rdbuf(infile.rdbuf());
	streambuf *oldoutbuf = cout.rdbuf(outfile.rdbuf());
	cin >> n;
	while (index < n) {
		cin >> smax >> str;
		count = 0;
		int len = str.size(), sum = 0;
		if (str[0] - '0' == 0)
			count = 1;
		sum = str[0] - '0';
		for (int i = 1; i < len; i++) {
			int tmp = str[i] - '0';
			if (sum + count< i) {
				count += i - (sum + count);
			}
			sum += tmp;
		}

		cout << "Case #" << index + 1 << ": " << count << endl;
		index++;
	}
	cout.rdbuf(oldoutbuf);
	cin.rdbuf(oldinbuf);
	return 0;
}