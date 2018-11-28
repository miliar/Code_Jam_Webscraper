#include <iostream>
#include <vector>
using namespace std;
int main(){
	int cases,a,b;
	cin>>cases;
	for(int t=1;t<=cases;t++){
		vector<vector<int> > cards1(4,vector<int>(4));
		vector<vector<int> > cards2(4,vector<int>(4));
		cin>>a;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>cards1[i][j];
			}
		}
		cin>>b;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>cards2[i][j];
			}
		}
		int count = 0,common;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(cards1[a-1][i]==cards2[b-1][j]){
					count++;
					common = cards1[a-1][i];
				}
			}
		}
		cout<<"Case #"<<t<<": ";
		if(count==1) cout<<common;
		else if(count==0) cout<<"Volunteer cheated!";
		else cout<<"Bad magician!";
		cout<<endl;
	}
	return 0;
}