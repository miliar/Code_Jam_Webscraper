#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;

int palin(int);
int square(int);
int srpalin(int);

int main(){
	ifstream fin;
	ofstream fout;
	fin.open("C-small-attempt2.in");
	fout.open("output");
	int t,a,u,i,count;
	double b;
	fin>>t;
	for(int j=1;j<=t;j++){
		fin>>a>>u;
		count=0;
		for(i=a;i<=u;i++){
			b = sqrt(i);
			if(palin(i) && square(i) && palin(b)){
			count++;
			}
		}
	cout<<"Case #"<<j<<": "<<count<<endl;
	fout<<"Case #"<<j<<": "<<count<<endl;
	}
}

int palin(int a){
	int temp,remainder,sum=0;
	temp = a;
	while(temp>0){
	      	remainder=temp%10; 
      		temp/=10;                
     		sum=sum*10 + remainder;
	}
	if(sum == a)
		return 1;
	else return 0;
}

int square(int a){
	float root;
	root = sqrt(a);
	if(root*root == a)
		return 1;
	else return 0;
}
