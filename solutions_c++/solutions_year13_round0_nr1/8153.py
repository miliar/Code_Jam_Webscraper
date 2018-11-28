#include<iostream>
#include<cstdio>
#include<string.h>
#include<cstring>
#include<string>
using namespace std;
main(){
	char arr[4][4];
	bool temp;
	bool flag;

	int i,j,k,sum=0,t;
	cin >> t;
	for(k=1;k<=t;k++){
		temp = false;
		flag = false;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				cin >> arr[i][j];
				if(arr[i][j] == '.')
					flag = true;
			}
		}
		for(i=0;i<4;i++){
			sum = 0;
			sum = (arr[i][0] + arr[i][1] + arr[i][2] + arr[i][3]);
			if(sum == 352 || sum == 348){
				temp=true;
				cout << "Case #"<< k <<": X won";
				break;
			}
		else if(sum == 316 || sum == 321){
				temp=true;
				cout << "Case #"<< k << ": O won";
				break;
			}
		}
		if(temp==false){
			for(i=0;i<4;i++){
				sum = 0;
				sum = (arr[0][i] + arr[1][i] + arr[2][i] + arr[3][i]);
				if(sum == 352 || sum == 348){
					temp = true;
					cout << "Case #"<< k<<": X won";
					break;
				}
			     else if(sum == 316 || sum == 321){
					temp = true;
					cout << "Case #"<< k<<": O won";
					break;
				}
			}
		}
		if(temp==false){
			int sum1 = 0;
			int sum2 = 0;
			sum1 = arr[0][0] + arr[1][1] + arr[2][2] + arr[3][3];
			sum2 = arr[0][3] + arr[1][2] + arr[2][1] + arr[3][0];
			if(sum1 == 352 || sum1 == 348 || sum2 == 352 || sum2 == 348){
				temp=true;
				cout << "Case #"<< k <<": X won";
			}

	       		else if(sum1 == 316 || sum1 == 321 || sum2 == 316 || sum2 == 321){
				temp=true;
				cout <<"Case #"<<k<<": O won";
			}
		}

		if(temp == false){
			if(flag==true){
				temp=true;
				cout << "Case #"<< k <<": Game has not completed";
			}
		}
	       if(temp==false)
			cout<<"Case #"<<k<<": Draw";

		cout << "\n";
	}
}
			

