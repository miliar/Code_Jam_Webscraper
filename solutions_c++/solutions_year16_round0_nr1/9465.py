#include<iostream>

using namespace std;

int ans[10];

bool check(int c){
	while(c!=0){
		int tmp=c%10;
		ans[tmp]++;
		c/=10;
	}
	for(int i=0;i<10;i++){
		if(ans[i]==0)return true;
	}
	return false;
}

int main(){
	int n;
	cin>>n;
	for(int l=1;l<=n;l++){
		for(int i=0;i<10;i++)ans[i]=0;
		int a;
		cin>>a;
		int c=a;
		if(a==0){
			cout<<"Case #"<<l<<": INSOMNIA"<<endl;
			continue;
		}
		while(check(c)){
			c+=a;
		}
		cout<<"Case #"<<l<<": "<<c<<endl;
		
	}
}
