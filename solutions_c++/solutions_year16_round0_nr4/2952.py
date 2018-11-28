#include<iostream>
#include<fstream>
using namespace std;
class sol{};
int main(){
sol s;
ifstream is("D-small-attempt0.in");
ofstream os("Output.txt");
int num,K,C,S;
is>>num;
for(int i=1;i<=num;i++){
	is>>K>>C>>S;
	os<<"Case #"<<i<<":";
	for(int j=1;j<=K;j++){
		os<<" "<<j;
	}
	os<<"\n";
}
}