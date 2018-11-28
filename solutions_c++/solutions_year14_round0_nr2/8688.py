#include <iostream>
#include <fstream>
using namespace std;


int main () {
	
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	
	int n;
	cin >> n;
	double c,f,x;
	for (int i = 0; i < n; i++) {
		cin >> c >> f >> x;
		double f1 =2 ,t = 0,x1 = 0,x2 = 0;
		while (true) {
			x1 = x/(f1) + t;
			x2 = x/(f1 + f) + (c/f1) + t;

			if (x1 < x2) {
				cout << "Case #"<< i+1 << ": ";
				printf("%.6f", x1);
				cout  << endl;
				break;
			}
			t += (c/f1);
			f1 +=f;
		}
	}

	
	return 0;

}
