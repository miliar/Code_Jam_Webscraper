#include<iostream>
#include<cmath>

using namespace std;

int sum[100000001];
int data[20];

bool palindrome(long long num){

	int n;
	for(n=0;num>0;num/=10){
		data[n]=num%10;
		n++;
	}
	for(int i=0;i<n/2;i++){
		if(data[i]!=data[n-1-i]){
			return false;
		}
	}
	return true;
}

void init(){
	
	for(long long i=1;i<=10000000;i++){
		if(palindrome(i)&&palindrome(i*i)){
			sum[i]=sum[i-1]+1;
		}else{
			sum[i]=sum[i-1];
		}
	}
	
}

int main(){
	
	init();
	int T;
	cin>>T;
	for(int testcase=1;testcase<=T;testcase++){
		long long A,B;
		cin>>A>>B;
		long long sa=(long long)sqrt((double)A);
		long long sb=(long long)sqrt((double)B);
		if(sa*sa==A){
			cout<<"Case #"<<testcase<<": "<<sum[sb]-sum[sa-1]<<endl;
		}else{
			cout<<"Case #"<<testcase<<": "<<sum[sb]-sum[sa]<<endl;
		}
	}
	return 0;
}
