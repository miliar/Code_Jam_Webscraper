#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<string>
#include<algorithm>
#include<time.h>

using namespace std;

typedef long long llo;
typedef double llb;

#define con continue
#define vec vector
#define str string
#define pt puts("");
#define pb push_back
#define for0(a,b) for(a=0;a<b;++a)
#define for1(a,b) for(a=1;a<=b;++a)
#define ford(a,b) for(a=b;a;--a)


long i,j,k,l,n,m;
long tt,test,all;
long la[1000],he[100][10];
char c[100];
int main(){
	//freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);
	scanf("%ld",&tt);
	la['X']=1;
	la['T']=0;
	la['O']=2;
	for1(test,tt){
		printf("Case #%ld: ",test);
		all=0;
		memset(he,0,sizeof(he));
		for1(i,4){
			scanf("%s",c+1);
			for1(j,4)if(c[j]!='.'){
				++he[i][la[c[j]]];
				++he[4+j][la[c[j]]];
				if(i==j)++he[9][la[c[j]]];
				if(i+j==5)++he[10][la[c[j]]];
				++all;
			}
		}
		for1(i,10){
			if(he[i][0]+he[i][1]==4){
				puts("X won");
				break;
			}
			if(he[i][0]+he[i][2]==4){
				puts("O won");
				break;
			}
		}
		if(i>10){
			if(all<16)puts("Game has not completed");
			else puts("Draw");
		}
	}

	return 0;
}
