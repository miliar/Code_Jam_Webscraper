#include <iostream>

using namespace std;

int main(){
	int T;int casenum=1, tempans,temp;
	cin>>T;
	
	char A[4][4], AX[4][4], AO[4][4];

	while(T!=0){

		int i,j; int ans=0;// 1 if game is not completed // 2 if X won // 3 if O won
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				char in;				
				cin>>in;
				A[i][j]=in;
				AX[i][j]=in;
				AO[i][j]=in;				
				int temp;
				temp=in;
				if(temp==84){AX[i][j]='X';AO[i][j]='O';}
				
				if(temp==46){ans=1;}
			}
		}	

		/////////////////////	
		for(i=0;i<4;i++){
			tempans=1; temp= A[i][0];
			for(j=0;j<4;j++){
				int temp1 = A[i][j];
				tempans *= (temp==temp1);
			}
			if (tempans==1 && temp == 88){ans=2;}
			if (tempans==1 && temp == 79){ans=3;}
		}
		if(!(ans==2 || ans==3)){
		for(j=0;j<4;j++){
			tempans=1; temp= A[0][j];
			for(i=0;i<4;i++){
				int temp1 = A[i][j];
				tempans *= (temp==temp1);
			}
			if (tempans==1 && temp == 88){ans=2;}
			if (tempans==1 && temp == 79){ans=3;}
		}
		}

		if(!(ans==2 || ans==3)){		
		tempans=1; temp= A[0][0];
		for(i=0,j=0;i<4,j<4;i++,j++){
			int temp1 = A[i][j];
			tempans *= (temp==temp1);
		}
		if (tempans==1 && temp == 88){ans=2;}
		if (tempans==1 && temp == 79){ans=3;}
		}

		if(!(ans==2 || ans==3)){
		tempans=1; temp= A[3][0];
		for(i=3,j=0;i>=0,j<4;i--,j++){
			int temp1 = A[i][j];
			tempans *= (temp==temp1);
		}
		if (tempans==1 && temp == 88){ans=2;}
		if (tempans==1 && temp == 79){ans=3;}		
		}
		/////////////////////////////

		if(!(ans==2 || ans==3)){

			for(i=0;i<4;i++){
			tempans=1; temp= AX[i][0];
			for(j=0;j<4;j++){
				int temp1 = AX[i][j];
				tempans *= (temp==temp1);
			}
			if (tempans==1 && temp == 88){ans=2;}
			if (tempans==1 && temp == 79){ans=3;}
		}
		if(!(ans==2 || ans==3)){
		for(j=0;j<4;j++){
			tempans=1; temp= AX[0][j];
			for(i=0;i<4;i++){
				int temp1 = AX[i][j];
				tempans *= (temp==temp1);
			}
			if (tempans==1 && temp == 88){ans=2;}
			if (tempans==1 && temp == 79){ans=3;}
		}
		}

		if(!(ans==2 || ans==3)){		
		tempans=1; temp= AX[0][0];
		for(i=0,j=0;i<4,j<4;i++,j++){
			int temp1 = AX[i][j];
			tempans *= (temp==temp1);
		}
		if (tempans==1 && temp == 88){ans=2;}
		if (tempans==1 && temp == 79){ans=3;}
		}

		if(!(ans==2 || ans==3)){
		tempans=1; temp= AX[3][0];
		for(i=3,j=0;i>=0,j<4;i--,j++){
			int temp1 = AX[i][j];
			tempans *= (temp==temp1);
		}
		if (tempans==1 && temp == 88){ans=2;}
		if (tempans==1 && temp == 79){ans=3;}		
		}

		}

		//////////////////////////////

		if(!(ans==2 || ans==3)){

			for(i=0;i<4;i++){
			tempans=1; temp= AO[i][0];
			for(j=0;j<4;j++){
				int temp1 = AO[i][j];
				tempans *= (temp==temp1);
			}
			if (tempans==1 && temp == 88){ans=2;}
			if (tempans==1 && temp == 79){ans=3;}
		}
		if(!(ans==2 || ans==3)){
		for(j=0;j<4;j++){
			tempans=1; temp= AO[0][j];
			for(i=0;i<4;i++){
				int temp1 = AO[i][j];
				tempans *= (temp==temp1);
			}
			if (tempans==1 && temp == 88){ans=2;}
			if (tempans==1 && temp == 79){ans=3;}
		}
		}

		if(!(ans==2 || ans==3)){		
		tempans=1; temp= AO[0][0];
		for(i=0,j=0;i<4,j<4;i++,j++){
			int temp1 = AO[i][j];
			tempans *= (temp==temp1);
		}
		if (tempans==1 && temp == 88){ans=2;}
		if (tempans==1 && temp == 79){ans=3;}
		}

		if(!(ans==2 || ans==3)){
		tempans=1; temp= AO[3][0];
		for(i=3,j=0;i>=0,j<4;i--,j++){
			int temp1 = AO[i][j];
			tempans *= (temp==temp1);
		}
		if (tempans==1 && temp == 88){ans=2;}
		if (tempans==1 && temp == 79){ans=3;}		
		}

		}

		///////////////////////////////



		if(ans==1){
			cout<<"Case #"<<casenum<<": Game has not completed\n";
		}
		else if(ans==2){
			cout<<"Case #"<<casenum<<": X won\n";
		}
		
		else if(ans==3){
			cout<<"Case #"<<casenum<<": O won\n";
		}
		else {
			cout<<"Case #"<<casenum<<": Draw\n";
		}
	casenum++;
	T--;
	}
	return 0;
}
