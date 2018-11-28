#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <assert.h>
#include <iostream>

using namespace std;
typedef long long int ll;
void baseb(string str){
	for(int b=2; b<=10; b++){
		ll num=0;
		for(int i=0; i<str.length(); i++){
			num=num*b+str[i]-'0';
		}
		printf(" %lld",num);
	}
}

void jamCoin(int N, int J){
	assert(N>=2);
	vector<string> vstr;
	string tmp="";
	for(int i=0; i<N; i++) tmp=tmp+'0';
	tmp[0]='1';
	tmp[N-1]='1';
	vstr.push_back(tmp);
	int pos=1;
	while(vstr.size()<=J && pos<N-1){
		int p=vstr.size();
		for(int i=0; i<p; i++){
			tmp=vstr[i];
			tmp[pos]='1';
			vstr.push_back(tmp);
		}
		pos++;
	}
	for(int i=0; i<J && i<vstr.size(); i++){
		cout<<(vstr[i]+vstr[i]);
		baseb(vstr[i]);
		cout<<endl;
	}
}

int main(){
	int t;
	scanf("%d",&t);
	for(int i=1; i<=t; i++){
		printf("Case #%d:\n",i);
		int J, N;
		scanf("%d%d",&N,&J);
		if(!(N&1)) jamCoin(N/2,J);
	}
}
