#include <iostream>
#include <fstream>

using namespace std;

int main(){

	ifstream fin("A-small-attemptA-2014.in");
	ofstream fout("A-small-attemptA-2014.out");

	int dataNumber;
	fin>>dataNumber;
	
	for(int i=1;i<=dataNumber;i++){
		int rowFirst;
		int rowSecond;
		int m[4];
		fin>>rowFirst;
		int junk;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				if(j==rowFirst-1){
					fin>>m[k];
				}else{
					fin>>junk;
				}
			}
		}
		fin>>rowSecond;
		int candidate;
		int count = 0;
		int value = 0;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				if(j==rowSecond-1){
					fin>>candidate;
					for(int l=0;l<4;l++){
						if(candidate == m[l]){
							value = candidate;
							count++;
						}
					}
				}else{
					fin>>junk;
				}
			}
		}
		fout<<"Case #"<<i<<": ";
		if(count == 0){
			fout<<"Volunteer cheated!";
		}
		if(count == 1){
			fout<<value;
		}
		if(count > 1){
			fout<<"Bad magician!";
		}
		fout<<endl;
	}
}