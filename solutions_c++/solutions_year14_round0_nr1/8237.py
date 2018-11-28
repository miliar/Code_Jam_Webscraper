#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int numCommonNumbers(int row1[4],int row2[4]){
	int num=0,common;
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(row1[i]==row2[j]){
				num++;
				common = row1[i];
			}
		}
	}
	if(num==1)
		return common;
	if(num==0)
		return 0;
	if(num>1)
		return -1;
}

int main(){
	int T,caseNum=1;
	cin >> T;
	while(caseNum<=T){
		int arrange1[4][4],arrange2[4][4],ans1,ans2,row1[4],row2[4];
		cin >> ans1;
		ans1--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++)
				cin >> arrange1[i][j];
		}
		cin >> ans2;
		ans2--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++)
				cin >> arrange2[i][j];
		}
		for(int j=0;j<4;j++)
			row1[j] = arrange1[ans1][j];
		for(int j=0;j<4;j++)
			row2[j] = arrange2[ans2][j];
		if(numCommonNumbers(row1, row2)==0)
			cout << "Case #"<<caseNum<<": Volunteer cheated!"<<endl;
		else if(numCommonNumbers(row1, row2)==-1)
			cout << "Case #"<<caseNum<<": Bad magician!"<<endl;
		else
			cout << "Case #"<<caseNum<<": "<<numCommonNumbers(row1, row2)<<endl;
		caseNum++;
	}
	return 0;
}


