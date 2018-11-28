#include<iostream>
#include<cstdio>
#include <cstring>

using namespace std; 

int main (){
	int input1[4][4], input2[4][4];
	bool flag=false, arr[16]; 
	int T;
	cin>>T;
	int magic[T],store_res[T];	
	for (int i = 0; i < T; i++){
		int choice1, choice2;
		cin>> choice1;
		for(int m=0; m<4;m++){
			for (int n =0;n<4;n++){
				cin>>input1[m][n];
			}
		}	
		cin>>choice2;
		for( int m=0; m<4;m++){
			for ( int n =0;n<4;n++){
				cin>>input2[m][n];
				arr[4*m + n] = false;
			}
		}		
		int countTrue=0;		
		for (int k = 0; k<4;k++){
			arr[input1[choice1-1][k] - 1  ]=true;
		}
		for (int k =0; k<4;k++){
			if (arr[input2[choice2-1][k] -1 ]==true){
					countTrue++;
				if (countTrue==1){
					magic[i] = input2[choice2-1][k];
				}
			}
		}
		
		if (countTrue==1){
			store_res[i]=0;
		}else if (countTrue==0){
			store_res[i]=1;
		}else {
			store_res[i]=2;
		}
	}
	for (int i=0; i < T; i++){
		switch (store_res[i]){
			case 0:
				cout <<"Case #"<<i+1<<": "<<magic[i]<<"\n";
				break;
			case 1:
				cout <<"Case #"<<i+1<<": Volunteer cheated!"<<"\n";
				break;
			case 2:
				cout <<"Case #"<<i+1<<": Bad magician!"<<"\n";
				break;
		}		
			
	}
}
