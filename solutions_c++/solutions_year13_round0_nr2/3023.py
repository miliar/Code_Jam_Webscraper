#include <string>
#include <iostream>
#include <algorithm>
#include <cstdlib>

using namespace std;

int a[103][103];

int main(){
	int T;
	cin >> T;
	for(int t=1;t<=T;t++){
		int N,M;
		cin >> N >> M;

		for(int i=0;i<N;i++)
			for(int j=0;j<M;j++)
				cin >> a[i][j];

		bool good = true;
		for(int i=0;i<N;i++){
			for(int j=0;j<M;j++){
				int height = a[i][j];
				int goodrow = true;
				int goodcol = true;
				for(int k=0;k<M;k++){
					if(a[i][k]>height){
						goodrow = false;
					}
				}
				for(int k=0;k<N;k++){
					if(a[k][j]>height){
						goodcol = false;
					}
				}
				if(!goodrow&&!goodcol){
					good = false;
					goto printAns;
				}
			}
		}

		printAns:
		if(good){
			cout<<"Case #"<<t<<": YES"<<endl;
		} else {
			cout<<"Case #"<<t<<": NO"<<endl;
		}
	}
}