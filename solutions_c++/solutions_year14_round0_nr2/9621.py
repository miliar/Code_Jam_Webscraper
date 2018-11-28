#include <iostream.h>
#include <stdio.h>
#define FOR(i,j) for(int i=0;i<j;i++)
using namespace std;
int main(){
	int T,x,y,z=0;
	int a,b,c,d;
	scanf(%d,&T);
	while(z<T){
	z++;
	scanf(%d,&x);
	int ct=0;
	int cy;
	bool store[16];
	memset(&store,0,sizeof(bool)*16);
	FOR(i,4){
		scanf(%d %d %d %d,&a,&b,&c,&d);
		if (i==x-1){
			store[a]=store[b]=store[c]=store[d]=1;
		}
	}
	scanf(%d,&y);
	FOR(i,4){
		scanf(%d %d %d %d,&a,&b,&c,&d);
		if (i==y-1){
			if (store[a]) {ct++;cy=a;}
			if (store[b]) {ct++;cy=b;}
			if (store[c]) {ct++;cy=c;}
			if (store[d]) {ct++;cy=d;}
		}
	}
	
	if (ct==1) printf("Case # %d: %d",&z,&cy);
	else if (ct==0) printf("Case # %d: Volunteer cheated!\n",&z);
	else printf("Case # %d: Bad Magician!\n",&z);
	
	}

}