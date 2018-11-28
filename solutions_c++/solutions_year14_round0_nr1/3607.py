#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	int t;
	cin>>t;
	for(int p = 0; p < t; p++){
		int count[16];
		for(int i = 0; i < 16; i++){
			count[i] = 0;
		}
		int ans;
		int board[4][4];
		for(int x = 0; x < 2; x++){
			cin>>ans;
			for(int i = 0; i < 4; i++)
				for(int j = 0; j < 4; j++)
					cin>>board[i][j];
			for(int i = 0; i < 4; i++)
				count[board[ans - 1][i] - 1]++;
		}
		int found = 0;
		for(int i = 0; i < 16; i++){
			if(count[i] == 2){
				ans = i + 1;
				found++;
			}
		}
		cout<<"Case #"<<p + 1<<": ";
		if(found == 0){
			cout<<"Volunteer cheated!"<<endl;
		}
		else if(found == 1){
			cout<<ans<<endl;
		}
		else{
			cout<<"Bad magician!"<<endl;
		}
	}
	return 0;
}