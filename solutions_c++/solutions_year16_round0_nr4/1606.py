#include <iostream>
using namespace std;

int main() {
	int tc,tst;
	cin >> tst;
	for(tc=1 ; tc<=tst ; ++tc)
	{
		int i,k,c,s;
		cin >> k >> c >> s;
		cout << "Case #" << tc << ":";
		for(i=1 ; i<=s ; ++i)
			cout << " " << i;
		cout << endl;
	}
	return 0;
}
