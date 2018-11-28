#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include <queue>
#include <limits.h>
using namespace std;

int main() {
	int t;
	cin >> t;
	unsigned long long N, n;
	int checked = 0;
	int len = 0;
	int zerolen = 0;
	int j = 0;
	//cout<<( (1 << 10 )- 1)<<endl;
	for (int i = 1; i <= t; i++) {
		cin >> N;
		n = N;
		checked = 0;
		while (n) {
			len++;
			n /= 10;
		}
		//if(n==0)
		j = 1;
		do {
			n = j * N;
			//cout<<n<<" : "<<checked<<endl;
			zerolen = 0;
			while (n) {
				if (0 != (n % 10))
					break;
				n/=10;
				zerolen++;
			}
			n = j * N;
			while (n) {
				checked |= (1 << (n % 10));
				n /= 10;
			}
			n = j * N;
			j++;
		} while (checked !=( (1 << 10 )- 1) && zerolen < len);
		cout<<"Case #"<<i<<": ";
		if(checked !=( (1 << 10 )- 1))
			cout << "INSOMNIA" << endl;
		else
			cout << n << endl;
	}

}

//Powered by [KawigiEdit] 2.0!
