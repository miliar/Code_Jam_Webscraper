#include "fstream"
#include <string>

using namespace std;
 int main(){

fstream in,out;
in.open("A-small-attempt0.in",ios::in);
out.open("output.txt",ios::out);

int numero_test;
in>>numero_test;

for(int i=0;i<numero_test;i++){
	int smax;
	in>>smax;
	int tutti[smax+1];
	int b;
	in>>b;
	for(int j = smax; j >= 0; j--){
		tutti[j] = b%10;
		b/=10;
	}
	int numavanti=0;
	int numeroamici=0;
	for(int j=0;j<smax+1;j++){
		if(numavanti<j){
	numeroamici++;
	numavanti++;
	}
	if(numavanti>=j){
	numavanti+=tutti[j];
	}

	}
	out<<"Case #"<<i+1<<":"<<" "<<numeroamici<<endl;
}

}

