#include<iostream>
#include <fstream>
using namespace std;
int main(){
	ofstream saida;
	ifstream entrada;
	saida.open ("saida.txt");
	entrada.open ("entrada.txt");
	int t,n,m[5000],c1=0,c2=0,max_delta=0;
	entrada>>t;
	for(int i=0;i<t;i++){
		c1=c2=max_delta=0;
		entrada>>n;
		for(int j=0;j<n;j++){
			entrada>>m[j];
			if(j>0 && m[j]<m[j-1]){
				c1+=m[j-1]-m[j];
				if (m[j-1]-m[j]>max_delta)
					max_delta=m[j-1]-m[j];
			}
			
		}
		for(int j=0;j<n-1;j++){
			if(m[j]>=max_delta)
				c2+=max_delta;
			else
				c2+=m[j];
		}
		saida<<"Case #"<<i+1<<": "<<c1<<" "<<c2<<endl;
	}
	entrada.close();
	saida.close();
	return 0;
}
