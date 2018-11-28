#include <iostream>

using namespace std;

long int c[10];

void split(long int n){
	long long int j;
	while(n>0){
		j=n%10;
		if(c[j]==0){
			c[j]=1;
		}
		n=n/10;
	}
}

int main(){
	long long int i,j,k,t,n,x;
	cin>>t;
	for(x=1;x<=t;x++){
		cin>>n;
		bool l=false;
		i=1;
		for(j=0;j<10;j++)
			c[j]=0;
		if(n!=0){
			while(l==false){
				k=(i*n);
				split(k);
				i+=1;
				l=true;
				for(j=0;j<10;j++)
					if(c[j]==0)
						l=false;
			}
			cout<<"Case #"<<x<<": "<<k<<endl;
		}
		else cout<<"Case #"<<x<<": "<<"INSOMNIA"<<endl;
		
	}
	return 0;
}