#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

string toString(int temp){
	if(temp==0)
		return string(1,'0');
	string result;
	while(temp!=0){
		int i=temp%10;
		temp=temp/10;
		result = string(1, i+'0')+result;
	}
	return result;
}

double computeResult(double C, double F, double X){
  double currRate = 2;
  double currTime = X/currRate;
  double nextTime = C/currRate+X/(currRate+F);
  double totalTime = 0;
  while(currTime>nextTime){
    totalTime += C/currRate;
    currRate += F;
    currTime = X/currRate;
    nextTime = C/currRate + X/(currRate+F);
  }
  totalTime+=X/(currRate);
  return totalTime;
}

int main(){
  ifstream infile("B-small-attempt1.in");
  int caseSize;
  infile>>caseSize;
  //cout<<caseSize<<endl;
  for(int i=0; i<caseSize; ++i){
    double C, F, X;
    infile>>C;
    infile>>F;
    infile>>X;
    //cout<<C<<" "<<F<<" "<<X<<endl;
    cout<<setprecision(10);
    cout<<"Case #"<<toString(i+1)<<": "<<computeResult(C, F, X)<<endl;
  }
  return 0;
}
