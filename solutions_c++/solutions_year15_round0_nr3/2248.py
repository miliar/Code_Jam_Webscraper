#include <iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int T,tt,X,L;
char s[10005];
int a[10005];
int d[5][5]={0,0,0,0,0,
	0,1,2,3,4,
	0,2,-1,4,-3,
	0,3,-4,-1,2,
	0,4,3,-2,-1};
int hash(char c){
	if(c=='i')
		return 2;
	if(c=='j')
		return 3;
	if(c=='k')
		return 4;
	return 1;
}
bool solve(){
	if(L<3)
		return false;
	int ret=1;
	
	for(int i=0;i<L;i++){
		if(ret>0)
			ret=d[ret][a[i]];
		else ret=-d[-ret][a[i]];		
	}
	if(ret!=-1)
		return false;
	//bool flag=false;
	ret=1;
	int I=L,K=-1;
	for(int i=0;i<L;i++){
		if(ret>0)
			ret=d[ret][a[i]];
		else ret=-d[-ret][a[i]];
		if(ret==2){
			I=i;	
			break;
		}
	}
	ret=1;
	for(int i=L-1;i>0;i--){
		if(ret>0)
			ret=d[a[i]][ret];
		else ret=-d[a[i]][-ret];
		if(ret==4){
			K=i;	
			break;
		}
	}
	if(I+1<K)
		return true;
	return false;
	
}
int main(){	
	//freopen("t.txt","r",stdin);
	//freopen("w.out","w",stdout);
	scanf("%d",&T);
	tt=1;
	while(T--){
		scanf("%d%d",&L,&X);
		scanf("%s",s);		
		for(int i=0;i<X;i++){
			for(int j=0;j<L;j++){
				int x=hash(s[j]);
				a[i*L+j]=x;
			}
		}
		L*=X;
		if(solve())
			printf("Case #%d: YES\n",tt++);
		else
			printf("Case #%d: NO\n",tt++);
	}
}