#include <iostream>
#include <string>

using namespace std;


int main(){

	int T;

	cin >> T;
	int casi = 1;
	while (T--){

		int friends = 0;
		int sMax;
		cin >> sMax;
		string data;
		cin >> data;
		int reached = data[0] %48;

		int pos = 1;
		

		while (reached < sMax){

			if (data[pos] > 0){

				 if (reached < pos){
					int temp = 0;
					temp = pos - reached;
					reached += temp;
					friends += temp;
					reached += data[pos] % 48;
				}
				 else{
					 reached += data[pos] % 48;
				 }

			}

			pos++;


		}
		cout << "Case #" << casi++ << ": " << friends << endl;


	}


	return 0;
}