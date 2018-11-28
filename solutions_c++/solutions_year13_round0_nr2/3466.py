
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <string>
#include <sstream>

using namespace std;


int lawn[102][102];
int mcol[102];
int mrow[102];

int main(){

	ifstream in;
	in.open("Blarge.in");
	
	ofstream out;
	out.open("out.txt");
	
	int T;
	in>>T;
	
	
	
	for(int u=0;u<T;u++){
	
		int N,M;
		in>>N>>M;
		
		for(int i=0;i<N;i++){
			int m = 0;
			for(int j=0;j<M;j++){
				in>>lawn[i][j];
				if(lawn[i][j] > m){
					m = lawn[i][j];
				}
			}
			mrow[i] = m;
		}
		
		for(int j=0;j<M;j++){
			int m=0;
			for(int i=0;i<N;i++){
				if(lawn[i][j] > m){
					m = lawn[i][j];
				}
			}
			mcol[j] = m;
		}
		int isPos = 1;
		for(int i=0;i<N;i++){
			for(int j=0;j<M;j++){
				if(lawn[i][j] < mrow[i] && lawn[i][j] < mcol[j]){
					isPos = 0;
					break;
				}
			}
		}
		
		if(isPos==1){
			out<<"Case #"<<(u+1)<<": YES"<<endl;
			cout<<"Case #"<<(u+1)<<": YES"<<endl;
		}
		else{
			out<<"Case #"<<(u+1)<<": NO"<<endl;
			cout<<"Case #"<<(u+1)<<": NO"<<endl;
		}
		
    }
	in.close();
	out.close();
	
    return 0;
}





