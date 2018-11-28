#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

int main(int argc, char** argv){
	ifstream read("input2.txt");
	string line;
  	int T;
	int count;
  	if (read.is_open()){
  		read>>T;
	for(int i=0; i<T; i++){
		int retVal;
		read>>line;
		count=1;
		for(int j=0; j<line.size()-1; j++){
			if(line[j]!=line[j+1])	count++;
			
			
		}	
		if(count%2){
			if(line[0]=='+')	retVal=count-1;
			else	retVal=count;

		}
		else{
			if(line[0]=='-')	retVal=count-1;
			else	retVal=count;

		}
	int caseNum=i+1;
	cout<<"Case #"<<caseNum<<": "<<retVal<<endl;


	}
			
    read.close();
  }

	return 0;
}

