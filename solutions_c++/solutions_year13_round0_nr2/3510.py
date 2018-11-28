#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
#include <cassert>
#include <cstring>
using namespace std; 

int lawn[100][100];


int main()
{
	string filedir="D:\\Dropbox\\Contest\\Algorithm\\GCJ\\2013Q\\";
    string fname = "B-large";
    freopen((filedir+fname+".in").c_str(), "r", stdin);
    freopen((filedir+fname+".out").c_str(), "w", stdout);


	bool res;

	int T=0;
	cin>>T;
	int N,M;
	for(int t=1;t<=T;t++){
		res=true;
		cin>>N>>M;
		for(int n=0;n<N;n++){
			for(int m=0;m<M;m++) {
				cin>>lawn[n][m];
			}
		}

		for(int r=0;r<N;r++){
			for(int c=0;c<M;c++){
				int block=lawn[r][c];
				int rcount=0;
				int ccount=0;
				int i,j;

				for(i=r,j=0;j<M;j++){
					if(lawn[i][j]<=block)
						ccount++;
				}

				for(j=c,i=0;i<N;i++){
					if(lawn[i][j]<=block)
						rcount++;
				}

				if((ccount!=M)&&(rcount!=N))
					res=false;		
			}
		}

		if(res)
			cout<<"Case #"<<t<<": YES"<<endl;
		else
			cout<<"Case #"<<t<<": NO"<<endl;
	}
}