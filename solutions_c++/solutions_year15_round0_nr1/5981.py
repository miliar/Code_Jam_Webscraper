#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string.h>
#include <sstream>
#include <vector>
#include <algorithm>    // std::sort

using namespace std;

string convertInt(int n){
	stringstream ss;
	ss << n;
	return ss.str();
}

int solve(int N,string X){

	int max=0;int num=0;
	for(int i=0;i<=N;i++){
		int poss=i-num;
		if(poss>max)
			max=poss;
		num=num+atoi(X.substr(i,1).c_str());
	}
	return max;

}


int main(int argc,char* argv[]){
	freopen(argv[1],"r",stdin);
	fstream output("output");
	string line;
	getline(cin,line);
	int T=(atoi(line.c_str()));
	int i,N; string X;
	for(i=0;i<T;i++){
		getline(cin,line);int j;
		// N=(atoi(line.c_str()));	
		// getline(cin,line);
		int k=0;int p=0;vector<int> sizes;		
		for(j=0;j<line.length();j++){
			if(line[j]==' ')
				break;

			// if(k==N-1){
			// 	sizes.push_back(atoi(line.substr(p).c_str()));break;
			// 	}			
			// if(line[j]==' '){
			// 	sizes.push_back(atoi(line.substr(p,j-p).c_str()));
			// 	p=j+1;k=k+1;
			// 	}
			}
		N=(atoi(line.substr(0,j).c_str()));
		X=line.substr(j+1);
		// X=

		int ans=solve(N,X);
		printf("Case #%d: %d\n",i+1,ans);
		output << "Case #" << i+1 <<": " << ans << "\n" ;
	}
	output.close();
	return 0;
}

