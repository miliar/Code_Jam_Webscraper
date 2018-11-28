#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <sstream>
using namespace std;


double stringToNumber (const string &Text )
{                               
	stringstream ss(Text);
	double result;
	return ss >> result ? result : 0;
}

string numberToString(const long number){
	string result;
	stringstream convert;
	convert<<number;
	return convert.str();
}
	
void solveCountSheep(double input,double caseno,ofstream &out);
bool checkArray(int* arr);
void updateChecker(int *checker,long input);

int main(){
	long cases,num;
	string temp;
	ifstream in("A-large.in");
	ofstream out("output.txt");
	getline(in,temp);
	cases=stringToNumber(temp);
	for(long i=0;i<cases;i++){
		getline(in,temp);
		num=stringToNumber(temp);
		solveCountSheep(num,(i+1),out);
	}
	in.close();
	out.close();
}

void solveCountSheep(double input,double caseno,ofstream &out){
	if(input==0){
		out<<"Case #"<<caseno<<": "<<"INSOMNIA"<<endl;
	}
	else{
		int *checker=new int[10];
		for(int i=0;i<10;i++){
			checker[i]=0;
		}
		long in=input;
		long origin=input;
		int num=2;
		long res=in;
		while(checkArray(checker)){
			updateChecker(checker,in);
			res=in;
			in=origin*num;
			num++;
		}
		out<<"Case #"<<caseno<<": "<<res<<endl;
	}	
}

bool checkArray(int* arr){
	bool out=false;
	for(int i=0;i<10;i++){
		if(arr[i]==0){
			out=true;
		}
	}
	return out;
}

void updateChecker(int *checker,long input){
	string strNum=numberToString(input);
	for(int i=0;i<strNum.length();i++){
		int index=(int(strNum[i]))-48;
		//cout<<index<<endl;
		checker[index]++;
	}
	//cout<<"CHECKER VALUES!"<<endl;
	// for(double i=0;i<10;i++){
	// 	//cout<<checker[i]<<"!";
	// }
}