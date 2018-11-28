#include <iostream>
#include <string>
#include <fstream>


using namespace std;

int main (int argc,char* argv[]){
	ifstream is ;
	is.open(argv[1],ifstream::in);
	ofstream os ;
	os.open(argv[2],ofstream::out);
	int cases =0;
	is >> cases ;
	int before =0;
	int after =0;
	int match =0;
	int target =0;
	int A[4][4] ;
	int B[4][4] ;
	for(int i=0;i<cases;i++){
		is >> before ;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				is>>A[j][k];
			}
		}
		is >> after ;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				is>>B[j][k];
			}
		}
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				if(A[before-1][j]==B[after-1][k]){
					match++ ;
					target = A[before-1][j] ;
				}
					
			}
		}
		if(match==1){
			os<<"Case #"<<i+1<<": "<<target<<endl ;
		}
		else if(match>1){
			os<<"Case #"<<i+1<<": Bad magician!"<<endl ;
		}
		else{
			os<<"Case #"<<i+1<<": Volunteer cheated!"<<endl ;
		}
		match = 0 ;
		target = 0 ;
		
	}
	return 0 ;
	
	
	
}
