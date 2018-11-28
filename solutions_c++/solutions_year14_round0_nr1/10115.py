#include <iostream>
using namespace std;

int main(){


	int a;

	cin >> a;

	int i, j, k;
	int card1[4][4],card2[4][4],n1,n2;
	int magic[100];

	for (k = 0; k < a; k++){
		cin >> n1;
		for (i = 0; i < 4; i++){
			for (j = 0; j < 4; j++){

				cin >> card1[i][j];

			}
		}

		cin >> n2;
		for (i = 0; i < 4; i++){
			for (j = 0; j < 4; j++){

				cin >> card2[i][j];

			}
		}

		int count = 0;
		int num;

		for (i = 0; i < 4; i++){
			for (j = 0; j < 4; j++){

				if (card1[n1 -1][i] == card2[n2 -1][j]){
					count++;
					num = card1[n1-1][i];
				}

			}
		}

		if (count == 1){
			magic[k] = num;
		}
		else
		{
			if (count == 0){
				magic[k] = -1;
			}
			else
			{
				magic[k] = -2;
			}
		}




	}

	for (i = 0; i < a; i++){
		if (magic[i]==-1)
			cout << "Case #" << i + 1 << ": " << "Volunteer cheated!" << endl;
		else{
			if (magic[i]==-2)
				cout << "Case #" << i + 1 << ": " << "Bad magician!" << endl;
			else
				cout <<"Case #"<<i+1<<": "<< magic[i] << endl;
		}
		

	}

	
	int p;
	while (1){
		cin >> p;
		if (p == 1) break;
	}

	



}