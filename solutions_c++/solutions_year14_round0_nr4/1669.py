#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;

bool naoMark[1010];

void popFrontVec(vector<double>& vec){
	for(int i = 0 ; i<vec.size()-1 ; i++){
		vec[i] = vec[i+1];
	}
	vec.pop_back();
}

int main(){
	ifstream ifs("D-large.in");
	ofstream sorted("sorted.out");
	ofstream ofs("D.out");
	int numCases, N;
	ifs>>numCases;

	for(int q = 0; q<numCases; q++){
		vector<double> nao, ken;
		ifs>>N;
		double tempD;
		for(int i = 0; i<1010; i++)naoMark[i] = false;
		for(int i = 0; i<N; i++){
			ifs>>tempD;
			nao.push_back(tempD);
		}	
		for(int i = 0; i<N; i++){
			ifs>>tempD;
			ken.push_back(tempD);
		}
		sort(ken.begin(), ken.end());
		sort(nao.begin(), nao.end());
		sorted<<q+1<<", N = "<<N<<endl;
		for(int i = 0; i<N; i++){
			sorted<<nao[i]<<" ";
		}	
		sorted<<endl;
		for(int i = 0; i<N; i++){
			sorted<<ken[i]<<" ";
		}	
		
		sorted<<endl;
		int kWin = 0;
		double rbound = nao[0];
		for(int i = 0; i<ken.size(); i++){
			if(ken[i] > rbound){
				int j = 0;
				while( ken[i] > nao[j]){
					if( !naoMark[j]){
						naoMark[j] = true;
						kWin++;
						break;
					}else j++;
				}
			}
		}
		
		int kWindecit = 0;
		while(nao.size() > 0){
			rbound = ken[0];
			int inc = 0;
			for(int i = 0; i<nao.size(); i++){
				if(nao[i] < rbound){
					inc++;
				}
			}
			kWindecit += inc;
			for(int i = 0; i<inc; i++){
				popFrontVec(nao);
				ken.pop_back();
			}
			inc = 0;
			while(nao.size() > 0 && nao[0] > ken[0]){
				popFrontVec(nao);
				popFrontVec(ken);
			}
		}
		ofs<<"Case #"<<q+1<<": "<<N-kWindecit<<" "<<N-kWin<<endl;
	}
	system("pause");
}