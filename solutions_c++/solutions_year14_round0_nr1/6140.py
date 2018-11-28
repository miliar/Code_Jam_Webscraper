#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;


#define tin fin
#define tout fout

#define MAX 17
int cards[MAX];

int main(){

	int testC,number,row1,row2,caseN=1;
	
	ifstream fin("asmall.in");
	ofstream fout("aout.out");
	
	tin>>testC;
	while(testC--){
		memset(cards,0,sizeof(cards));
		tin>>row1;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				tin>>number;
				if(i==row1-1){
					cards[number]++;
				}
			}
		}
		tin>>row2;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				tin>>number;
				if(i==row2-1){
					cards[number]++;
				}
			}
		}
		
		
		//find the one that has count==2
		int chosen=-1;
		
		for(int i=1;i<17;i++){
			if(chosen==-1 && cards[i]==2){
				chosen=i;
			}
			else if(chosen!=-1 && cards[i]==2){
				chosen=-2; // bad magician
			}
		}		
		
		if(chosen==-1) //volunteer cheated, none was in both rows
			tout<<"Case #"<<caseN++<<": Volunteer cheated!"<<endl;
		else if(chosen==-2)
			tout<<"Case #"<<caseN++<<": Bad magician!"<<endl;
		else
			tout<<"Case #"<<caseN++<<": "<<chosen<<endl;
	}









	return 0;
}
