#include <fstream>
using namespace std;

int main(){
	ifstream cin;
	ofstream cout;

	cin.open("B-small-attempt0.in");
	cout.open("QR2_Soutput.txt");

	int N;
	cin >> N;
	for(int n=0 ; n<N ; n++){
		int H, W;
		cin >> H >> W;
		int *col = new int [W];
		int *row = new int [H];


		int **sq = new int *[H];
		for(int i=0 ; i<H ; i++){
			sq[i] = new int [W];
			for(int j=0 ; j<W ; j++){
				cin >> sq[i][j];
				if(sq[i][j] == 2){
					row[i] = 2;
					col[j] = 2;
				}
			}
		}

		bool poss = true;
		for(int i=0 ; i<H ; i++){
			for(int j=0 ; j<W ; j++){
				if(sq[i][j] == 1){
					if(!(row[i] != 2 || col[j]!=2)){
						poss = false;
						break;
					}
				}
			}
		}
		cout << "Case #" << n+1 << ": " << ((poss)? "YES":"NO") << endl;
	}
	cin.close();
	cout.close();
}