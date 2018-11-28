#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
using namespace std;
int done();		//return 1 when numbers completed....
long T;
long N,K,R;
int A[10]={0};
ifstream f("A-large.in");
ofstream f2("output.txt");
int main(){
f >>T;
for(long j=1;j<=T;j++){
	for(int i=0;i<10;i++)
		A[i]=0;
	f>>N;
	for(int i=1;i<=100;i++){
		if(done())
			break;
		else{
			K=N*i;
			R=K;
			while(K!=0){
				int digit=K%10;
				A[digit]=1;
				K=K/10;
			}
			
		}
	}
	stringstream buffer;
	buffer<<"Case #"<<j<<": ";
	if(done())
		buffer<<R<<endl;
	else{
		
		buffer<<"INSOMNIA"<<endl;
	
	}
		
	f2 << buffer.str();
	
	
}
f.close();
f2.close();
	return 0;
}

int done(){
	
	for(int i=0;i<10;i++){
		if(A[i] == 0)
			return 0;
	}
return 1;	
}


