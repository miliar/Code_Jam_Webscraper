
#include "iostream"

using namespace std;
void hashh(int t[] , int k) {
	while (k != 0) {
		t[k % 10] = 1;
		k = k / 10;
	}
}
bool all(int t[]) {
	int f = 0;
	for (int i = 0; i < 10; i++) {
		if (t[i] == 1) {
			f++;
		}
	}
	return f == 10;
}
int main()
{
	int t, n = 1 , k , array[10];
	cin >> t;

	for (int i = 1; i <t+1; i++) {
		for (int j = 0; j < 10; j++)
			array[j] = 0;
		cin >> k;
		if (k == 0) {
			cout << "Case #" << i << ": INSOMNIA" << endl;
		}
		else {
			n = 1;
			while(!all(array)){
				hashh(array, k*n);
				n++;
			}
			cout << "Case #" << i <<": " << k*(n-1) << endl;
		}
	}
	return 0;
}

