#include <iostream>
#include <cstdlib>
#include<fstream> 
#include<cassert>  
#include<algorithm>
#include<cstring>
#define MAXS 101
using namespace std;
int N,counter=0;
string str;


void scambia(int j) {
	for(int i=0;i<=j;i++) {
		if (str[i]=='+')
			str[i]='-';
		else
			str[i]='+';
	}
}


int main()
{
	ifstream in("input.txt");  
	assert(in);     
	ofstream out("output.txt");
	in>>N;
	for(int i=0;i<N;i++){
		in>>str;
		counter=0;
		for(int j=str.size();j>=0;j--) {
			if (str[j]=='-') {
				scambia(j);
				counter++;
			}
		}
		out<<"Case #"<<i+1<<": "<<counter<<endl;
	}
	return 0;
}

