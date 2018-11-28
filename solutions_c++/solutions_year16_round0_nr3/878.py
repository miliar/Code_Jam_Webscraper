#include<iostream>
#include<cmath>
#include<vector>
#include<string>
#include<fstream>
using namespace std;

unsigned long long isPrime(unsigned long long n){     

	if(n%2==0) return 2;

	double s=sqrt(n);
	for(unsigned long long i=3;i<s;i+=2){
		if(n%i==0){
			return i;
		}
	}

	return 0;
}

unsigned long long conversion(int base,string& jc){
	int l=jc.length();
	unsigned long long num=0,d=1;

	for(int i=l-1;i>=0;i--){
		num+=(jc[i]-48)*d;
		d*=base;
	}

	return num;
}

bool isJamCoin(string& jc,vector<unsigned long long>& div){

	unsigned long long temp;
	for(int i=2;i<11;i++){
		if((temp=isPrime(conversion(i,jc)))!=0){
			div[i-2]=temp;
		}else{
			return false;
		}
	}

	return true;
}

void createjamcoin(int n,int j,vector<string>& jc,vector<vector<unsigned long long>>& div){

	int count=0;
	string c="1";
	for(int i=1;i<n-1;i++){
		c+='0';
	}
	c+='1';

	vector<unsigned long long> temp;
	temp.resize(9);

	int k;
	while(count<j){
		k=n-2;
		while(c[k]=='1'&&k>0){
			c[k--]='0';
		}
		c[k]='1';
		if(isJamCoin(c,temp)){
			//cout<<c<<'\n';
			jc.push_back(c);
			div.push_back(temp);
			count++;
		}
	}
}

void main(){

	fstream infile,outfile;
	int testnum,n,j;
	infile.open("C-small-attempt0.in",ios::in);
	outfile.open("output.dat",ios::out);	
	infile>>testnum;
	infile>>n;
	infile>>j;

	vector<string> jamcoins;
	vector<vector<unsigned long long>> divisors;

	createjamcoin(n,j,jamcoins,divisors);

	outfile<<"Case #"<<1<<":\n";
	for(int i=0;i<j;i++){
		outfile<<jamcoins[i]<<" ";
		for(int k=0;k<9;k++){
			outfile<<divisors[i][k]<<" ";
		}
		outfile<<'\n';
	}

	/*for(int i=0;i<500;i++){
		cout<<i+1<<"th jamcoin: "<<jamcoins[i]<<'\n';
		cout<<"its divisors: ";
		for(int k=0;k<9;k++){
			cout<<divisors[i][k]<<" ";
		}
		cout<<"\n\n";
	}

	cout<<jamcoins.size()<<'\n';*/
}
