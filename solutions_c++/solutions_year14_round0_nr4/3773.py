#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


// key word : general harmonic progression ,  Digamma function
int main(){
	int T;
	int i,j,k;

	int N;

	cin >> T;

	for (i=1;i<=T;i++){
		cin >> N;

		vector<double> Naomi(N);

		for (j=0;j<N;j++){
			cin >> Naomi[j];
		}

		vector<double> Ken(N);
		for (j=0;j<N;j++){
			cin >> Ken[j];
		}

		sort(Naomi.begin(), Naomi.end());
		sort(Ken.begin(), Ken.end());

		int Deceitful = 0;

		for (j=0,k=0;j<N && k < N;){
			if (Naomi[j] > Ken[k]){
				Deceitful++;
				j++;
				k++;
			}else{
				j++;
			}
		}

		int Ken_War = 0;

		for (j=0,k=0;j<N && k < N;){
			if (Ken[j] > Naomi[k]){
				Ken_War++;
				j++;
				k++;
			}else{
				j++;
			}
		}

		
		cout << "Case #" << i <<": " << Deceitful << " " << N-Ken_War << endl;
	}
}
