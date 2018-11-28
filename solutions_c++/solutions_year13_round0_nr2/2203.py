#include <iostream>
#include <fstream>
#include <conio.h>
#include <cstdlib>

using namespace std;
int N,M,remN,remM, minVal=1;
int arr[101][101];

bool checkrow(int n){
	for (int m=0; m<M; m++){
		if(arr[N][m]==1 && arr[n][m]!=minVal) return false;
	}
	arr[n][M]=0;
	remN--;
	return true;
	
}

bool checkcol(int m){
	for (int n=0; n<N; n++){
		if(arr[n][M]==1 && arr[n][m]!=minVal) return false;
	}
	arr[N][m]=0;
	remM--;
	return true;
	
}

int main(){
	//ifstream cin("B-large.in");
	ofstream out("out.txt");
	int T; cin>>T;
	
	for (int t=1; t<=T; t++){
		out<<"Case #"<<t<<": ";
		
		cin>>N>>M;
		remN=N; remM=M;
		for (int n=0; n<N; n++){
			for (int m=0; m<M; m++){
				cin>>arr[n][m];
				//cout<<(arr[n][m]==1?"0":"-")<<" ";
			}
			//cout<<endl;
			arr[n][M]=1;
		}
		fill(arr[N],arr[N]+M, 1);
		
		int minI, minJ, min, n, m;
		minVal=1;
		bool val=true;
		while (remN!=0 && remM!=0){
			min=101;
			for (n=0; n<N; n++){
				if(arr[n][M]==0)continue;
				for (m=0; m<M; m++){
					if(arr[N][m]==1 && arr[n][m]<min){
						min=arr[n][m];
						minI=n; minJ=m;
						if(min==minVal){
							val=false; break;
						}
					}
				}
				if(!val){
					val=true; break;
				}
			}
			
			minVal=min;
			//cout<<minVal<<endl;
			
			if(!checkrow(minI) && !checkcol(minJ)) {
				val=false;
				break;
			}
		}
		
		if(val)out<<"YES\n";
		else out<<"NO\n";
		//getch(); system("cls");
	}
	
	return 0;
}
