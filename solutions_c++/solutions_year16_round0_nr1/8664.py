#include <iostream>
#include <string>
using namespace std;


int arr[11]={0}; //0,1,2...9

bool ver(){
	for(int i=0; i<10;i++)
		if(arr[i]==0)	return false;
	return true;	
}

void clc(){
	for(int i=0; i<10;i++)
		arr[i]=0;
}

void desc(int x){
	while(x/10)	{
		arr[x%10]=1;
		x=x/10;
	}
	arr[x%10]=1;
}

int sol(int num){
	int res=0;
	while(!ver()){
		res+=num;
		desc(res);
	}
	return res;
}

int main() {
	int T; cin>>T;
	for(int i=1;i<=T;i++){
		clc();
		int num ;cin>>num;
		cout<<"Case #"<<i<<": ";
		if(num==0)	cout<<"INSOMNIA";
		else	cout<<sol(num);
		cout<<endl;
	}
	return 0;
}