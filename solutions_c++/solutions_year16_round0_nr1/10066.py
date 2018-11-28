#include<bits/stdc++.h>
using namespace std;
vector<long long>estado(10);
long long operacion(long long a){
	while(a!=0){estado[a%10]=1;a=a/10;}
}
int main(){
	long long y;
	cin>>y;
	vector<long long>rsp;
	for(long long j=0;j<y;j++){
	long long a;
	cin>>a;
	long long tmp=0;
	long long b=0;
	long long h=0;
	while(b!=10){
		tmp++;
		if(tmp>1000){h=-1;break;}
		b=0;
		h=h+a;
		operacion(h);
		for(long long i=0;i<estado.size();i++){
			if(estado[i]==1){b++;}
		}
	}
	for(long long i=0;i<estado.size();i++){
			estado[i]=0;
		}
	rsp.push_back(h);
}
for(long long i=0;i<rsp.size();i++){
	if(rsp[i]==-1){cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;}else{
	cout<<"Case #"<<i+1<<": "<<rsp[i]<<endl;
}
}
}