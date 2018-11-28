#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int a[7]  = {0, 1, 4, 9, 121, 484};
int T;
void OPEN() {
    freopen("thefile.txt","r",stdin);
    freopen("output.txt","w",stdout);
}
int main() {
	OPEN();
	cin >> T;
	for (int i=0; i<T; i++) {
		int A, B;
		cin >> A >> B;
		int count = 0;
		for (int j=0; j<7; j++) {
			if (a[j]>=A && a[j]<=B) count++;
		}
		cout << "Case #" << i+1 << ": " << count << endl;
	}
	
	return 0;
}