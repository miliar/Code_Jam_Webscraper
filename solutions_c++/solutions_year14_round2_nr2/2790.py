#include<iostream>
#include<stdio.h>

using namespace std;

int main(){
int T;
cin>>T;
for(int i=1; i<=T; i++){
	int A, B, K;
	cin>>A>>B>>K;
	int count=0;
	for(int a=0; a<A; a++){
	for(int b=0; b<B; b++){
	int bitab=a & b;
	if(bitab<K) count++;
	}
	}
	cout<<"Case #"<<i<<": "<<count<<endl;
}
}


