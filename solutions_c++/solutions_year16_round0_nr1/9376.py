#include <iostream>
#include <fstream>
using namespace std;

long long int answer(int n)
{
	bool found[10] = {false};
	bool ans = true;
	long long int curr = n, temp;

	while(1) {
		temp = curr;
		while (temp) {
			found[temp%10] = true;
			temp = temp/10;
		}
		ans = true;
		for (int i=0; i<10; ++i) {
			ans = ans & found[i];
		}
		if (ans) {
			return curr;
		}
		curr += n;
	}
	return 0;
}

int main()
{
	int t, n, tnum=1;
	ifstream infile("in.txt");
	ofstream outfile("out.txt");
	infile >> t;
	while (tnum <= t) {
		outfile << "Case #" << tnum << ": ";
		infile >> n;
		if (n == 0) {
			outfile << "INSOMNIA" << endl;
		} else {
			outfile << answer(n) << endl;
		}
		++tnum;
	}
	outfile.close();
	//  test
//		for (int i=1; i<1000001;  ++i) {
//			cout << i << ": " << answer(i) << endl;
//		}
	return 0;
}
