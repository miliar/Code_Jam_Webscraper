#include <iostream>
#include <vector>
#include <string>
using namespace std;
bool isRowOne(vector<vector<int> >&lawn,int row){
	for(int i=0;i<lawn[row].size();i++){
		if(lawn[row][i]==2) return false;
	}
	return true;
}
bool isColOne(vector<vector<int> >&lawn,int col){
	for(int i=0;i<lawn.size();i++){
		if(lawn[i][col]==2) return false;
	}
	return true;
}
int main(){
	int tests;
	cin>>tests;
	for(int test=1;test<=tests;test++){
		int n,m;
		cin>>n>>m;
		vector< vector<int> > lawn(n,vector<int>(m));
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				cin>>lawn[i][j];
			}
		}
		bool ans=true;
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				if(lawn[i][j]==1){
					if(!isRowOne(lawn,i)&&!isColOne(lawn,j)){
						ans=false;
						break;
					}
				}
			}
			if(!ans) break;
		}
		string strAns;
		if(ans)
			strAns = "YES";
		else
			strAns = "NO";
		cout<<"Case #"<<test<<": "<<strAns<<endl;
	}
	return 0;
}