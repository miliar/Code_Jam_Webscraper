#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;

int* WarAndDecWar(int N,double *Na,double *Ke){
	 double val;
	 bool indexW[N],indexDW[N];
	 for(int i = 0;i<N;i++)
	 	indexW[i] = indexDW[i] = 0;
	 int optwar=0,optdecwar=0;
	 for(int i = 0; i < N; i++){
	 	bool skip = false;
		 for(int j = 0; j < N; j++){
	 		if( Na[i] > Ke[j] && !indexDW[j] ){
	 			optdecwar++;
	 			indexDW[j] = 1;
	 			break;
	 		}
	 	 }
	 	 for(int j = 0; j < N && !skip; j++){
	 	
	 	 	if( Na[i] < Ke[j] && !indexW[j] ){
	 			indexW[j] = 1;
	 			skip = 1;
	 		}
	 	 }
	 	 if(skip)
	 	  skip = 0;
	 	 else
	 	  optwar++;
	 	  
	 }
	 
	 int *ans;
	 ans = new int[2];
	 ans[0] = optdecwar;
	 ans[1] = optwar;
	 return ans;
	 
}
int main(){
	int t = 0, j = 1;
	ifstream ifile("D-large.in");
	ofstream ofile("D-small-attempt0.out");
	//if(!ifile) return 0;
	ifile>>t;
	while(t--){
		int N;
		ifile>>N;
		
		double Na[N],Ke[N];
		for(int i = 0;i<N;i++)
	 		ifile>>Na[i];
	 	for(int i = 0;i<N;i++)
	 		ifile>>Ke[i];
	 	sort(Na,Na+N);
	 	sort(Ke,Ke+N);
		int *ans = WarAndDecWar(N,Na,Ke);
	 	//cout<< "Case #" << j++ << ": " << ans[0] << " " << ans[1] << endl ;
        ofile<< "Case #" << j++ << ": " << ans[0] << " " << ans[1] << endl ;
          
	}
	
}
