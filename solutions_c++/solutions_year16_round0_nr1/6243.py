#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int ti;
int check(int num){
	long long ans[10],t,j;
	memset(ans,0,sizeof(ans));
	bool overall = false;
//	bool failed;
	for(int i=0;i<100;++i){
		bool failed = false;
		t = num *i;
		while(t>0){
			ans[t%10]= 1;
			t = t/10;
		}
		bool found = false;
		for(j=0;j<10;++j){
			if(ans[j]==0){
				failed = true;
				break;
			}
		}
		if(failed==false){
			overall = true;
			t = num*i;
			break;
		}
	}
	if(overall==false){
		printf("Case #%d: INSOMNIA\n",ti);
	}
	else{
		printf("Case #%d: %lld\n",ti,t);
	}
}
int main(){
	int tst,j;
	cin >> tst;
	for(ti=1;ti<=tst;++ti){
		cin >> j;
		if(j==0){
			printf("Case #%d: INSOMNIA\n",ti);
		}
		else{
			check(j);
		}
	}
}

