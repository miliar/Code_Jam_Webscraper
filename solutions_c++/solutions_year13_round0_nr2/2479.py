#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int main(){
	ifstream infile("B-large.in");
	ofstream outfile("outputB.out");
	int T;
	infile>>T;
	
	for( int t=1;t<=T;++t ){
		int N, M;
		bool bigposs=true;
		vector<vector<int> > lawn;
		infile>>N>>M;
		lawn.resize(N);
		
		for( int i=0;i<N;++i ){
			lawn[i].resize(M,0);
			
			for( int j=0;j<M;++j ){
				int in;
				infile>>in;
				lawn[i][j]=in;
			}
		}
		
		//checking each cell
		for( int r = 0 ; r < N;++r ){
			for( int c=0;c<M;++c) {
				bool poss=true;
				
				//checking the row;
				for( int m=0;m<M;++m ){
					if( lawn[r][m] > lawn[r][c] ){
						poss=false;
						break;
					}
				}
				
				if( poss ) continue;
					
				poss=true;
				//checking the column
				for(int n=0;n< N;++n ){
					if( lawn[n][c] > lawn[r][c] ){
						poss=false;
						break;
					}
				}
				
				if( poss ) continue;
				bigposs=false;
				break;
			}			
			if( !bigposs ) break;
		}
		
		if( bigposs ){
			outfile<<"Case #"<<t<<": YES"<<endl;
		} else {
			outfile<<"Case #"<<t<<": NO"<<endl;
		}
	}
	
	return 0;
}