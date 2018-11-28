#include<cstdio>
#include<iostream>
using namespace std;
double C,F,X;
double time(int n){
	double aux=0;
	for(int i=0;i<n;i++) aux+=C/(2+F*i);
	aux+=X/(2+F*n);
	return aux;
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w+",stdout);
	int T;
	cin>>T;
	for(int t=0;t<T;t++){
		cout<<"Case #"<<t+1<<": ";
		cin>>C>>F>>X;
		double t1,t0;
		int cont=1;
		t0=time(0);
		while(true){
			t1=time(cont);
			if(t1>t0) break;
			t0=t1;
			cont++;
		}
		printf("%.7f",t0);
		cout<<endl;
	}
	fclose(stdin);
	fclose(stdout);
}
