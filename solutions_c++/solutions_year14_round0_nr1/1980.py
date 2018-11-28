#include <bits/stdc++.h>
using namespace std;


int getAns(vector<int> first, vector<int> second){
	vector<int> index;
	for(int i=0;i<(int)first.size();i++){
		for(int j=0;j<(int)second.size();j++){
			if(first[i]==second[j]){
				index.push_back(first[i]);
			}
		}
	}
	if(index.size()==0){
		return -2;
	}
	else if (index.size()>1){
		return -1;
	}
	else if (index.size()==1){
		return index[0];
	}
	return -3;
}

int main(){
	//freopen("in.txt","r",stdin);
	int tc;
	cin >> tc;
	for(int d=1;d<=tc;d++){
		vector<int> first,second;
		int row1;
		cin >> row1;
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				int temp;
				cin >> temp;
				if(i==row1){
					first.push_back(temp);
				}
			}
		}
		
		int row2;
		cin >> row2;
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				int temp;
				cin >> temp;
				if(i==row2){
					second.push_back(temp);
				}
			}
		}
		
		cout << "Case #" << d << ": ";
		int ans = getAns(first,second);
		if(ans>0){
			cout << ans << endl;
		}
		else if (ans==-1){
			cout << "Bad magician!" << endl;
		}
		else if (ans==-2){
			cout << "Volunteer cheated!" << endl;
		}
		
	}
}
