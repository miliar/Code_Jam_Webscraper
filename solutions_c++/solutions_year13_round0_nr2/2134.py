#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool checkBoundaries(vector< vector<int> > v,int j, int k,int N, int M){
	int x,y;
	int cur=v[j][k];

	//check x
	for(x=0;x<N;x++){
		if(v[x][k]>cur){
			//check up
			for(y=0;y<M;y++){
				if(v[j][y]>cur){
					return false;
				}
			}
		}
	}
	return true;
}
int main(){
	int T,N,M,i,j,k;
	int tmp;
	vector< vector<int> > pattern;
	int flag=0;
	cin>>T;

	for(int i=0;i<T;i++){
		flag=0;
		cin>>N>>M;
		for(int j=0;j<N;j++){
			vector<int> v1;
			for(int k=0;k<M;k++){
				cin>>tmp;
				v1.push_back(tmp);
			}
			pattern.push_back(v1);
		}

		for(int j=0;j<N;j++){
			for(int k=0;k<M;k++){
				if(!checkBoundaries(pattern,j,k,N,M)){
					cout<<"Case #"<<i+1<<": NO"<<endl;
					flag=1;
					break;
				}
			}
			if(flag) break;
		}
		if(!flag)cout<<"Case #"<<i+1<<": YES"<<endl;
		pattern.clear();
	}
	return 0;
}
