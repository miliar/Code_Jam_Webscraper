#include <iostream>
using namespace std;

int main() {
	int i,t,n,ii,cnt,dig,temp,mul;
	bool flag[10];
	cin>>t;
	for(ii=1; ii<=t; ii++){
		cin>>n;
		if(n==0){
			cout<<"Case #"<<ii<<": INSOMNIA"<<endl;
			continue;
		}
		else{
			for(i=0; i<=9; i++)	flag[i]=0;
			cnt=0;
			mul=0;
			while(cnt<10){
				mul++;
				temp=mul*n;
				while(temp>0){
					dig = temp%10;
					temp/=10;
					if(flag[dig]==0){
						cnt++;
						flag[dig]=1;
					}
				}
			}
			cout<<"Case #"<<ii<<": "<<n*mul<<endl;
		}
	}
	return 0;
}