#include<iostream>
#include<string>
#include<fstream>
using namespace std;

int cases[] = {0,0,0,0,0,0,0,0,0,0};

bool compare(){
	for(int i=0;i<10;i++){
		if(cases[i]==0)
			return false;
	}
	return true;
}

void mark(long M){
	int n;
	while(M>=10){
		n=M%10;
		cases[n]=1;
		M/=10;

	}
	cases[M]=1;

}
main() {
		long n,N,T,count=1;
	ifstream fin("A-large.in");
	ofstream fout("output.txt");
	fin >> T;
		
	while(T>=1 && T<=100){

		fin >> n;
		if(n>0 && n<=1000000){
			int i=1;
			while(!compare()){
				N=n*i;	
	
				mark(N);
	
				i++;
			}
			
			fout << "Case #"<<count<<": " << N << endl;
			
		}else if(n==0)
			fout << "Case #"<<count<<": " << "INSOMNIA"<< endl;
			
		for(int i=0;i<10;i++)
			(cases[i]=0);
		T--;
		count++;
	}
}
