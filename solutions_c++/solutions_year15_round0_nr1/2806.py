#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int Smax;
string a;

bool test(int x)
{
	int standed = x;
	for(int i = 0; i < a.size(); ++i) {
		if(a[i] == 0 || standed >= i)
			standed += (a[i] - 48);
		else
			return false;
	}
	return true;
}

int binsearch(int start, int stop) {
	if(start == stop)
		return start;
	if(test((start+stop)/2))
		return binsearch(start, (start+stop)/2);
	return binsearch((start+stop)/2 + 1, stop);
}

void qwe(int t)
{
	cin >> Smax;
	cin >> a;
	vector<int> tab;
	int x = binsearch(0, 10000);
	cout << "Case #" << t <<  ": " << x << endl;
}

int main()
{
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int i = 1; i<= T;++i)
		qwe(i);
	return 0;
}
