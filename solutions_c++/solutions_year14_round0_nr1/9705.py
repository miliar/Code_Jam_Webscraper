#include <string>
#include <fstream>
#include <set>
#include <iostream>
using namespace std;

string toString(int temp){
	if(temp==0)
		return string(1,'0');
	string result;
	while(temp!=0){
		int i=temp%10;
		temp=temp/10;
		result = string(1, i+'0')+result;
	}
	return result;
}
void checkTrick(const char *fileName){
  ifstream infile(fileName);
	int testCaseSize;
	set<int> firstRow;
	infile>>testCaseSize;
	for(int i=0; i<testCaseSize; ++i){
		int firstInput;
		infile>>firstInput;
		firstRow.clear();
		for(int j=0; j<16; ++j){
			int temp;
			infile>>temp;
			if(j/4==firstInput-1){
				firstRow.insert(temp);
				//cout<<temp<<endl;
			}
		}
		int secondInput;
		infile>>secondInput;
		int countMatch = 0;
		int result;
		for(int j=0; j<16; ++j){
			int temp;
			infile>>temp;
			if(j/4 == secondInput-1){
				if(firstRow.find(temp)!=firstRow.end()){
					++countMatch;
					result = temp;
				}
			}
		}
		if(countMatch==0)
		  cout<<"Case #"<<toString(i+1)<<": Volunteer cheated!"<<endl;
		else if(countMatch==1)
		  cout<<"Case #"<<toString(i+1)<<": "<<toString(result)<<endl;
		else
		  cout<<"Case #"<<toString(i+1)<<": Bad magician!"<<endl;
	}
}

int main(){
	char name[] = "A-small-attempt6.in";
	checkTrick(name);
	return 0;
}
