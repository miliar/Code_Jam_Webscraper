#include<iostream>
#include<fstream>
using namespace std;

int main(){
	int numberOfTestCases;
	cin>>numberOfTestCases;
	int k=1;
	int ans=0;
	ofstream myfile;
	myfile.open ("output.txt");
	while(numberOfTestCases){
		int firstQuestion;
		cin>>firstQuestion;
		int firstArrangement[4][4];
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>firstArrangement[i][j];
			}
		}
		int secondQuestion;
		cin>>secondQuestion;
		int secondArrangement[4][4];
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>secondArrangement[i][j];
			}
		}
		int count=0;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(firstArrangement[firstQuestion-1][i]==secondArrangement[secondQuestion-1][j]){
					count++;
					if(count==1){
						ans=firstArrangement[firstQuestion-1][i];
					}
				}
			}
		}
		if(count==0){
			myfile<<"Case #"<<k<<": Volunteer cheated!\n";
		}
		else if(count==1){
			myfile<<"Case #"<<k<<": "<<ans<<"\n";
		}
		else{
			myfile<<"Case #"<<k<<": Bad magician!\n";
		}
		numberOfTestCases--;
		k++;
	}
	myfile.close();
	return 0;
}