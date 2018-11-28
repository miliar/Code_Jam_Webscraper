#include <iostream>

using namespace std;

int main(){
	int a[10]={0};
	int T;
	unsigned long long x,x_,x__;
	int sum=0;
	int it;
	cin>>T;
	for(int i=0;i<T;i++){
		cin>>x;
		it=0;
		x__=-1;
		for(int m=0;m<10;m++)
			a[m]=0;
		while(1){
			sum=0;
			x_=(it+1)*x;
			if(x__==x_)
			{
				cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
				break;
			}
			x__=x_;
			while(x_!=0){
				a[x_%10]=1;
				x_=x_/10;
			}
			for(int j=0;j<10;j++){
				sum+=a[j];
			}
			if(sum==10){
				cout<<"Case #"<<i+1<<": "<<x__<<endl;
				break;
			}
			it++;
		}
	}
	return 0;
}