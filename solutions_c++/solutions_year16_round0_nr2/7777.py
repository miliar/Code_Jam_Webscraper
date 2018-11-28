#include<iostream>
#include<string>
#include<string.h>
#include<algorithm>
#include<fstream>
using namespace std;
int main (){
	int n,count,p,j=1,output;
	string m;
	ifstream infile("codejam.txt");
	ofstream offile("output.txt");
    infile>>n;
    while(infile>>m){
    	count = 0;
    	if(m[m.size()-1] == '-')
    	count = 1;
    	 for(int i = m.size()-2; i >=0; i--){
    	 	if(m[i] != m[i+1])
    	 	   count += 1;
		   }
		offile<<"Case #"<<j++<<": ";
			offile<<count<<"\n";
		}

}

