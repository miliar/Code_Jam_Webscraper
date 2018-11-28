#include<iostream>
#include<fstream>
#include<string>
#include<math.h>
using namespace std;
long int *a;
long long int notprime(long long int n){
	int check=0;
	for(long int i=2;i<=sqrt(n);i++){
		if(n%i==0)return i;
		//cout<<"ad";
	}
	
	return 0;
}


int checkforit(long long int n){
	int count=0,req;
	a[10]=notprime(n);
	if(a[10]==0)return 0;
	for(int i=2;i<10;i++){
		long long int dupe=n;
		long long int sum=0;
		int j=0;
		//cout<<n;
		while(dupe>0){
			int d = dupe%10;
			sum = sum + d*pow(i,j);
			j++;
			dupe = dupe/10;
			//cout<<" a ";
			//cout<<"a";
		}
		req = notprime(sum);
		if(req==0)return 0;
		a[i]=req;
	}
	return 1;
}

int isit(long long int n){
	while(n>0){
		if(!(n%10==1 || n%10 == 0) )return 0;
		n=n/10;
	}
	return 1;
}

int main(){
	ifstream fin("A-large.in");
	ofstream fout("gcj1.out");
	int J,testcases;
	fin>>testcases;
	int y=0;
	//y++;
	while(y<testcases){
		fin>>J;
		int num;
		fin>>num;
		a = new long int[11];
		long long int required;
		J--;
		long long int start = pow(10,J);
		//start = start - 10;
		//cout<<start;
		
		fout<<"Case #"<<y+1<<":"<<"\n";
		//checkforit(100231);
		for(int i=0;i<num;i++){
			do{
				start = start+1;
				required = start;
				//cout<<" a ";
				if(start%10 ==1 && isit(start) && checkforit(start))break;
			}while(1);
			fout<<start<<" ";
			for(int k=2;k<=10;k++)fout<<a[k]<<" ";
			fout<<"\n";
			}
			y++;
		
	}
	fin.close();
	fout.close();
		
	return 0;
}
