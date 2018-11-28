# include <iostream>
# include <cstring>
using namespace std;
int main(){
	long long int j,n,tt,temp,sum,tsum;
	int t,i=0,k,num[10];
	cin>>t;
	while(i++<t){
		memset(num, 0, sizeof(num));
		cin>>n;
		j=1;
		temp=sum=0;
		if(n==0){
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
			continue;
		}
		while(sum!=10 ){
			temp=n*j;
		//cout<<"temp "<<temp<<endl;
		tt=temp;
		while(tt!=0){
			int r=tt%10;
			num[r]=1;
			tt/=10;}
		tsum=0;
		for(k=0;k<10;k++){
			tsum=tsum+num[k];
			}
		//cout<<endl<<"tsum "<<tsum;
		sum=tsum;
	//	cout<<"k";
		j=j+1;
	//	cout<<"j "<<j<<endl;
		
	}
	cout<<"Case #"<<i<<": "<<n*(j-1)<<endl;
	}
	return 0;
}
