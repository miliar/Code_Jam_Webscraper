#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;

int rd[10];

bool check(){
	for(int i=0;i<10;i++){
		if(rd[i]==0)return false;
	}
	return true;
}

void sett(int n){
	int tmp=n;
	do{
		rd[tmp%10]=1;
		tmp=tmp/10;
	}while(tmp!=0);
}
	
int main(){
	int T,N,r,mul;
	cin>>T;
	int rud=0;
	while( (rud++)<T){
		memset(rd,0,sizeof(rd));
		cin>>N;
		if(N==0){
			cout<<"Case #"<<rud<<": INSOMNIA"<<endl;
			continue;
		}
		r=1;
		while(!check()){
			mul=(r++)*N;
			sett(mul);
		}
		cout<<"Case #"<<rud<<": "<<mul<<endl;
	}
	return 0;
}


