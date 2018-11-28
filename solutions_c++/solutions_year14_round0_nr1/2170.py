#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;
int main(){
	
	freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
	
	int testCase;
	int firstRow,secondRow;
	int temp;
	int firstRowArr[4];
	int secondRowArr[4];
	cin>>testCase;
	for(int i=1;i<=testCase;i++){
		cin>>firstRow;
		for(int j=0;j<firstRow-1;j++){
			cin>>temp>>temp>>temp>>temp;
		}
		cin>>firstRowArr[0]>>firstRowArr[1]>>firstRowArr[2]>>firstRowArr[3];
		for(int j=firstRow;j<4;j++){
			cin>>temp>>temp>>temp>>temp;
		}
		cin>>secondRow;
		for(int j=0;j<secondRow-1;j++){
			cin>>temp>>temp>>temp>>temp;
		}
		cin>>secondRowArr[0]>>secondRowArr[1]>>secondRowArr[2]>>secondRowArr[3];
		for(int j=secondRow;j<4;j++){
			cin>>temp>>temp>>temp>>temp;
		}
		int count = 0;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				if(firstRowArr[j]==secondRowArr[k]){
					temp = firstRowArr[j]; 
					count++;
					break;
				}
			}
		}
		cout<<"Case #"<<i<<": ";
		if(count == 0){
			cout<<"Volunteer cheated!"<<endl;
		}else if(count == 1){
			cout<<temp<<endl;
		}else{
			cout<<"Bad magician!"<<endl;
		}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}