#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
int main() {
	ifstream fin("a.txt");
	ofstream fout("output.txt");
	int T; fin>>T;
	for(int t = 1;t<=T;t++) {
		
		double C,F,X;
		fin>>C>>F>>X;
		double start = C*(2.0+F)/F;
		double res = 0.0;
		if(X < start) {
			res = X/2.0;
		}
		else {
		   res = C/2.0;
		   double original = X;
		   X-= start;
		   double speed = 2.0+F;
		   while(X > C) {
			   res+= (C/speed);
			   X-=C;
			   speed += F;
		   }
		   res+= (original/speed);
		}
		char arr[501];
		sprintf(arr,"%0.8f",res);
		fout<<"Case #"<<t<<": ";
		fout<<arr<<"\n";
	}
	fin.close();
	fout.close();
}