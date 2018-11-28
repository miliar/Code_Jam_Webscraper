#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream infile("B-small-attempt0.in");
	//ifstream infile("A-large.in");
	ofstream outfile("B-small.out");
	streambuf *oldinbuf = cin.rdbuf(infile.rdbuf());
	streambuf *oldoutbuf = cout.rdbuf(outfile.rdbuf());
	int n = 0,num = 0, maxres = 0, index = 0;
	cin >> n;
	while (index < n) {
		cin >> num;
		int *pans = new int[num];
		maxres = 0;
		for (int i = 0; i < num; i++) {
			cin >> pans[i];
			if (maxres < pans[i])
				maxres = pans[i];
		}
		int totaltime = 0;
		for (int i = 2; i <= maxres; i++) {
			totaltime = 0;
			for (int j = 0; j < num; j++) {
				if (pans[j] <= i)
					continue;
				totaltime += (pans[j] - 1) / i;
			}
			if (totaltime + i < minres)
				minres = totaltime + i;
		}

		delete []pans;

		cout << "Case #" << index + 1 << ": " << minres << endl;
		index++;
	}
	cout.rdbuf(oldoutbuf);
	cin.rdbuf(oldinbuf);
	return 0;
}