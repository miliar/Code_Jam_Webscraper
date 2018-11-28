#include <iostream>

using namespace std;

int Calculate (int* a, int n) {
	int y = 0;
	int peopleClapping = 0;
	int i = 0;
	while (i <= n) {
		if (a[i] != 0) {
			if (i <= peopleClapping)
				peopleClapping += a[i];
			else {
				y += i-peopleClapping;
				peopleClapping += a[i] + i;
			}
		}
		i++;
	}
	return y;
}

void Case (int x) {
	int Smax;
	cin >> Smax;
	int* a = new int[Smax+1];
	char c;
	while ((c = cin.peek ()) < '0' || c > '9')
		c = cin.get ();
	for (int i = 0; i <= Smax; i++) {
		c = cin.get ();
		a[i] = c-'0';
	}
	cout << "Case #" << x << ": " << Calculate (a,Smax) << endl;
	delete[] a;
}

int main () {
	int cases;
	cin >> cases;
	for (int i = 0; i < cases; i++)
		Case (i+1);
}


