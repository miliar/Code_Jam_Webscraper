#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
using namespace std;

int main() {
	ofstream cout("output.txt");
	ifstream cin("input.txt");
	int N=0; cin>>N;
	for(int o=1;o<=N;++o){
		int k1=0,k2=0,ie=0,k=0;
		cin>>ie; vector<double>W(ie); vector<double>M(ie);
		for(int i=0;i<ie;++i) cin>>W[i];
		for(int i=0;i<ie;++i) cin>>M[i];
		sort(W.begin(),W.end()); sort(M.begin(),M.end());
		
		for(int i=0;i<ie;++i){
			if(W[i]<M[i-k])++k;
			else ++k1;
		}
		k=0;
		for(int i=0;i<ie;++i){
			int f=1;
			for(int j=0;j<ie;++j)
				if(W[i]<M[j]){M[j]=0,f=0;break;}
			if(f){
				++k2;
				for(int j=0;j<ie;++j)if(M[j]!=0){M[j]=0;break;}
			}
		}
		
		cout<<"Case #"<<o<<": "<<k1<<" "<<k2<<endl;
	}
	return 0;
}
