#include <iostream>
#include <string.h>
#include<stdio.h>
using namespace std;

int main(){

	int t;
	cin>>t;
	for(int j = 1; j <= t; j++){
		int maxShyness, audienceCounter = 0, friendCounter = 0, extraNeeded;
		char inputString[10];
		cin>>maxShyness;
		cin>>inputString;
		for(int i = 0; i <= maxShyness; i++){
			if(inputString[i] == '0'){
				continue;
			}
			else{
				if(i > audienceCounter){
					extraNeeded = i - audienceCounter;
					friendCounter += extraNeeded;
					audienceCounter += extraNeeded +inputString[i] - 48;
				}
				else{
					//cout<<audienceCounter<<" "<<inputString[i]<<endl;
					audienceCounter += inputString[i] - 48;
				}
			}
		}
		
		printf("Case #%d: %d\n", j,friendCounter);
		
	}	
	
return 0;
	
}
