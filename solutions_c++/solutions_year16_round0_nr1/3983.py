#include<iostream>
#include<string.h>
using namespace std;



int main(){

	int t,n,i=0,flag,k;
	long long ans;
	int boo;
	cin>>t;
	while(i<t){
			i++;
		flag=0;
		boo=0;
		int a[10]={0};
		cin>>n;
		if(n==0){
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
			continue;
			}
		long long m=n;
		k=0;
		while(boo==0){
		k++;
		m=k*n;
		ans=m;
		while(m!=0){
			int l=m%10;
			m/=10;
			if(a[l]==0){
				a[l]++;
				flag++;
			}
			if(flag==10){
				boo=1;
				break;
			}
		}
		}
		if(flag==10){
			cout<<"Case #"<<i<<": "<<ans<<endl;
		}
		else{
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		}
	
	}

return 0;
}
