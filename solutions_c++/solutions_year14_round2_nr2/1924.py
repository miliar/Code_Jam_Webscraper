#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;

int N;
int A,B,K;
long long ans;
void showAns(int round, ofstream& file){
	file<<"Case #"<<round<<": "<<ans<<endl;
	return;
}

void getAns(){
	ans=0;
	for(int i = 0 ; i < A;++i){
		for(int j = 0; j < B;++j){
			int temp = i&j;
			if (temp<K)
				++ans;

		}
	}
}

void main(){
	ifstream file("B-small-attempt2.in");
	if(!file)
		return;
	int T = 0;
	file>>T;
	ofstream outfile("output");
	for(int idx = 1; idx<=T; ++idx){
		file>>A>>B>>K;
		
		getAns();

		showAns(idx,outfile);	
	}
	outfile.close();
	file.close();

}



