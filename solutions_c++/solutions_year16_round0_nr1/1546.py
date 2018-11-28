#include<iostream>
using namespace std;

long long int N;
int t,T,i,done,a[10],temp,n,mul;

int main(){
	cin>>T;
	for(t=1;t<=T;++t){
		done=0;
		mul=1;
		for(i=0;i<10;++i)
			a[i]=0;

		cin>>N;
		if(N==0)
			cout<<"Case #"<<t<<": INSOMNIA\n";
		else{
			while(done==0){
				temp=N*mul;
				while(temp!=0){
					n=temp%10;
					a[n]=1;
					temp/=10;
				}
				for(i=0;(i<10)&&(a[i]);++i);
				if(i==10)
					done=1;
				else
					++mul;
			}
			cout<<"Case #"<<t<<": "<<N*mul<<'\n';
		}
	}
	return 0;
}
