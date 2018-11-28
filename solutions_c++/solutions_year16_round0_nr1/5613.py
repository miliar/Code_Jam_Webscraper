#include <iostream>
#include <map>
using namespace std;


int main() {
	// your code goes here
	long T,t;
	cin>>T;
	t=T;
	while(T>0){
	map<long,long> str;
	long n,i,count=0,flag=0;
	cin>>n;
	if(n==0){
		cout<<"Case #"<<t-T+1<<": "<<"INSOMNIA"<<"\n";
	}else{
		for(long j=0;j<10;j++)
			str[j]=-1;
		for(i=1;flag!=1;i++){
			int x= i*n;
			while(x>0){
				if(str[x%10]<0){
					str[x%10]=1;
					count++;
				}
				x=x/10;
			}
			if(count == 10){
				if(T==1)
				cout<<"Case #"<<t-T+1<<": "<<i*n;
				else
				cout<<"Case #"<<t-T+1<<": "<<i*n<<"\n";
				flag=1;
			}
		}
	}
	T--;
	}
	return 0;
}
