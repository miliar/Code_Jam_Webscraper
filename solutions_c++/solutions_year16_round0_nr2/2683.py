#include <iostream>
#include <vector>
#include <set>
#include <fstream>
using namespace std;


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
		cout<<"- Test CASE #"<<i+1<<endl;
		string stack;
		int moves = 0;
		char currentFace;
		
		input>>stack;
		currentFace = stack[0];
		for(int j = 1; j<stack.size(); j++){
			if(stack[j] != currentFace){
				currentFace = stack[j];
				moves++;
			}
		}
		if(currentFace=='-') moves++;
		
		
		output<<"Case #"<<i+1<<": "<<moves<<endl;
		
		
		
		
	}
	input.close();
	output.close();
	return 0;
}

