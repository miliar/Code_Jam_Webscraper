#include <bits/stdc++.h>
using namespace std;
#define ll long long

int t[10];

void clear(){
	for(int i=0;i<10;i++)
		t[i]=0;
}

void add_hash(int num){
	for(;num!=0;num=num/10){
		t[num%10]++;
	}
}

int check(){
	for(int i=0;i<10;i++){
		if(t[i]==0)
			return 0;
	}
	return 1;
}

int main() {
	ll int t,cnt=0;
	cin>>t;
	while(cnt<t){
		ll int n;
		clear();
		cin>>n;
		if(n==0){
			cout<<"Case #"<<cnt+1<<": INSOMNIA"<<endl;
		}
		else{
			for(ll int k=1;;k++){
				ll int num=n*k;
				add_hash(num);
				bool i=check();
				if(i){
					cout<<"Case #"<<cnt+1<<": "<<num<<endl;
					break;
				}
			}
		}
		cnt++;
	}
	return 0;
}