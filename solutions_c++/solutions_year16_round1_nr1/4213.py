#include<iostream>
#include<iomanip>
#include<sstream>

using namespace std;

string last(string s){
	string temp=s.substr(0,1);
	char c;
	char compare;

	for(int i=1; i<s.length(); ++i){
		c=s[i]-'A';
		compare=temp[0]-'A';

		if(c>=compare){
			temp=s[i]+temp;
		}else{
			temp=temp+s[i];
		}
	}

	return temp;

}


int main(){
	int total;
	cin>>total;


	string test;
	int case_num=1;

	for(int j=0; j<total; ++j){

		cin>>test;
		string t=last(test);
		cout<<"Case #"<<case_num<<": "<<t<<endl;

		++case_num;
	}

}



