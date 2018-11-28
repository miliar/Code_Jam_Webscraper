#include <iostream>
#include <stdio.h>
#include <fstream>
using namespace std;

int main(){
	ifstream myin;
	myin.open("B-large.in");
	ofstream myout;
	myout.open("Output2.out");
	int t,i,j;
	double c,f,x,count;
	myin >> t;
	j=0;
	while(t--){
		j++;
		count=0;
		i=0;
		myin >> c >> f >> x ;
		while(x/(2+f*i) >= c/(2+f*i) + x/(2+f+f*i)){
			count+= c/(2+f*i);
			i++;
		}
		count+=x/(2+f*i);
		myout.setf(ios::fixed, ios::floatfield);
		myout.precision(7);
		myout << "Case #"<<j<<": "<<count<<"\n";
	}
	myin.close();
	myout.close();
	return 0;
}