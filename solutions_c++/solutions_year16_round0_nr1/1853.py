/*
 * main.cpp
 *
 *  Created on: 09-04-2016
 *      Author: Ock
 */

#include <iostream>
#include <fstream>

using namespace std;

int T;
long long N;
ifstream input;
ofstream output;
int i;




void solve() {
	if( N==0){
		output << "Case #" << i << ": INSOMNIA" <<endl;
		return;
	}

	int dig[10];

	for(int j=0;j<=9;j++){
		dig[j]=0;
	}

	for(long long k=N;;k+=N){
		int aux = k;

		while(aux>0){
			int d =aux%10;
			aux/=10;
			dig[d]=1;
		}
		bool allfound= true;
		for(int j=0;j<=9;j++){
			if(dig[j]==0) {
				allfound = false;
				break;
			}
		}
		if(allfound) {
		  output << "Case #" << i << ": "<< k<<endl;
		return;
		}

	}


}



int main(){
	input.open("A-large.in", ifstream::in);
	output.open("output.txt", ofstream::out);

	input >> T;
	//cout <<T<<endl;
	for(i=1;i<=T;++i){
		input>>N;
		solve();
		//cout <<N <<endl;
	}


	input.close();
	output.close();


	return 0;
}
