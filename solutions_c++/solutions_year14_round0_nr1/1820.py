#include <iostream>
#include <string>
using namespace std;
int arr1[4][4];
int arr2[4][4];
int row1;
int row2;

int judge(){
	int cnt = 0;
	int res = 0;
	for(int i = 0; i < 4; i++) {
		int num1 = arr1[row1-1][i];
		for(int j = 0; j < 4; j++){
			int num2 = arr2[row2-1][j];
			if(num1 == num2){
				cnt++;
				res = num1;
			}
		}
	}
	if(cnt == 0){
		return -1;
	}
	if(cnt > 1){
		return 0;
	}
	return res;
}

int main(){
	int num;
	cin>>num;
	int res[100];
	for(int i = 0; i < num; i++){
		cin>>row1;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				cin>>arr1[i][j];
		cin>>row2;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				cin>>arr2[i][j];
		res[i]=judge();
	}
	for(int i = 0; i < num; i++){
		cout<<"Case #"<<i+1<<": ";
		if(res[i] == 0)
			cout<<"Bad magician!"<<endl;
		else if(res[i]==-1)
			cout<<"Volunteer cheated!"<<endl;
		else
			cout<<res[i]<<endl;
	}
}