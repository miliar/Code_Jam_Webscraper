#include<iostream>

using namespace std;

int main(void){
	
	int T,N;
	long i,j;
	long m=0,num=10;
	//cout<<"Hello World"<<endl;
	cin>>T;
	
	for(i=1;i<=T;i++){
		cin>>N;
		int dig[10]={0,0,0,0,0,0,0,0,0,0};
		num=0;
		m=0;
		
		for(j=1;m==0;j++){
			num=j*N;
			//cout<<"Num :"<<num<<endl;
			while(num>0){
				dig[num%10]++;
				num/=10;
			}	
			m=dig[0]*dig[1]*dig[2]*dig[3]*dig[4]*dig[5]*dig[6]*dig[7]*dig[8]*dig[9];
			//cout<<"m="<<m<<endl;
			if(j>100){
				cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
				break;
			}
		}	
		if(j>100){
				continue;
		}
		cout<<"Case #"<<i<<": "<<N*(j-1)<<endl;
	}
	
	
	return 0;
}
