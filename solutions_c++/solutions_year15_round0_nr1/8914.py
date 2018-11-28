#include<iostream>
#include<cstdio>
#define FOR(a,b) for(a=0;a<b;a++)
using namespace std;
const int MAX=1001;
int S;
int sl[MAX];	//shyness level;

int bin(int l,int h){
	if(h==0) return 0;
	if(l==h) return l;
	int mid = (l+h)/2,i;
	int avail=mid;
	FOR(i,S+1){
		if(sl[i]!=0){
			if(i<=avail) avail +=sl[i];
			else return bin(mid+1,h);
		}
	}
	return (mid>l)? bin(l,mid): mid;
}

int main(){
	int T,i,j,ans;
	scanf("%d",&T);
	FOR(i,T){
		scanf("%d",&S);
		FOR(j,S+1){
			char inp;
			do{
				scanf("%c",&inp);
			}
			while(inp==' '||inp=='\n');
			sl[j]= int(inp-'0');
		}
		ans=bin(0,S);
		/*
		ans=0;
		int l=0,h=S,mid,avail;
		bool down;
		while(l<=h){
			if(l==h || h==0) {ans=h; break;}
			mid = (l+h)/2;
			avail=mid;
			down=true;
			FOR(j,S+1){
				if(sl[j]!=0){
					if(j<=avail) avail +=sl[j];
					else{
						l=mid+1;
						down=false;
						break;
					}
				}
			}
			if(down){
				if(mid>l) h=mid;
				else {
					ans=mid;
					break;
				}
			}
		}
		*/
		printf("Case #%d: %d\n",i+1,ans);
		
	}
	
}