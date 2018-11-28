#include<iostream>
#include<fstream>
using namespace std;


int main()
{
	int numTestCases;
	int row1, row2;
	cin>>numTestCases;
	
	for(int i = 0; i < numTestCases; i++){
			
			//Read Row number
			cin>>row1;
			int j = 1;
			int arr1[4];
			//Read corresponding Row
			while(j <= 4){
				int garbage;
				if(j != row1){
					for(int k = 0; k < 4; k++){
					
						cin>>garbage;
					}
				}
				else{
					for(int k = 0; k < 4; k++){
					
						cin>>arr1[k];
					}
				}
				j++;
			}
			//arr1 has the corresponding rows
			
			
			//Read row number
			cin>>row2;
			j = 1;
			int arr2[4];
			//Read corresponding Row
			while(j <= 4){
				int garbage;
				if(j != row2){
					for(int k = 0; k < 4; k++){
						cin>>garbage;
					}
				}
				else{
					for(int k = 0; k < 4; k++){
						cin>>arr2[k];
					}
				}
				
				j++;
			}
			//arr2 has the corresponding rows
			
			int valueMatched = 0;
			int counterFlag = 0;
			for(int m = 0; m < 4; m++){
				for(int n = 0; n < 4; n++){
					if(arr1[m] == arr2[n]){
						valueMatched = arr1[m];
						counterFlag++;	
					}	
				}
			}
		
			if(counterFlag == 0){
				cout<<"Case #"<<(i+1)<<": Volunteer cheated!\n";	
				
			}
			else if(counterFlag == 1){
				cout<<"Case #"<<(i+1)<<": "<<valueMatched<<"\n";	
			}
			else{
				cout<<"Case #"<<(i+1)<<": Bad magician!\n";	
				
			}
		}
	
	
	
	return 0;
	
	
}
