#include <iostream>
using namespace std;

int main(){
	int t, n, aux;

	cin>>t;
	for(int i=0;i<t;i++){
		cin>>n;
		int k=0;
		int num[10]={0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		bool end=false;
		while(!end){
			k++;
			aux=n*k;
			while(aux>0){
				num[aux%10]=1;
				aux=aux/10;
			}
			end=true;
			if(n!=0){
				for(int j=0;j<10 && end;j++){
					if(num[j]==0){
						end=false;
					}
				}
			}
		}
		if(n==0){
			cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
		}
		else{
			cout<<"Case #"<<i+1<<": "<<n*k<<endl;
		}
	}
}