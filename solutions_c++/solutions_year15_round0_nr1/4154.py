#include<iostream>
#include<fstream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

long long int findNo(){
	long long int total=0,ans=0,last_count=0;
	fin>>total;
	char ch;
	int p=0;
	for(long long int level=0;level<=total;level++){
		fin>>ch;
		p=int(ch)-48;
		if(p>0){
			if(last_count>=level){
				last_count+=p;
			}
			else{
				long long int temp=level-last_count;
				ans+=temp;
				last_count+=temp+p;
			}
		}
	}
	return ans;
}


void main(){

	long long int tc;
	fin>>tc;
	for(long long int i=1;i<=tc;i++){
		fout<<"Case #"<<i<<": "<<findNo()<<"\n";
	}
}