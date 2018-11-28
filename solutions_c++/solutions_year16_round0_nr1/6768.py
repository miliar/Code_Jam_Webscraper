#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large-practice.out","w",stdout);
	
	long long int t,i;
	cin>>t;
	for(i=1;i<=t;i++){
		long long int a[10]={0};
		long long int j,n,b,c;
		cin>>n;
		for(j=1;j<=200000;j++){
			b=n*j;
			while(b!=0){
				c=b%10;
				b=b/10;
				a[c]=1;
			}
			if(a[0]==1&&a[1]==1&&a[2]==1&&a[3]==1&&a[4]==1&&a[5]==1&&a[6]==1&&a[7]==1&&a[8]==1&&a[9]==1){
				break;
			}
		}
		if(a[0]==1&&a[1]==1&&a[2]==1&&a[3]==1&&a[4]==1&&a[5]==1&&a[6]==1&&a[7]==1&&a[8]==1&&a[9]==1)
		cout<<"Case #"<<i<<": "<<n*j<<endl;
		else
		cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
	}
}
