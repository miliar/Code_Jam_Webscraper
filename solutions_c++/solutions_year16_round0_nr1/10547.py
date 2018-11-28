#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

struct data{
	int num;
	bool predicate;
} cases[10];

int checkPredicate(){
	int counter=0;
	for (int i = 0; i < 10; ++i){
		if(cases[i].predicate == 0){
			counter++;
		}
	}
	return counter == 10 ? 1 : 0;
}

int check(int params){
	cases[params].predicate=false;
	return checkPredicate() == 1 ? 0 : 1;
}

void createData(){
	for(int i=0;i<10;i++){
		cases[i].num=i;
		cases[i].predicate=true;
	}
}

int main(int argc, char* argv[]){

	ifstream input;
	ofstream output;

	input.open(argv[1]);
	output.open(argv[2]);

	int testCases;
	input>>testCases;
	for(int k = 0; k < testCases; ++k){
		int N, out;
		input>>N;
		createData();
		int loopEnd = 1;
		if(N==0){
			loopEnd = 0;
		}
		for(int i = 1;loopEnd==1;i++){
				int temp = N*i;
				out = temp;
				while(temp>=1){
					if(temp>=10){
						loopEnd = check(temp%10);
					}else{
						loopEnd = check(temp);
					}
					temp = temp/10;
				}
		}
		if(N==0){
			output<<"Case #"<<k+1<<": "<<"INSOMNIA"<<endl;
		}else{
			output<<"Case #"<<k+1<<": "<<out<<endl;
		}
	}


	return 0;
}

