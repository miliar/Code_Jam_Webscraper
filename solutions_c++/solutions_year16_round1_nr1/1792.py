#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

string lastwd(string &org)
{
	string dst;
	for(int i=0; org[i]; ++i) {
		string pre = org[i] + dst;
		string post = dst + org[i];
		if ( pre < post )
			dst = post;
		else
			dst = pre;
	}
	return dst;
}

int main()
{
	int tcase;
	string org;

	cin >> tcase;

	for (int i=1; i<=tcase; ++i) {
		cin >> org;
		cout << "Case #" << i << ": " << lastwd(org) << endl;
	}
	return 0;
}
