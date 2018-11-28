#include<iostream>

using namespace std;

int main(){
	int i,t;
	int j=1;
	cin>>t;
	while(j<=t){
		long long n;
		cin>>n;
		int a[11];
		for(i=0;i<=9;i++){
			a[i]=0;
		}
		int d=0;
		long long l=1;
		while(d<10){
			if(n==0){
				break;
			}
			long long k=n*l;
			while(k>0){
				int x=k%10;
				if(a[x]==0){
					a[x]=1;
					d++;
				}
				k/=10;
			}
			if(d==10){
				break;
			}
			l++;

		}
		long long h=l*n;

		cout<<"Case #"<<j<<": ";
		if(n==0){
			cout<<"INSOMNIA"<<endl;
		}else{
			cout<<h<<endl;
		}
		j++;
	}


	return 0;
}