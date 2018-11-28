#include <iostream>
#include <cstdlib> // for atoi
using namespace std;
int main(){
int testCase;
int rowOne;
int rowTwo;
int marker;
int cardVal;
int cardArray [4][4];
int cardRowOne [4];
int cardRowTwo [4];

cin>> testCase;
for(int i=1;i<=testCase;i++){

cin>>rowOne;

cin>>cardArray[0][0]>>cardArray[0][1]>>cardArray[0][2]>>cardArray[0][3];
cin>>cardArray[1][0]>>cardArray[1][1]>>cardArray[1][2]>>cardArray[1][3];
cin>>cardArray[2][0]>>cardArray[2][1]>>cardArray[2][2]>>cardArray[2][3];
cin>>cardArray[3][0]>>cardArray[3][1]>>cardArray[3][2]>>cardArray[3][3];
for(int m = 0; m<=3;m++){
	cardRowOne[m]=cardArray[rowOne-1][m];
}

cin>>rowTwo;

cin>>cardArray[0][0]>>cardArray[0][1]>>cardArray[0][2]>>cardArray[0][3];
cin>>cardArray[1][0]>>cardArray[1][1]>>cardArray[1][2]>>cardArray[1][3];
cin>>cardArray[2][0]>>cardArray[2][1]>>cardArray[2][2]>>cardArray[2][3];
cin>>cardArray[3][0]>>cardArray[3][1]>>cardArray[3][2]>>cardArray[3][3];
for(int n = 0; n<=3;n++){
	cardRowTwo[n]=cardArray[rowTwo-1][n];
}


for(int j = 0; j<=3; j++){
	for(int k = 0; k<=3; k++){
		
		if(cardRowOne[j] == cardRowTwo[k]){
			marker++;
			cardVal = cardRowOne[j];
		}
	}
}


if(marker == 0){
	cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
}else if (marker == 1){

	cout<<"Case #"<<i<<": "<<cardVal<<endl;
	
}else{
	cout<<"Case #"<<i<<": Bad Magician!"<<endl;
}
marker=0;
}

return 0;
}
