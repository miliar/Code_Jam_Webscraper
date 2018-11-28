//============================================================================
// Name        : magic.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {

//	freopen("d:\\A-small-attempt0.in", "r", stdin);
//	freopen("d:\\a-small.txt", "w", stdout);
	int n;
	cin>>n;
	for (int i=0;i<n;++i){
		int array1[4][4];
		int array2[4][4];
		int num1,num2;
		cin>>num1;
		for (int m=0;m<4;m++){
			for (int l=0;l<4;l++){
				cin>>array1[m][l];
			}
		}
		cin>>num2;
		for (int x=0;x<4;x++){
				for (int z=0;z<4;z++){
					cin>>array2[x][z];
				}
			}
		int num=0;
		int res;
		for (int j=0;j<4;j++){
			for (int k=0;k<4;k++){
				if(array1[num1-1][j]==array2[num2-1][k]){
					num++;
					res=array1[num1-1][j];
				}
			}
		}
		if(num==0)
			cout<<"Case #"<<i+1<<":"<<" "<<"Volunteer cheated!"<<endl;
		else if(num==1)
			cout<<"Case #"<<i+1<<":"<<" "<<res<<endl;
		else
			cout<<"Case #"<<i+1<<":"<<" "<<"Bad magician!"<<endl;

	}
	return 0;
}
