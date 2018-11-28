#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int t,sm,sa;
	int d[1000];
	string inp;
	cin >> t;
	for(int i=1;i<=t;i++){
		cin >> sm >> inp;
		cout << "Case #" << i << ": ";
      		int sn = inp[0]-'0';
		sa = 0;
		for(int j=1; j <= sm; j++){
			d[j] = inp[j] - '0';
			if (sn < j) {
				sa += (j - sn);
				sn += (j-sn); 
			}
			sn += d[j];
		}
		cout << sa << endl;
	}
}

