#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <sys/time.h>
#include <string>
#include <fstream>
#include <ctime>

char testcases[5], row1[5], n1[5], n2[5], n3[5], n4[5], row2[5];
	
int T, r1, r2;
int bef[4][4];
int af[4][4];


bool readInput(){
	std::ifstream inputFile;
    	
	std::ofstream text;
    	
        inputFile.open("problem1.in");
 	
	if (!inputFile){
        	std::cout << "ERROR - File not found" << std::endl;
		return false;
    	}
	
	text.open("problem1.out");
	
	if(!text.is_open()) return false;
	
	inputFile >> testcases;
	
	T=atoi(testcases);
	
	std::cout << "T=" << T << std::endl;
	
	int count=0;
	
	for (int i=0; i<T; i++){
		inputFile >> row1;
		r1=atoi(row1);
		
		count=0;
		int card;
		
		for (int l=0; l<4; l++){
		
			inputFile >> n1 >> n2 >> n3 >> n4;
				
			bef[l][0] = atoi(n1);
			bef[l][1] = atoi(n2);
			bef[l][2] = atoi(n3);
			bef[l][3] = atoi(n4);
			
			std::cout << n1 << " " << n2 << " " << n3 << " " << n4 << std::endl;
			
		}
		
		inputFile >> row2;
		
		r2=atoi(row2);
		
		std::cout << "\n\nRows: " << r1 << "/" << r2 << std::endl;
		
		for (int l=0; l<4; l++){
		
			inputFile >> n1 >> n2 >> n3 >> n4;
				
			af[l][0] = atoi(n1);
			af[l][1] = atoi(n2);
			af[l][2] = atoi(n3);
			af[l][3] = atoi(n4);
		}
		
		for (int t=0; t<4; t++){
			for(int c=0; c<4; c++){
				std::cout << "Compare " << bef[r1-1][t] << " and " << af[r2-1][c] << std::endl;
				if(bef[r1-1][t]==af[r2-1][c]){
					count++;
					card=bef[r1-1][t];
					std::cout << "Card "<< card << "/" << af[r2-1][c]<< std::endl;
				}
			}
		}
		
		
		
		
		if(count>1)
			text << "Case #" << i+1 << ": Bad magician!";
		if(count==0)
			text << "Case #" << i+1 << ": Volunteer cheated!";
		if(count==1)
			text << "Case #" << i+1 << ": " << card;
			
		if(i!=T-1)
			text << "\n";
		
	}
	
	
        inputFile.close(); 
	text.close(); 
	

	
    	return true;
}


int main(void){

	readInput();
	
	return 1;
	
}
