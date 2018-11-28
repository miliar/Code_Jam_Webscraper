#include<iostream>
#include<vector>
using namespace std;

int deck1[4][4], deck2[4][4];
int sameNum = -1;
int findAns(int row1, int row2){
	vector<int> v;
	for(int j=0;j<4;j++){
		v.push_back(deck1[row1][j]);
	}
	
	int ans = 0;
	for(int j=0;j<4;j++){
		for(int k=0;k<v.size();k++){
			if(v[k] == deck2[row2][j]){
				ans++;
				sameNum = v[k];
			}
		}
	}
	return ans;
}

int main(){
	int tc,g1,g2;
	
	
	cin>>tc;
	for(int i=1;i<=tc;i++){
		cin>>g1;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				cin>>deck1[j][k];
			}
		}
		cin>>g2;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				cin>>deck2[j][k];
			}
		}
		
		int res = findAns(g1-1,g2-1);
		if(res == 0){
			cout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
		} else if(res == 1){
			cout<<"Case #"<<i<<": "<<sameNum<<endl;
		} else {
			cout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
		}
	}
	return 0;
}