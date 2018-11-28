#include <iostream>
using namespace std;

int min(int a, int b){
	return (a < b) ? a : b;
}

int main(int, char**){
	long int t, i, x, r, c;
	bool flag;

	cin >> t;
	for(i = 1; i <= t; i++){
		cin >> x >> r >> c;
		flag = false;
		if( (r * c) % x != 0)
			flag = true;
		else {
			switch(x){
				case 3:
					if(r == 1 || c == 1)
						flag = true;
				break;
				case 4:
					if(r <= 2 || c <= 2)
						flag = true;
				break;
			}
		}
		if(flag)
			cout << "Case #" << i << ": RICHARD" << endl;
		else
			cout << "Case #" << i << ": GABRIEL" << endl;
	}
}