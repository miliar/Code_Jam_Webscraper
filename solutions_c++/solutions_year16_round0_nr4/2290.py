#include <cstdio>
#include <iostream>

using namespace std;



/* cheaty way to do this: in the small case
   you can just calculate where the original ones
   would be and put those ones.
*/

int main(){

	int T;
	long long K, C, S;
	long long aux;
	long long aux2;
	cin >> T;

	for (int caso = 1 ; caso <= T; caso++){

		cin >> K;
		cin >> C;
		cin >> S;

		cout << "Case #" << caso << ":";

		for (long long i = 0; i < K; i++){
			aux2 = 1;
			for (int j = 1; j < C;j++){
				aux2 *= K; 
			}
			aux = (i*aux2)  + 1;
			cout << " " << aux;
		}
		cout << endl;


	}

}