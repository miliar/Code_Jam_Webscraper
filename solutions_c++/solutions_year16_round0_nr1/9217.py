#include <iostream>
using namespace std;
typedef long long ll;
int main(){
	ll t,n,i,j,temp,a[10],flag,tp;
	cin>>t;
	j=0;
	while(t--){
		j++;
		cin>>n;
		tp=n;
		for(i=0;i<10;i++)
			a[i]=0;
		if(n==0){
			cout<<"Case #"<<j<<": "<<"INSOMNIA\n";
			continue;
		}
		while(1){
			temp=n;
			//cout<<temp<<"\n";
			while(temp){
				a[temp%10]++;
				temp/=10;
			}
			flag=1;
			for(i=0;i<10;i++){
				//cout<<a[i]<<" ";
				if(a[i]==0){
					flag=0;
					break;
				}
			}
			//cout<<"\n";
			if(flag){
				cout<<"Case #"<<j<<": "<<n<<"\n";
				break;
			}
			n+=tp;
		}
	}
	return 0;
}