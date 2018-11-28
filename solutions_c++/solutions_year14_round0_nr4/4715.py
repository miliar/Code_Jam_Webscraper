#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>

using namespace std;

int score, testcases, N, war, deceit;
double temp, MaxNaomi, MinNaomi, MaxKen, MinKen;
vector<double>::iterator it;

int War(vector<double> &N, vector<double> &K, int n){
	score=0;
	while(K.size()>0){
		MaxNaomi=*max_element(N.begin(),N.end());
		MaxKen=*max_element(K.begin(),K.end());
	if(MaxNaomi>MaxKen){
		it=min_element(K.begin(),K.end());
		K.erase(it);
		N.pop_back();
		score++;
	}
	else if(MaxNaomi<MaxKen){
		for(int i=0; i<n; i++){
			if(K[i]>MaxNaomi){K.erase(K.begin()+i); N.pop_back(); break;}
		}
		//destroy element of Ken just above MaxNaomi using iteration;
	}
	}
	return score;
};

int Deceit(vector<double> &N, vector<double> &K, int n){
	score=0;
	MinKen=*K.begin();
	int count=0;
	for(int i=0; i<n; i++){
		if(N[i]>MinKen){break;}
		count++;
	}
	int I=count; int J=0;
	while(I<n&&J<n){
		if(N[I]>K[J]){score++; I++; J++;}
		else if(N[I]<K[J]){I++;}
	}
	return score;
};

int main(){
	vector<double> Naomi;
    vector<double> Ken;
	ifstream infile("D-large.in");
	ofstream outfile;
	outfile.open("2.txt");
	
	infile>>testcases;
	for(int t=1; t<=testcases; t++){
		infile>>N;
		Naomi.clear();
		Ken.clear();
		for(int i=0; i<N; i++){infile>>temp; Naomi.push_back(temp);}
		for(int i=0; i<N; i++){infile>>temp; Ken.push_back(temp);}
		sort(Naomi.begin(),Naomi.end());
		sort(Ken.begin(),Ken.end());
		deceit=Deceit(Naomi, Ken, N);
		war=War(Naomi, Ken, N);
		outfile<<"Case #"<<t<<": "<<deceit<<" "<<war<<endl;
		
}
outfile.close();
return 0;
}
