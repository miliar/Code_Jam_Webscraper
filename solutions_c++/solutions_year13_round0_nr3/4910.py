#include<iostream>
#include<fstream>
#include <stdio.h>
#include <math.h>
#include<string>
#include<sstream>
using namespace std;
int func (int res){
	string Result;          

	ostringstream convert;   

	convert << res;      

	Result = convert.str();
	//cout<<Result<<endl;
	for(int l=0; l<=Result.size()/2 ; l++)
		if(Result[l] != Result[Result.size()-1-l])
			return 0;

	return 1;
}
int main(){
	
	ifstream in("C-small-attempt0.in");
	ofstream out("outttt.txt");
	int t;
	in>>t;
	for(int i = 0 ; i < t; i++){
		double a,b;
		double count;
		count =0;
		in>>a>>b;
		double result;
		int res;
		for(double j=a ; j<=b; j++){
			result = sqrt (j);
			res = (int )result;
			if(result - res == 0){
				int z = func(j);
				if(z == 1){
					if(func(result) == 1)
						count++;
				}
			}
		}
		out<<"Case #"<<i+1<<": "<<count<<endl;
		
	}
	return 0;
}
