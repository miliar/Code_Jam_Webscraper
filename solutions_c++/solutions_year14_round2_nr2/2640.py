#include <iostream>
#include <fstream>
#include <algorithm>
#include <limits.h>
#include <vector>
#include <iomanip>

using namespace std;

ifstream input;

int main () {

	input.open("input.txt");
	FILE* fp = fopen( "output.txt", "w" );

	int lenght = 0;
	input>>lenght;

	// Analizza i vari casi
	for (int i = 0; i < lenght; i++) {

		int A,B,K, cont = 0;

		input>>A;
		input>>B;
		input>>K;

		for (int o=0; o<A; o++) {
			for (int j=0; j<B; j++) {

				int AND = o&j;

				if (AND < K) {
					cont++;
				}
			}
		}

		fprintf(fp, "Case #%d: %d\n", i+1, cont); // Case #1: 10
		//cout<<"Case #"<<i+1<<": "<<fixed<<setprecision(7)<<best_time<<endl;
		cout<<"A: "<<A<<" B: "<<B<<" K: "<<K<<endl;
		cout<<" Cases: "<<cont<<endl;
	}

	fclose(fp);
}

