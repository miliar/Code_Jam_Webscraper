#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <cmath>
#include <fstream>

using namespace std;

int main ()
{
	ifstream fin("A-small-attempt2.in");
	ofstream fout("MagicResults.txt");
	
	if(!fin){
		cout<<"Unable to open file";
		cin.get();
		return EXIT_FAILURE;
	}
	
	int tests;
	int rowTemp[4];
	int rowTemp2[4];
		
	fin>>tests;
	
	for (int i = 0; i<tests; i++){
		int random = 0;
		int rowNum;
		fin>>rowNum;
		int ind = 0;
		for(int j = 0; j<16; j++){
			
			if((j/4+1)==rowNum){
				fin>>rowTemp[ind];
				ind++;
			}	
			else
				fin>>random;			
		}
		
		int rowNum2;
		fin>>rowNum2;
		ind  = 0;
		
		for (int j = 0; j<16; j++){
			
			if(j/4+1==rowNum2){
				fin>>rowTemp2[ind];
				ind++;
			}
			else
				fin>>random;
		}
		
		int same = 0;
		int card = 0;
		
		for(int k = 0; k<4;k++){
			if(same>1)
				break;
			
			for(int l = 0; l<4; l++){
				
				if(same>1)
					break;
				
				if(rowTemp[k]==rowTemp2[l]){
					same++;
					card = rowTemp[k];
					
				}
				
				
			}			
		
		}
		
		fout<<"Case #"<<i+1<<": ";
		
		if(same==1)
			fout<<card;
		else if(same==0)
			fout<<"Volunteer cheated!";
		else
			fout<<"Bad magician!";		
		fout<<endl;
	}
	
	return 0;
	
}
