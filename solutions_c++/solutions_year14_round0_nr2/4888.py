#include<iostream>
#include<fstream>
#include<iomanip>

using namespace std;

float val, C, F, X;
int testcases, count;
float A[10000];

float calx(int k){
	val=X/(2+k*F);
	while(k>0){
		val+=(C/(2+(k-1)*F));
		k--;
	}
	return val;
};

int main(){
	ifstream infile("B-small-attempt5.in");
	ofstream outfile;
	outfile.open("2.txt");
	
	infile>>testcases;
	for(int t=1; t<=testcases; t++){
	infile>>C>>F>>X;
    A[0]=calx(0);
	A[1]=calx(1);
	count=0;

	while(A[count+1]<A[count]){
		A[count+2]=calx(count+2);
		count++;
	}
	
	if(A[count+1]>=A[count]){outfile<<"Case #"<<t<<": "<<setprecision(20)<<A[count]<<endl;}
	
}
	
outfile.close();
return 0;
}

