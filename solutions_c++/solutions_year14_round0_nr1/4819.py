#include<iostream>
#include<fstream>
using namespace std;

static int numbers[4];

bool findNumber(int number){
	for(int i=0;i<4;++i)
		if(numbers[i]==number)
			return true;
	return false;
}

int main(){

	ifstream input;
	ofstream output;
	input.open("1a.in");
	output.open("1a.out");


	int T;
	input>>T;

	int line;
	int dump;
	int result;

	for(int i=0;i<T;++i){
		result=0;
		input>>line;
		for(int j=0;j<4*(line-1);++j)
			input>>dump;
		for(int j=0;j<4;++j)
			input>>numbers[j];
		for(int j=0;j<4*(4-line);++j)
			input>>dump;

		input>>line;
		for(int j=0;j<4*(line-1);++j)
			input>>dump;
		for(int j=0;j<4;++j){
			input>>dump;
			if(findNumber(dump)){
				if(result==0){
					result=dump;
					continue;
				} else
					result=-1;
			}
		}
		for(int j=0;j<4*(4-line);++j)
			input>>dump;

		output<<"Case #"<<1+i<<": ";
		switch(result){
		case 0:
			output<<"Volunteer cheated!";
			break;
		case -1:
			output<<"Bad magician!";
			break;
		default:
			output<<result;
		}
		output<<"\n";
	}

	input.close();
	return 0;


}
