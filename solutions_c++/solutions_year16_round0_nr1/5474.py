#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("outfile1.txt","w",stdout);
	int t,k=1;
	cin>>t;
	while(k<=t){
		long long int n;
		int flag=0,i=1,a[10]={0};
		long long int num,number;
		cin>>n;
		number=n;
		if(n==0)
			cout<<"Case #"<<k<<": "<<"INSOMNIA"<<endl;
		else{
			while(flag==0){
				num=n*i;
				number=n*i;
				while(num!=0){
					a[num%10]=1;
					num=num/10;
				}
				flag=1;
				for(int j=0;j<10;j++){
					/*if(a[j]==0){
						flag=0;
						cout<<"\na["<<j<<"]="<<a[j]<<endl;
						break;
					}*/
				//	cout<<"\na["<<j<<"]="<<a[j]<<endl;
					if(a[j]==0)
						flag=0;
				}
				i++;
				//cout<<"\n end first while \n";
			}
			cout<<"Case #"<<k<<": "<<number<<endl;
		}
		k++;
	}
	return 0;
}
