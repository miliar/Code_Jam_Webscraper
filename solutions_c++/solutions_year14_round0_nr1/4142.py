#include <iostream>
#include <cmath>
#include <map>
#include <stdio.h>
#include <cstring>
#define FOR(i,j) for(int i=0;i<j;i++)
#define pb push_back
using namespace std;
int main(){
	int T,x,y,z=0;
	int a,b,c,d;
	cin>>T;
	while(z<T){
	z++;
	cin>>x;
	int ct=0;
	int cy;
	bool store[17];
	memset(&store,0,sizeof(bool)*17);
	FOR(i,4){
		cin>>a>>b>>c>>d;
		if (i==x-1){
			store[a]=store[b]=store[c]=store[d]=1;
		}
	}
	cin>>y;
	FOR(i,4){
		cin>>a>>b>>c>>d;
		if (i==y-1){
			if (store[a]) {ct++;cy=a;}
			if (store[b]) {ct++;cy=b;}
			if (store[c]) {ct++;cy=c;}
			if (store[d]) {ct++;cy=d;}
		}
	}
	
	if (ct==1) cout<<"Case #"<<z<<": "<<cy<<endl;
	else if (ct==0) cout<<"Case #"<<z<<": Volunteer cheated!"<<endl;
	else cout<<"Case #"<<z<<": Bad magician!"<<endl;
	
	}

}