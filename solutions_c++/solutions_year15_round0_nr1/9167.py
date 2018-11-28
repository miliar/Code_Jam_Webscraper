#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<string>
#include<string.h>
#include<fcntl.h>

using namespace std ;

int logic(){

	string s ;
	int smx ;
	cin>>smx>>s ;
	vector<int> v(smx+2,0) ;
	for(int i=0;i<=smx;i++){
		v[i] = s[i]-'0' ;
		if(i>0)
			v[i]+=v[i-1] ;
	}
	int tadd = 0 ;
	for(int i=1;i<=smx;i++){
		if(i>v[i-1]+tadd)
			tadd+=(i-(v[i-1]+tadd)) ;
	}
	return tadd ;

}


int main(){

	freopen("3.in","r",stdin) ;
	freopen("3.out","w",stdout) ;

	int test ;
	cin>>test ;
	for(int i=1 ; i<=test;i++){
		cout<<"Case #"<<i<<":"<<" "<<logic()<<endl ;
		
	}

}
