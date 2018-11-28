#include "stdafx.h"
#include <fstream>
#include <string>
using namespace std;

int main (int argc, char *argv[])
{
	ifstream infile("input.txt");
	ofstream outfile("out.txt");
	int T;
	infile>>T;
	int lawn[10][10];
	for(int i=1;i<=T;i++){
		int N,M;
		infile>>N>>M;
		for(int j=0;j<N;j++)
			for(int k=0;k<M;k++)
				infile>>lawn[j][k];
		
		int j;
		for(j=0;j<N;j++){
			int k;
			for(k=0;k<M;k++){
				if(lawn[j][k]!=1) continue;
				int r;
				//row scan
				for(r=k-1;r>=0;r--){
					if(lawn[j][r]>1) break;//faild
					else lawn[j][r]=-1;
				}
				if(r==-1){
					for(r=k+1;r<M;r++){
						if(lawn[j][r]>1) break;//faild
						else lawn[j][r]=-1;
					}
					if(r==M) continue;//pass
				}
				
				//col scan
				for(r=j-1;r>=0;r--){
					if(lawn[r][k]>1) break;
					else lawn[r][k]=-1;
				}
				if(r==-1){
					for(r=j+1;r<N;r++){
						if(lawn[r][k]>1) break;
						else lawn[r][k]=-1;
					}
					if(r!=N) break;//no path.
				}
				else break;
			}
			if(k!=M) break;
		}
		char cval[4];
		sprintf(cval,"%d",i);
		string linehead="Case #"+string(cval);
		if(j!=N) outfile<<linehead+": NO"<<endl;
		else outfile<<linehead+": YES"<<endl;
	}
	return 0;
}
