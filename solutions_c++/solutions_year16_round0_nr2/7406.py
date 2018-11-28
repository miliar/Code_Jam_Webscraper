#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main() {
	ofstream out;
	ifstream in;
	
	out.open("b2.out");
	
	in.open("b2.in");
	
	int t,T;
	in>>T;
	for(t=0;t<T;t++){
		int inv=0,i,len;
		string str;
		in>>str;
		len=str.length();
		for(i=0;i<len-1;i++){
			if(str[i]!=str[i+1])
				inv++;
		}
		if(str[len-1]=='+')
			out<<"Case #"<<t+1<<": "<<inv<<endl;
		else
			out<<"Case #"<<t+1<<": "<<inv+1<<endl;
	}
	return 0;
}
