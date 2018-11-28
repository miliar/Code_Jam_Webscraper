#include <iostream>
#include <fstream>
using namespace std;
#define SIZE 100
#define FILE "B-small-attempt1.in"


struct {
	int height[SIZE][SIZE];
	int N,M;
}lawn;

int main(){
	int no;
	bool boolean;
	ifstream input;
	ofstream output;
	input.open(FILE, ios::in);
	output.open("output.out", ios::out);

	input>>no;
	for(int k=0;k<no;k++){
		boolean= true;
		input>> lawn.N;
		input>> lawn.M;
		for(int i=0;i<lawn.N;i++)
			for(int j=0;j<lawn.M;j++)
				input>> lawn.height[i][j];
				
		for(int i=0;i<lawn.N;i++){
			int max=0;
			for(int j= 0; j<lawn.M; j++){
				if (max < lawn.height[i][j])
					max= lawn.height[i][j];
			}
			lawn.height[i][lawn.M]= max;
		}
		for(int j=0;j<lawn.M;j++){
			int max=0;
			for(int i= 0; i<lawn.N; i++){
				if (max < lawn.height[i][j])
					max= lawn.height[i][j];
			}
			lawn.height[lawn.N][j]= max;
		}
		for(int i=0;i<lawn.N;i++)
			for(int j=0; j<lawn.M; j++)
				if(lawn.height[i][j]<lawn.height[i][lawn.M])
					if(lawn.height[i][j]!=lawn.height[lawn.N][j]){
						boolean= false;
					}
		for(int j=0; j<lawn.M; j++)
			for(int i=0;i<lawn.N;i++)
				if(lawn.height[i][j]<lawn.height[lawn.N][j])
					if(lawn.height[i][j]!=lawn.height[i][lawn.M]){
						boolean= false;
					}
		output<< "Case #" << k+1<< ": ";
		if(boolean)
			output<< "YES"<< endl;
		else
			output<< "NO"<< endl;
	}

	system("pause");
	return 0;

}