#include <iostream>
using namespace std;

int c(int d[]){
	for(int j=0; j<10; j++){
			if (d[j]==0){
				return 0;
			}
		}
		return 1;
}
void m(int x, int d[]){
	int a;
	for(int i=0; i<10; i++){
		a=x%10;
		x=x/10;
		d[a]=1;
		if(x<=0){
			break;
		}
	}
}

int main() {
	int t, n, d[10], j;
	long int x;
	cin>>t;
	for(int i=1; i<=t; i++){
		cin>>n;
		x=n;
		cout<<"Case #"<<i<<": ";
		for(j=0; j<10; j++){
			d[j]=0;
		}
		if(n==0){
			cout<<"INSOMNIA"<<endl;
		}else{
			for(j=1; j<30000; j++){
				m(x,d);
				if(c(d)){
					cout<<x<<endl;
					break;
				}
				x+=n;
			}
		}
		if (j>=30000){
			cout<<"INSOMNIA"<<endl;
		}
	}
	return 0;
}
