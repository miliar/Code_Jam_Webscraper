#include<iostream>
using namespace std;
int main(){
	int j;
	long check[10];
	long req = 0;
	for(j=0; j<10;j++){
		check[j] = 1<<j;
		req = req | check[j];
	}
	int T;
	cin>>T;
	int i;
	for(i=0;i<T;i++){
		int N;
		cin>>N;
		if(N==0){
			cout<<"Case #"<<(i+1)<<": INSOMNIA"<<endl;
		}
		else{
			long tracker = 0;
			long name = N;
			long limit = N*100;
			while(name <= limit){
				long temp=name;
				while(temp){
					tracker = tracker | check[temp%10];
					temp/=10;
				}
				if(tracker == req){
					cout<<"Case #"<<(i+1)<<": "<<name<<endl;
					break;
				}
				name += N;
			}
			if(name > limit){
				cout<<"Case #"<<(i+1)<<": INSOMNIA"<<endl;
			}
		}
	}
	return 0;
}
