#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#define inf (1<<30)
using namespace std;

int main(){
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D.out","w",stdout); 
	int T;
	cin>>T;
	for (int _=1;_<=T;_++){
		printf("Case #%d: ",_);
		int x,r,c,ret;
		cin>>x>>r>>c;
		if (r<c) swap(r,c);
		if (r==1 && c==1){
			if (x<2) puts("GABRIEL"); else puts("RICHARD");
		}
		if (r==2){
			if (x<3) puts("GABRIEL"); else puts("RICHARD");
		}
		if (r==3 && c==1){
			if (x<2) puts("GABRIEL"); else puts("RICHARD");
		}
		if (r==3 && c==2){
			if (x<4) puts("GABRIEL"); else puts("RICHARD");
		}
		if (r==3 && c==3){
			if (x==1 || x==3) puts("GABRIEL"); else puts("RICHARD");
		}
		if (r==4 && c<3){
			if (x<3) puts("GABRIEL"); else puts("RICHARD");
		}
		if (r==4 && c==3){
			if (x<5) puts("GABRIEL"); else puts("RICHARD");
		}
		if (r==4 && c==4){
			if (x==1 || x==2 || x==4) puts("GABRIEL"); else puts("RICHARD");
		}
	}
}
