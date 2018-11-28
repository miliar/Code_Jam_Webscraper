#include "bits/stdc++.h"
using namespace std;
int v[10];
void verifi(int cn){
	int dig;
	while(cn){
		dig=cn%10;
		v[dig]=1;
		cn=cn/10;
	}
}
bool ver(){
	bool sw=true;
	for (int i = 0; i < 10; ++i)
	{
		if(!v[i])sw=false;
	}
	return sw;
}
int main(){
	int n;
	cin>>n;
	for (int i = 1; i <=n; ++i)
	{
		int k=1;
		int cn=0,t;
		cin>>t;
		v[0]=v[1]=v[2]=v[3]=v[4]=v[5]=v[6]=v[7]=v[8]=v[9]=0;
		while(!ver() and t){
			cn=t;
			cn=cn*k;
			verifi(cn);
			k++;
		}
		cout<<"Case #"<<i<<": ";
		if(t)cout<<cn<<endl;
		else cout<<"INSOMNIA"<<endl;
	}
	return 0;
}