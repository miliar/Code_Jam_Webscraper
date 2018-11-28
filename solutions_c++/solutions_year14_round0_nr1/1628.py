#include <iostream>
#include <fstream>
using namespace std;
int main(void){
	ofstream fout("A-small-attemp1.out");
	ifstream fin("A-small-attempt1.in");
	unsigned T;
	fin >> T;
	bool flag[16];
	for (unsigned t=1; t<=T; t++){
		int cnt = 0;
		int last= 0;
		for (int i=0; i<16; i++)
			flag[i] = false;
		int m, a;
		fin >> m; 
		for (int i=1; i<=4; i++)
			for (int j=0; j<4; j++){
				fin>>a;
				if (i==m){
					flag[a-1] = true;
				}
			}
		fin >> m; 
		for (int i=1; i<=4; i++)
			for (int j=0; j<4; j++){
				fin>>a;
				if (i==m && flag[a-1]){
					cnt++;
					last = a;
				}
			} 
		if (cnt==0)
			fout<<"Case #"<<t<<": Volunteer cheated!"<<endl;
		else if (cnt>1)
			fout<<"Case #"<<t<<": Bad magician!" << endl;
		else fout<<"Case #"<<t<<": "<<last<<endl;
	}
	fin.close();
	fout.close();
}
