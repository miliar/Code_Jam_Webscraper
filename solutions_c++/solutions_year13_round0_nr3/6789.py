#include <iostream>
#include <vector>
#include <fstream>

using namespace std;


bool is_palindrom(double a){
	bool t=false;
	int b=a;
	double b1=0;
	double temp=0;
	char count[25];
	_itoa_s(a,count,10);
	int c=strlen(count);
	while(b>0){
	temp=b%10;
	b1=b1+temp*pow(10,c-1);
	c--;
	b=b/10;
	}
	if(b1==a){t=true;}else{t=false;}
	return t;
}

int count(int st,int fn){
	vector<double> a;
	vector<double> a1;
	int k=0;
	for(int i=st;i<=fn;i++){
			a.push_back(i);
			a1.push_back(sqrt(i));
		}
	for(int i=0;i<=fn-st;i++){
		if(is_palindrom(a[i])==true )
			if(is_palindrom(a1[i])==true){
			k++;}
	}
	return k;
}

void main(){
	ifstream file("C-small-attempt1.in");
	ofstream file1("answer.txt");
	int n;
	int g;
	vector<int> a;
	vector<int> start;
	vector<int> finish;
	file>>n;
	int* k=new int[n];
	while(file){
		file>>g;
		a.push_back(g);
	}
	for(int j=0;j<2*n;j+=2){
		start.push_back(a[j]);
		finish.push_back(a[j+1]);
	}
	
	for(int j=0;j<n;j++){
		k[j]=count(start[j],finish[j]);
	}
	for(int j=0;j<n;j++){
		file1<<"Case #"<<j+1<<": "<<k[j]<<endl;
	}
}