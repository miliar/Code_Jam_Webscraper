#include <iostream>
using namespace std;

int main(){
	int T,S;
	//unsigned long long int posiciones[110];
	unsigned long long int K,C,KCmenos1;
	cin>>T;
	for(int i=0;i<T;i++){
		cin>>K>>C>>S;
		KCmenos1=1;
		
		cout<<"Case #"<<(i+1)<<":";
		
		for(int l=1;l<C;l++) KCmenos1*=K;
		for(int j=0;j<S;j++){
			//3*0+1
			//3*1+1
			//3*2+1
			//K^(C-1)*0+1
			//.
			//.
			//.
			//K^(C-1)*(K-1)+1
			cout<<" "<<KCmenos1*j+1;
			//posiciones[j]=KCmenos1*j+1;
		}
		cout<<endl;
		
	}
}
