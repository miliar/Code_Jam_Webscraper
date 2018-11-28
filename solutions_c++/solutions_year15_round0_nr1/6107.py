#include<iostream>
#include<string>
#include<fstream>
using namespace std;

int main()
{
	ofstream output;
	output.open("outl.txt");
	ifstream input;
	input.open("A-large.in");
	int t, j=1;
	input>>t;
	while(j<=t){
		int S, friends = 0, count = 0;
		input>>S;
		string str;
		input>>str;
		for(int i=1;i<=S;i++){
			count += str.at(i-1) - 48;
			if(count<i && (str.at(i)-48 != 0)){
				friends += i - count;
				count += i - count;
			}
		}
		output<<"Case #"<<j<<": "<<friends<<endl;
		j++;
	}
	return 0;
}
