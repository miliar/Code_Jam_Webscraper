#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	int t;

	cin >> t;
	int soluciones[t];

	for (int m = 0; m < t; ++m) {
	    int s, personas;
		soluciones[m] = 0;
	    
	    cin >> s;
		cin >> personas;

		int p[s+1];
		for (int i = s; i >= 0; i--) {
		    p[i] = personas % 10;
		    personas /= 10;
		}

		//for (int i = 0; i <= s; ++i) 
		//	cout << p[i];
	
	  	int j = 0;
	  	int h = 0;
	  	int parados = 0;

		for (int h = 0; h < s; ++h) {
		    
			parados += p[h];

			if (p[j] == 0 && parados <= j && h==j){ 
				soluciones[m]++;
				j++; 
			}
			else {
				j += p[j];
				if (j>s)
					break;
			}
		}
	}
	
	for (int k = 1; k < t+1; ++k) {
		cout << "Case #" << k << ": " << soluciones[k-1] << endl;
		    
	}
	return 0;
}