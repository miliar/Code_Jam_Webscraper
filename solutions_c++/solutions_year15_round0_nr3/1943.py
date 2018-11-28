#include <stdio.h>
#include <cstring>
#include <string>
#include <stdlib.h>
int L,X;
char s[10005];
int a[4][4]={
	{0,1,2,3},
	{1,0,3,2},
	{2,3,0,1},
	{3,2,1,0}
};
int sign[4][4]={
	{1,1,1,1},
	{1,-1,1,-1},
	{1,-1,-1,1},
	{1,1,-1,-1}
};
int head[100003],sh[100003];
int tail[100003],st[100003];
int get(int l,int r){
	if(l>r) return 0;
	int i,j;
	int x;
	int si,res;
	for(i=l;i<=r;i++){
		x=s[i]-'i'+1;
		if(i==l) res=x,si=1;
		else{
			si*=sign[res][x];
			res=a[res][x];
		}
	}
	return si*res;
}
int init(){
	int i,j;
	j=L;
	for(i=L;i<X*L;i++){
		s[j]=s[j%L];
		j++;
	}
	s[j]='\0';
	// printf("%d",strlen(s));  
	int x;
	for(i=0;s[i];i++){
		x=s[i]-'i'+1;
		if(i==0) head[i]=x,sh[i]=1;
		else{
			head[i]=a[head[i-1]][x];
			sh[i]=sh[i-1]*sign[head[i-1]][x];
		}
	}	
	for(i=X*L-1;i>=0;i--){
		x=s[i]-'i'+1;
		// printf("%d ",x);
		// fflush(stdout);
		if(i==strlen(s)-1) tail[i]=x,st[i]=1;
		else{
			tail[i]=a[x][tail[i+1]];
			st[i]=st[i+1]*sign[x][tail[i+1]];
		}
	}
	for(i=0;s[i];i++){
		// printf("%d ",tail[i]);
		if(head[i]*sh[i]!=1) continue;
		for(j=strlen(s)-1;j>i;j--){
			if(tail[j]*st[j]!=3) continue;
			// printf("   %d %d   ",i,j);
			if(get(i+1,j-1)!=2) continue;
			return 1;
		}
	}
	return 0;
}
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T,C;
	scanf("%d",&T);
	for(C=1;C<=T;C++){
		printf("Case #%d: ",C);
		scanf("%d %d\n%s",&L,&X,s);
		printf("%s\n",init()?"YES":"NO");
		fflush(stdout);
	}
}