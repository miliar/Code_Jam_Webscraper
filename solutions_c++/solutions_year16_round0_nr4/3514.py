#include <iostream>
#include <string>
using namespace std;


int main() {
	
	int caseNum, K,C,S;
	cin>>caseNum;
	for(int i = 0; i<caseNum  ;i++)
	{
		cin>>K>>C>>S;
		cout<<"Case #"<<i+1<<":";
		for(int j=0;j< S; j++) {
			cout<<" "<<j+1;
		}
		cout<<endl;
	}
	// your code goes here
	return 0;
}