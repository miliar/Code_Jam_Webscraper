//hi
#include<bits/stdc++.h>
using namespace std;
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define LL long long int
int ans[10000];
int tmp[10000];
int n,p,r,s,N;
int sol(){
	int i,j,t,cp,cr,cs;
	for(t=1;t<4;t++){
		ans[0]=t;
		for(i=0;i<n;i++){
			int x=1<<i;
			for(j=0;j<x;j++){
				if(ans[j]==1) tmp[2*j]=1, tmp[2*j+1]=2;
				if(ans[j]==2) tmp[2*j]=2, tmp[2*j+1]=3;
				if(ans[j]==3) tmp[2*j]=3, tmp[2*j+1]=1;
			}
			for(j=0;j<2*x;j++)
				ans[j]=tmp[j];
		}
		cp=0, cr=0, cs=0;
		for(i=0;i<N;i++){
			if(ans[i]==1) cp++;
			if(ans[i]==2) cr++;
			if(ans[i]==3) cs++;
		}
		if(cp==p&&cr==r&&cs==s) return 1;
	}
	return 0;
}
string go(string a){
	int len=a.length();
	if(len==1) return a;
	string b=a.substr(0,len/2),c=a.substr(len/2,len/2);
	b=go(b);
	c=go(c);
	if(b>c) return c+b;
	return b+c;
}
int main(void){
    int t,hh;
    scanf("%d",&t);
    for(hh=1;hh<=t;hh++){
		scanf("%d%d%d%d",&n,&r,&p,&s);  //prs 012
		N=1<<n;
		int i,j,k;
		if(sol()){
			string aa(N,' ');
			for(i=0;i<N;i++){
				if(ans[i]==1) aa[i]='P';
				if(ans[i]==2) aa[i]='R';
				if(ans[i]==3) aa[i]='S';
			}
			aa=go(aa);
			printf("Case #%d: ",hh);
			for(i=0;i<N;i++)
				printf("%c",aa[i]);
			printf("\n");
		}else{
			printf("Case #%d: IMPOSSIBLE\n",hh);
		}
	}
    return 0;
}
