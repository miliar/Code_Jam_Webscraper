#include<iostream>
#include<fstream>
using namespace std;

int main(void){
	int T,N;
	int grid[4][4];
	int tmp[4];
	ifstream cin("A-small-attempt0.in");
	ofstream cout("2014_gcj_qr_A.out");
	cin >> T;
	for(int i = 0; i < T; i++){
		cin >> N;
		for(int j = 0;j < 4; j++)
			for(int k = 0; k < 4; k++)
				cin >> grid[j][k];
		for(int j = 0; j < 4; j++)
			tmp[j] = grid[N-1][j];
		cin >> N;
		for(int j = 0;j < 4; j++)
			for(int k = 0; k < 4; k++)
				cin >> grid[j][k];
		int count = 0;
		int key = 0;
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				if(tmp[j] == grid[N-1][k]){count++;key = tmp[j];};
			}
		}
		cout << "Case #"<<(i+1)<<": ";
		switch(count){
		case 0:{cout << "Volunteer cheated!" << endl;break;}
		case 1:{cout << key << endl;break;}
		default:{cout << "Bad magician!"<< endl;break;}
		}
		count = 0;
	}
	system("pause");
}