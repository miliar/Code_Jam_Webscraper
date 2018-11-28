
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <sstream>
#include <map>

using namespace std;

int T,I,N;
int**lines;


ifstream input;
ofstream output;

typedef unsigned long long ull;

void solve() {
	map<int,int> counter;
	for(int j=0;j<2*N-1;++j){
		for(int i=0;i<N;++i){
		  if(counter.find(lines[j][i])==counter.end()){
			  counter[lines[j][i]] = 1;
  		  } else{
			  counter[lines[j][i]] =  counter[lines[j][i]] +1;
		  }
		}
	}

	//Find nonrepeating
	int ind = -1;
    cout << "row ";
    output << "Case #" << I << ":";
    for(map<int,int>::iterator it = counter.begin();it!=counter.end();++it){
    	if(it->second%2== 1) {
    		ind = it->first;
    		cout << ind;
    		output << " " << ind;
    	}
    }

    cout <<endl;
    output<<endl;



}



int main(){
	input.open("B-large.in", ifstream::in);
	output.open("output.txt", ofstream::out);

	input >> T;
	for(I=1;I<=T;++I){
		input >> N;
		cout << N << endl;

		lines = new int*[2*N-1];
		for(int j=0;j<2*N-1;++j){
			lines[j] = new int[N];
			for(int i = 0 ;i<N;++i){
				input >> lines[j][i];
			}
		}

		solve();
		//output << "Case #" << i << ": " << sol << endl;
		for(int j=0;j<2*N-1;++j){
			delete lines[j];
		}
		delete lines;

	}


	input.close();
	output.close();


	return 0;
}




