#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
	int testCases;
	int cards1[4][4]={0};
	int cards2[4][4]={0};

	cin>>testCases;
	for(int i=0;i<testCases;i++){
		int answ1;
		int answ2;
		cin>>answ1;
		cin.get();
		answ1--;


		for(int j=0;j<4;j++){
			string line;
			getline(cin,line);
			istringstream ss(line);

			for(int k=0;k<4;k++){
				ss>>cards1[j][k];
			}
		}
		cin>>answ2;
		answ2--;
		cin.get();
		for(int j=0;j<4;j++){
			string line;
			getline(cin,line);
			istringstream ss(line);

			for(int k=0;k<4;k++){
				ss>>cards2[j][k];
			}
		}

		int count=0;
		int answer=-1;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				if(cards1[answ1][j]==cards2[answ2][k]){
					if(!count)answer=cards1[answ1][j];
					count++;

				}
			}
		}

		if(count==0){
			cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		}else if(count>1){
			cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
		}else{

			cout<<"Case #"<<i+1<<": "<<answer<<endl;
		}
	}
}
