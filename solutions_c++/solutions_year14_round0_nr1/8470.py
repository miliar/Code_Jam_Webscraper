#include <iostream>

using namespace std;

int main(){
	
	int nNumOfTestCases,nCurTestCase = 0,nFirstAnswer,nSecondAnswer, nOutput,nCount = 0;
	int arrFirst[4][4];
	int arrSecond[4][4];
	
	cin>>nNumOfTestCases;
	while(nCurTestCase < nNumOfTestCases){
	
		cin>>nFirstAnswer;
		
		for(int i = 0 ; i < 4;i++){
			for(int j =0 ; j < 4;j++){
				cin>>arrFirst[i][j];
			}
		}
		
		cin>>nSecondAnswer;
		
		for(int i = 0 ; i < 4;i++){
			for(int j =0 ; j < 4;j++){
				cin>>arrSecond[i][j];
				
				if( i == (nSecondAnswer - 1) ){
					for( int k = 0 ; k  < 4; k++){
						if(arrFirst[nFirstAnswer -  1][k] == arrSecond[i][j]){
							nCount++;
							nOutput = arrSecond[i][j];
						}
					}
				}
				
			}
		}
		
		if(nCount == 1){
			cout<<"Case #"<<nCurTestCase + 1<<": "	<<nOutput<<"\n";
		}
		else{
			if(nCount > 1){
				cout<<"Case #"<<nCurTestCase + 1<<": Bad magician!\n";
			}
			else{
				cout<<"Case #"<<nCurTestCase + 1<<": Volunteer cheated!\n";
			}
		}
		
		nCurTestCase++;
		nCount = 0;
	}
	return 0;
}
