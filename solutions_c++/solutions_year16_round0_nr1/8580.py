#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool seen[20]={false};
ifstream in ("a.in");
ofstream out ("a.out");

int t;

bool add_seen(int n){
	while(n>0){
		seen[n%10]=true;
		n/=10;
	}
	bool all=true;
	for(int x=0;x<=9;x++)
		all=all&&seen[x];
	return all;		
}

int main(){
	in>>t;
	for(int x=0;x<t;x++){
		int n;
		in>>n;
		if(n==0){
			out<<"Case #"<<(x+1)<<": INSOMNIA"<<endl;
			continue;
		}
		int c=1;
		while(!add_seen(n*c)){
			c++;
		}		
		out<<"Case #"<<(x+1)<<": "<<(n*c)<<endl;
		for(int z=0;z<=9;z++)
			seen[z]=false;
	}
	
}
