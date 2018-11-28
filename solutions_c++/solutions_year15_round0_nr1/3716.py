/*
*Nahid Hossain
*mail@akmnahid.com
*/
#include<iostream>
#include<vector>
using namespace std;

unsigned int clappingPerson=0;
unsigned int clappingFriend=0;

unsigned int result[101];

char input[1100];



//vector<int> inputs
int main(){
	int noOfTestCases;
	int smax=0;
	
	cin >> noOfTestCases;
	int n=0;
	while(n<noOfTestCases){
		cin >> smax;
		cin >> input;
		clappingPerson = 0;
		clappingFriend = 0;
		for(int i = 0; i <= smax; i++){
			int curNumber=(int)input[i] - (int) '0' ;
			
			if(curNumber!=0){
				
				if(i==0){
					clappingPerson=curNumber;
				}
				else {
					
					if(clappingPerson<i){
						clappingFriend = clappingFriend + (i-clappingPerson);
						clappingPerson+= (i-clappingPerson);
					}
						clappingPerson=clappingPerson + curNumber;
					
				}
				
			}
			//cout << i  << " : "<< curNumber << " : " << clappingPerson << " : " << clappingFriend << endl;
			
			
		}
		//cout << endl;
		//result[n] = clappingFriend;		
		n++;
	}
	
	for(int i = 0; i < noOfTestCases ; i++)
		cout << "Case #"<< (i+1) << ": " << result[i] << endl;
	return 0;
}
