#include<iostream>
using namespace std;

int main(){
	long int t,n,i,j,a,count,b;
	cin>>t;
	long int test=t;
	while(t--){
		cin>>n;
		b=1;
		j=n;
		long int z[10]={0};
		if(n==0)
			cout<<"case #"<<test-t<<": "<<"INSOMNIA"<<endl;
		else{
			while(true){	
				a=j;
				while(a){
					z[a%10]++;
					a/=10;
				}
				count=0;
				for(i=0;i<10;i++){
					if(z[i]==0)
						count++;
				}
				if(count==0)
					break;
				b++;
				j=b*n;

			}
			cout<<"case #"<<test-t<<": "<<j<<endl;;
		}	
	}
}
