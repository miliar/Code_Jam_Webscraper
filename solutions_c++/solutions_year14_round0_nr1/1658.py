#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int T, nCase = 1;

int input()
{
	int bits = 0;
	int line;
	int tmp;
	
	cin >> line;
	for (int i=0;i<4;++i) {
		for (int j=0;j<4;++j) {
			cin >> tmp;
			if (i+1 == line) bits |= (1<<tmp);
		}
	}
	return bits;
}

string solve(int A, int B)
{
	int R = (A&B);
	if (R==0)
		return "Volunteer cheated!";
	
	int lsb = (R&-R);
	if (R!=lsb)
		return "Bad magician!";
	
	for (int i=1;i<=16;++i)
		if (lsb == (1<<i)) {
			R = i;
			break;
		}
	ostringstream oss;
	oss << R;
	return oss.str();
}

int main()
{
	cin >> T;
	while (T--) {
		int first = input();
		int second = input();
		
		cout << "Case #" << nCase ++ << ": " << solve(first, second) << endl;
	}
	return 0;
}