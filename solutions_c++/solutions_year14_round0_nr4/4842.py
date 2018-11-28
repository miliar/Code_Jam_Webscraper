#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>
#include <vector>
using namespace std;

void one_game(ofstream& fout){
	vector<float> N,K;
	int m = 0;
	cin>>m;
	
	for(int i=0;i<m;i++){
		float tmp;
		cin>>tmp;
		N.push_back(tmp);
	}
	
	for(int i=0;i<m;i++){
		float tmp;
		cin>>tmp;
		K.push_back(tmp);
	}
	
	sort(N.begin(),N.end());
	sort(K.begin(),K.end());
	vector<float>::iterator it;

	/*
	cout<<endl;
	for(it=N.begin();it!=N.end();it++)
	cout<<*it<<" ";	
	cout<<endl;
	for(it=K.begin();it!=K.end();it++)
	cout<<*it<<" ";
	cout<<endl;
	*/
		
	int dw=0,w=0;
	int x = 0;
	int xend = K.size()-1;
	
	for(int i=0;i<N.size();i++){
		if(N[i]>K[x]){
			dw++;
			x++;	
		}
		else if(N[i]<K[x])
			xend--;
		else;
		
	}
	
	fout<<dw<<" ";
	
	x = K.size()-1;
	for(int i=N.size()-1;i>=0;i--){
		if(N[i]>K[x])
			w++;
		else
			x--;
	}
	
	fout<<w;
	
}

int main(){
	int T = 0;
	cin>>T;
	ofstream fout;
	fout.open("gcj_q4.out");
	
	for(int i=0;i<T;i++){
		fout<<"Case #"<<i+1<<": ";
		one_game(fout);
		fout<<endl;
	}

}