#include <iostream>       // std::cout
#include <string>         // std::string
#include <stdio.h>
using namespace std;

long long flips(string cakes){
	long long a;
	int i=0;
	char current_face=cakes[0];
	a=0;
	for(i=1;i<cakes.length();i++){
		if(current_face!=cakes[i]){
			a++;
			current_face=cakes[i];
		}
	}
	if(current_face=='-'){
		a++;
	}
	return a;
}

int main(){
	int N,i;
	string cakes;
	cin>>N;
	getline(cin,cakes);
	for(i=0;i<N;i++){
		getline(cin,cakes);
		cout<<"Case #"<<i+1<<": "<<flips(cakes)<<"\n";
	//	printf("%ld\n",flips(cakes));
	}
	
	return 0;
}
