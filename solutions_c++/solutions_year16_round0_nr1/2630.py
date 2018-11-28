#include <iostream>
#include <vector>
#include <set>
#include <fstream>
using namespace std;

void splitNumber(std::set<int>& digits, int number) {
	if (0 == number) { 
		digits.insert(0);
	} else {
		while (number != 0) {
			int last = number % 10;
			digits.insert(last);
			number = (number - last) / 10;
		}
	}
}

void printv(std::set<int>& digits){
	for(set<int>::iterator i=digits.begin();i!=digits.end();i++) { 
		cout<<*i;
	}
}

int main(int argc, char *argv[]) {
	int T;
	
	ifstream input(argv[1]);
	if(!input.is_open()){
		cerr<<"ERROR: can't open file "<<argv[1]<<endl;
		return -1;
	}
	ofstream output((static_cast<string>(argv[1])+".out").c_str());
	input>>T;
	
	for(int i=0;i<T;i++) { 
		cout<<"- Test CASE #"<<i<<endl;
		int N;
		input>>N;
		
		if(N==0){
			output<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		}else{
			int c=1;
			set<int> seenDigits;
			int NN = N;
			
			splitNumber(seenDigits, N);
			cout<<"Count: "<<c<<"    Number: "<<NN<<"    Digits: ";
			printv(seenDigits);
			cout<<endl;
			while(seenDigits.size()<10){
				NN += N;
				splitNumber(seenDigits, NN);
				c++;
				cout<<"Count: "<<c<<"    Number: "<<NN<<"    Digits: ";
				printv(seenDigits);
				cout<<endl;
			}
			output<<"Case #"<<i+1<<": "<<NN<<endl;
		}
		
		
		
	}
	input.close();
	output.close();
	return 0;
}

