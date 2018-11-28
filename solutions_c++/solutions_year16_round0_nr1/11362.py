#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main() {

	vector<int> v ;
	vector<int> r ;
	r.assign(10,1);


	//ifstream inFile ("note.txt");

	int N = 0;


	cin >> N;


/* for (int i=0 ; i<10 ; i++){

cout << v[i] << "  " << i << "  " << r[i] << endl;

}


*/

	for (int i=1 ; i<=N; i++){

		int Atual = 0;
		int cont = 0;
		int sum =0;
		int Mult ;
		int part;
		int result = 0;
		v.assign(10,0);

		cin >> Atual;
		sum = Atual;

		if (Atual != 0){

			result = 1;

			while (v!=r){


				sum = Atual * result;
				Mult = sum;
				while ( Mult!= 0) {

				part = Mult%10;

				 if (v[part] == 0){

							v[part] = 1;

						      }
							Mult = Mult/10;

					}
					result += 1;
				}
			}




		cout << "Case #" << i << ": ";

		if (result==0){
			cout << "INSOMNIA" << endl;

		}else {

			cout << sum << endl;
		}
	}

	return 0;
}
