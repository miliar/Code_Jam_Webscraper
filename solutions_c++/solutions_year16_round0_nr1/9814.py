#include<iostream>
#include<cstring>
using namespace std;
int main(){
	int test,a,n,temp=0,cnt=0,incr=2,N=0;
	string num;
	int sleep[10]={0};
	cin>>test;
	for(int i=1;i<=test;i++){
		cin>>a;
		n=a;
	while(1){
	while(n>0) {
		temp= n % 10;
		if(sleep[temp]==0){
		cnt++;
		sleep[temp]=1;
		}
		n /= 10;
	}
	if(cnt==10){
			cout<<"Case #"<<i<<": "<<N<<endl;
			memset(sleep, 0, sizeof(int)*10);
			cnt=0;
			N=0;
			temp=0;
			incr=0;
			break;
		}
	//sleep[n]=n;
	n=a*incr;
	N=n;
	incr++;
	if(incr>100000){
		cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		memset(sleep, 0, sizeof(int)*10);
			cnt=0;
			N=0;
			temp=0;
			incr=0;
		break;
	}

	//cout<<cnt<<" "<<a<<" "<<endl;
	}
	}
}
