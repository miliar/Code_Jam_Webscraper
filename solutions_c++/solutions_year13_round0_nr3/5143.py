#include <iostream>
#include <cmath>
#include <sstream>
#include <string>
#include <climits>

using namespace std;


long long int arrr[100];

bool palin(unsigned long long int l)
{
	unsigned long long int Number;
	Number = l;

//	string String = static_cast<ostringstream*>( &(ostringstream() << Number) )->str();
	unsigned long long int j;
	string String = "";
	while (l) {
		String += (l % 10 + '0');
		l = l / 10;
	}
	for(unsigned long long int i = 0, j = (String.size() - 1); i <= (String.size()/2); i++,--j){
		if(String[i] != String[j]) {
			return false;
		}
	}
	return true;
}

int main()
{
	long long int t;
	long long int min, max;
	min = 2;
	long long int l = 1;

	t = 10000000;
	arrr[0] = 1;
	int c = 1;
	for(long long int xi = 2; xi < t; xi++) {
        	long long int min = xi * xi;
		if (palin(min) && palin(xi)) {
			arrr[c++] = min;
		}

	}
	cin >> t;
	long long int a;
	long long int b;
	int counter;
	while (t--) {
		counter = 0;
		cin >> a >> b;
		for (int j = 0; j < c; j++) {
			if (arrr[j] >= a && arrr[j] <= b) {
				counter++;
			}
		}

		cout << "Case #" << l << ": " << counter << endl;
		l++;
	}

}
