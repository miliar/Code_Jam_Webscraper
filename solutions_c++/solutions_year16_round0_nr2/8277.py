#include<iostream>
using namespace std;


int flipPancake(string p){
	if(p.find_last_of('-') == string::npos ) return 0;

	int flipCount = 0;
	int flipPos = p.find_last_of('-');
	string stack1, stack2;
	do{
		if( flipPos == p.length()-1 ){
			stack1 = p;
		} else {
			stack1 = p.substr(0, flipPos);
			stack2 = p.substr(flipPos+1, p.length()-1);
		}
		
		//flip stack1
		replace(stack1.begin(), stack1.end(), '-', '*');
		replace(stack1.begin(), stack1.end(), '+', '-');	
		replace(stack1.begin(), stack1.end(), '*', '+');	
		p = stack1 + stack2;

		flipCount++;
		flipPos = p.find_last_of('-');

	} while(flipPos != string::npos);

	return flipCount;
}


int main(){

	int t;
	string p;
	cin >> t;
	for(int i=1; i<=t; i++){
		cin >> p;
		cout<<"Case #"<<i<<": "<<flipPancake(p)<<endl;
	}

	return -1;
}