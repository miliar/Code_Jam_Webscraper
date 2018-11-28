#include <iostream>
using namespace std;


int main(int argc, char* argv[]){
	int n,m;
	int cases;
	bool found = true;

	cin >> cases;

	for(int i=0;i<cases;i++){
		cin >> n >> m;

		int numbers[n][m];
		int numbers2[n][m];
		
		//init second lawn to 0
		for(int j=0;j<n;j++){
			for(int k=0;k<m;k++){
				numbers2[j][k]=0;
				//cout<< numbers2[j][k];
			}
			//cout << endl;
		}
		//cout << endl;
		//find the largest h of each row
		for(int j=0;j<n;j++){
			for(int k=0;k<m;k++){
				cin >> numbers[j][k];
				if(numbers[j][k]>numbers2[j][0])
					numbers2[j][0]=numbers[j][k];

				//cout << numbers2[j][k];
			}
			//cout << endl;
		}

		
		//init each row with the largest h
		for(int j=0;j<n;j++){
			for(int k=0;k<m;k++){
				numbers2[j][k]=numbers2[j][0];
				//out << numbers2[j][k];
			}
			//cout << endl;
		}

		for(int j=0;j<n;j++){
			for(int k=0;k<m;k++){
				if(numbers[j][k]<numbers2[j][k]){
					
					for(int l=0;l<n;l++){
						numbers2[l][k] = numbers[j][k];
					}

				}
			}
			
		}

		for(int j=0;j<n;j++){
			for(int k=0;k<m;k++){
				if(numbers[j][k] != numbers2[j][k])
					found = false;
			}
		}
		

		if(found){
			cout << "Case #"<<i+1<<": YES"<< endl;
		}
		else
			cout << "Case #"<<i+1<<": NO" << endl;


		found = true;




	}



}