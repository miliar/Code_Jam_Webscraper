#include <bits/stdc++.h>

using namespace std;

int main(){
	int T , temp , r1 , r2 , f , fst[4][4] , snd[4][4];
	cin >> T;
	ofstream cout;
	cout.open("outputFile.txt");
	for(int t = 1 ; t <= T ; t++){
		cin >> r1;
		for(int i = 0 ; i < 4 ; i++){
			for(int j = 0 ; j < 4 ; j++){
				cin >> fst[i][j];
			}
		}
		cin >> r2;
		for(int i = 0 ; i < 4 ; i++){
			for(int j = 0 ; j < 4 ; j++){
				cin >> snd[i][j];
			}
		}
		f = 0;
		r1--;
		r2--;
		for(int i = 0 ; i < 4 && f!= -1 ; i++){
			for(int j = 0 ; j < 4 && f!= -1 ; j++){
				if(fst[r1][i] == snd[r2][j]){
					if(!f)
						f = fst[r1][i];
					else
						f = -1;
				}
			}
		}

		if(!f)
			cout<<"Case #"<<t<<": Volunteer cheated!"<<endl;
		else if(f == -1)
			cout<<"Case #"<<t<<": Bad magician!"<<endl;
		else
			cout<<"Case #"<<t<<": "<<f<<endl;
	}
	cout.close();
	return 0;
}
