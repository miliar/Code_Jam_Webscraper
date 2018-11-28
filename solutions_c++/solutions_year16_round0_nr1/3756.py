#include <iostream>
#include <stdlib.h>
#include <string.h>
using namespace std;

int main(){
	int T,N,n,numVistos,i;
	char aux[6];
	bool vistos[10];
	cin>>T;
	for(i=1;i<=T;i++){
		for(int k=0;k<10;k++) vistos[k] = false;
		numVistos=0;
		n=0;
		
		cin>>N;
		
		if(N==0) cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		else{
			while(numVistos<10){
				n+=N;
				itoa(n,aux,10);
				int pos = 0;
				while(pos<strlen(aux)){
					if(!vistos[aux[pos]-'0']){
						vistos[aux[pos]-'0']=true;
						numVistos++;
					}
					pos++;
				}
			}
			cout<<"Case #"<<i<<": "<<n<<endl;
		}
	}
}
