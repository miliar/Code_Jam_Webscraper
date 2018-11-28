#include <iostream>
#include <fstream>
using namespace std;
#define rr 		freopen("input.txt", "r", stdin)
#define wr 		freopen("output.txt", "w", stdout)
void dig(long long int N,int b[],int &count){
    while(N>0){
    	if(b[N%10]!=1){
    		b[N%10]=1;
    		count++;
    	}
    	N/=10;
    }
}
int main() {
    ios::sync_with_stdio(0);
    rr;
    wr;
	long long int i,j,N,T,l;
	cin>>T;
	for(j=1;j<=T;j++){
		cin>>N;
		if(N>0){
		int b[10]={0},k=0;
		for(i=1;k<10;i++){
			dig(i*N,b,k);
		}
		cout<<"Case #"<<j<<": "<<(i-1)*N<<endl;
		}
		else{
			cout<<"Case #"<<j<<": INSOMNIA"<<endl;
		}
		
	}
	return 0;
}

