#include<iostream>
#include<string.h>
#include<stdio.h>
#include<cmath>
using namespace std;
int T,TT,a,b;
int huiwen(int m){
	int a[100];
	int temp=m,t=-1;
	while(temp){
		t++;
		a[t]=temp%10;
		temp=temp/10;
	}
	for(int i=0;i<t/2+1;i++){
		if(a[i]!=a[t-i]) return 0;
	}
	return 1;
}


int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>T;
	TT=0;
	while(T--){
		cin>>a>>b;
		int a1=sqrt(a);
		int a2=sqrt(b);
		int ans=0;
		for(int i=a1;i<=a2;i++){
			if(!huiwen(i)) continue;
			if(i*i<a) continue;
			if(i*i>b) continue;
			if(!huiwen(i*i)) continue;
			ans++;
		}
		cout<<"Case #"<<++TT<<": "<<ans<<endl;
	}
	return 0;
}
