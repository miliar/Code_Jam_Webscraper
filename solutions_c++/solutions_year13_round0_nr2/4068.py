//
// april 2013
// vladh (vladh.net)
// all rights reserved
//

#include<iostream>
#include<fstream>
using namespace std;

int main(){
	ifstream in("B-large.in");
	ofstream out("data.out");
	string line;
	long long cases, k, n, m, i, j, x, max, lawn[100][100], status=0;
	bool possible=true;
	
	getline(in,line);
	cases = atoi(line.c_str());

	for(k=1; k<=cases; k++){
		possible=true;
		in>>n;
		in>>m;

		for(i=0; i<n; i++){
			for(j=0; j<m; j++){
				in>>lawn[i][j];
			}
		}

		for(i=0; i<n; i++){
			for(j=0; j<m; j++){
				status=0;

				max=0;
				for(x=0; x<n; x++){
					if(lawn[x][j] > max){
						max = lawn[x][j];
					}
				}
				if(lawn[i][j] < max) status++;

				max=0;
				for(x=0; x<m; x++){
					if(lawn[i][x] > max){
						max = lawn[i][x];
					}
				}
				if(lawn[i][j] < max) status++;

				if(status==2){
					possible=false;
					break;
				}
			}
			if(possible==false) break;
		}

		out<<"Case #"<<k<<": ";
		if(possible){
			out<<"YES";
		}else{
			out<<"NO";
		}
		out<<endl;
	}
	
	return 0;
}
