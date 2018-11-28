#include <iostream>
using namespace std;

int earlyCards[4][4];
int lateCards[4][4];

int answerQ1, answerQ2;

int nCases;

void printCards(){
	for( int i=0; i<4; i++){
			for( int j= 0; j<4; j++){
				cout<<earlyCards[i][j]<<" ";
			}
			cout<<endl;
		}
		
	for( int i=0; i<4; i++){
			for( int j= 0; j<4; j++){
				cout<<lateCards[i][j]<<" ";
			}
			cout<<endl;
		}
}
int main(){
	cin>>nCases;
	int index = 1;
	
	while( nCases -- ){
		cin>>answerQ1;
		for( int i=0; i<4; i++){
			for( int j= 0; j<4; j++){
				cin>>earlyCards[i][j];
			}
		}
		cin>>answerQ2;
		for( int i=0; i<4; i++){
			for( int j= 0; j<4; j++){
				cin>>lateCards[i][j];
			}
		}
	
		//printCards();
		
		int count = 0;
		int cardNumber = -1;
		for( int i=0; i<4; i++){
			for( int j=0; j<4; j++){
				if( earlyCards[answerQ1-1][i] == lateCards[answerQ2-1][j]){
				    count++;
				    cardNumber = earlyCards[answerQ1-1][i];
				}
			}
		}
		
		cout<<"Case #"<<index<<": ";
		if( count == 1)
			cout<<cardNumber<<endl;
		else if( count > 1)
			cout<<"Bad magician!"<<endl;
		else if( count == 0)
			cout<<"Volunteer cheated!"<<endl;
		index++;
		
	}
	
	return 0;
	
}
