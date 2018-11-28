#include <iostream>
#include <string>
using namespace std;

int main() {

    	int n, i, j, k;
	cin >> n;
	string aux("");
	for (i = 0; i < n; i++) {	
		int ch[100];
		cin >> aux;
		int result = 0;
		for (j = 0; j < aux.size(); j++) {
			if (aux[j] == '+')
				ch[j] = 1;
			else ch[j] = 0;
		}
		for (j = aux.size()-1; j >= 0; j--) {
			if (ch[j] == 1)	continue;
			result++;
			for (k = 0; k <= j; k++) {
				ch[k] = (ch[k]+1)%2;
			}
		}
		cout << "Case #" << i+1 << ": " << result << endl;
	}
}
