#include <iostream>
#include <string>
using namespace std;

int main() {

    	int n, nr, i, k;
	cin >> n;
	string aux("");
	for (i = 0; i < n; i++) {
		cin >> nr;
		int j = 1;
		int v[10] = {0};
		if (nr == 0) {
			aux = "INSOMNIA";
			goto end;
		}
		while (true) {	
			aux = to_string((nr*j));
			for (k = 0; k < aux.size(); k++) {
				v[aux[k]-'0'] = 1;
			}
			int sum = 0;
			for (k=0; k<10; k++) {
				sum += v[k];
			}
			if (sum == 10) break;
			j++;
		}
end:
			cout << "Case #" << i+1 << ": " << aux << endl;
	}
}
