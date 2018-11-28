#include<iostream>
#include<fstream>
using namespace std;

int sol(long long t,long long r){
	long long u=t,d=1,tmp;
	int size=0;
	while(u>0){
		size++;
		u=u>>1;
	}
	size=size/2-1;
	u=t;
	while(size--)u=u>>1;
	if(r>1000000000)u=(0x7fffffffffffffff)/r/4;
	while(u>d){
		tmp=(u+d+1)/2;
		if(t<2*tmp*tmp-tmp+2*tmp*r){
			u=tmp-1;
		}
		else d=tmp;
	}
	return d;
}


void main(){
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	long long r,t;
	cin>>T;
	for(int i=1;i<=T;i++){
	cin>>r>>t;
	cout<<"Case #"<<i<<": "<<sol(t,r)<<endl;
	}

	fclose(stdin);
	fclose(stdout);


}