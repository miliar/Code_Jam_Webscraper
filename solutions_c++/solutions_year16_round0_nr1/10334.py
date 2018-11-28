#include<iostream>
using namespace std;

int main(){
	int tc;
	int sum=0;
	long int num;
	cin>>tc;
	for(int i=1;i<=tc;i++){
		int arr[10]={0};
		sum=0;
		cin>>num;
		int j=1;
		for(j=1;sum<10&&num!=0;j++)
		{
			long int z=num*j;
			while(z!=0)
			{
				int r=z%10;
				//cout<<"num = "<<num<<" : z = "<<z<<" :  r = "<<r<<" : j = "<<j<<" : sum = "<<sum<<endl;
				if(arr[r]!=1){
					arr[r]=1;
					sum++;
				}
				z=z/10;
			}
		}
		cout<<"Case #"<<i<<": ";
		if(sum==0)
		{
			cout<<"INSOMNIA"<<endl;
		}
		else{
			cout<<num*(j-1)<<endl;
		}
	}
	return 0;
}
