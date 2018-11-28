#include <iostream>

using namespace std;

int main(){
	int T;
	int pos1, pos2;
	int mat1[4][4], mat2[4][4];
	int Tnum = 1;

	cin>>T;

	while(T--){
		int cor = 0;
		int answer;
		cin>>pos1;
		for(int i = 0; i<4; i++)
			for(int j=0; j<4; j++)
				cin>>mat1[i][j];
		cin>>pos2;
		for(int i =0; i<4; i++)
			for(int j=0; j<4; j++)
				cin>>mat2[i][j];

		for(int i =0; i<4; i++){
			for(int j =0; j<4; j++){
				if(mat1[pos1-1][i] == mat2[pos2-1][j]){
					cor++;
					answer = mat1[pos1-1][i];
				}
			}
		}

		if(cor == 0)
			cout<< "Case #"<<Tnum<<": Volunteer cheated!"<<endl;
		else if(cor == 1)
			cout<< "Case #"<<Tnum<<": "<<answer<<endl;
		else if(cor > 1)
			cout<< "Case #"<<Tnum<<": Bad magician!"<<endl;

		Tnum++;

	}
	return 0;
}