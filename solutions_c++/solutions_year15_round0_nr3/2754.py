#include <iostream>
#include <cstdio>
using namespace std;

const int table[5][5]={
	{0,0,0,0,0},
	{0,1,2,3,4},
	{0,2,-1,4,-3},
	{0,3,-4,-1,2},
	{0,4,3,-2,-1}};

int main(){
	int T; scanf("%d",&T);
	char s[10010];
	for(int Case=1; Case<=T; ++Case){
		int L,X; scanf("%d%d",&L,&X);
		getchar(); scanf("%s",s);
		if(L*X<3){
			printf("Case #%d: NO\n",Case);
			continue;
		}
		int now=1, shouldbe=2;
		for(int i=0; i<X; ++i){
			for(int j=0; j<L; ++j){
				bool minus=now<0;
				if(minus) now*=-1;
				switch(s[j]){
					case '1': now=table[now][1]; break;
					case 'i': now=table[now][2]; break;
					case 'j': now=table[now][3]; break;
					case 'k': now=table[now][4]; break;
				}
				if(minus) now*=-1;
				if(now==shouldbe && shouldbe==2) shouldbe=4;
				else if(now==shouldbe && shouldbe==4) shouldbe=-1;
			}
		}
		if(now!=-1 || shouldbe!=-1)
			printf("Case #%d: NO\n",Case);
		else
			printf("Case #%d: YES\n",Case);
	}
	return 0;
}
