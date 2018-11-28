#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <sstream>
using namespace std;

double stringToNumber (const string &Text );
void solvePancake(string input,int caseno,ofstream &out);
string flipCakes(string cakes,int rpoint,int* count);
int main(){
	long cases;
	string temp;
	ifstream in("B-large.in");
	ofstream out("output3.txt");
	getline(in,temp);
	cases=stringToNumber(temp);
	for(long i=0;i<cases;i++){
		getline(in,temp);
		solvePancake(temp,i,out);
	}
	in.close();
	out.close();
}



double stringToNumber (const string &Text )
{                               
	stringstream ss(Text);
	double result;
	return ss >> result ? result : 0;
}

void solvePancake(string input,int caseno,ofstream &out){
	int top=0,rpoint=input.length()-1;
	int *count=new int;*count=0;
	string cakes=input;
	while(true){
		while(cakes[rpoint]=='+' && rpoint>0){
			rpoint--;
		}
		if(top==rpoint && cakes[top]=='+'){
			break;
		}
		else if(top==rpoint && cakes[top]=='-'){
			cakes=flipCakes(cakes,rpoint,count);
			break;
		}
		else if(cakes[rpoint]=='-' && cakes[top]=='+'){
			int temptop=top;
			while(cakes[temptop+1]=='+'){
				temptop++;
			}
			cakes=flipCakes(cakes,temptop,count);
			cakes=flipCakes(cakes,rpoint,count);		}
		else if(cakes[rpoint]=='-'&& cakes[top]=='-'){
			cakes=flipCakes(cakes,rpoint,count);
		}
	}
	out<<"Case #"<<(caseno+1)<<": "<<(*count)<<endl;
}

string flipCakes(string cakes,int rpoint,int* count){
	string outcakes=cakes;
	*count=(*count)+1;
	int top=0;
	for(int i=0;i<=rpoint;i++){
		if(outcakes[i]=='-'){
			outcakes[i]='+';
		}
		else if(outcakes[i]=='+'){
			outcakes[i]='-';
		}
	}
	while(top<rpoint){
		char temp=outcakes[rpoint];
		outcakes[rpoint]=outcakes[top];
		outcakes[top]=temp;
		top++;
		rpoint--;
	}
	return outcakes;
}












