#include<bits/stdc++.h>
using namespace std;
int n,m,T;
int nr,ns,np;
char a[123456],ans[123456];
bool ok;
char s[3]={'P','S','R'};
char pd(char a,char b){
	if(a>b)swap(a,b);
	if(a=='P' && b=='R') return 'P';
	if(a=='R' && b=='S') return 'R';
	if(a=='P' && b=='S') return 'S';
}
void build(int dep,int l,char c){
	if(dep==n) {
		a[l]=c;
		return;
	}
	for(int i=0;i<3;i++)
		for(int j=i+1;j<3;j++){
			char L=s[i],R=s[j];
			 if(pd(L,R)==c){
			   build(dep+1,l*2-1,L);
			   build(dep+1,l*2,R);
			   return;
			}
		}
}
void check(int l,int r){
	int mid=(r-l+1)/2;
	int h1=l,h2=l+mid;
	int ok=false;
	for(int i=1;i<=mid;i++){
		int t1=h1+i-1,t2=h2+i-1;
		if(a[t1]>a[t2]){
			ok=true;
		}
		else if(a[t1]<a[t2]) break;
	}
	if(ok){
		for(int i=1;i<=mid;i++){
			int t1=h1+i-1,t2=h2+i-1;
			swap(a[t1],a[t2]);
		}
	}
}
void renew(){
	//for(int i=1;i<=(1<<n);i++)cerr<<a[i];cerr<<endl;
	
	int r=0,s=0,p=0;
	for(int i=1;i<=(1<<n);i++){
		if(a[i]=='R')r++;
		if(a[i]=='S')s++;
		if(a[i]=='P')p++;
	}
	if(r!=nr || s!=ns || p!=np) return;
	for(int i=1;i<=n;i++){
		int len=1<<i;
		for(int j=1;j<=(1<<n);j+=len) check(j,j+len-1);
	}
			
	bool pd=false;
	for(int i=1;i<=(1<<n);i++)	if(a[i]<ans[i]){
		pd=true;
		break;
	}else if(a[i]>ans[i]) break;
	if(!pd) return;
	if(pd)ok=true;
	for(int i=1;i<=(1<<n);i++) ans[i]=a[i];
}
int main(){
	freopen("t.in","r",stdin);
	freopen("t-1.out","w",stdout);
	scanf("%d",&T);
	for(int ti=1;ti<=T;ti++){
		printf("Case #%d: ",ti);
		scanf("%d%d%d%d",&n,&nr,&np,&ns);
		for(int i=1;i<=(1<<n);i++)ans[i]='Z';
		ok=false;
		build(0,1,'P');
		renew();
		build(0,1,'S');
		renew();
		build(0,1,'R');
		renew();
		if(ok) {
			for(int i=1;i<=(1<<n);i++)printf("%c",ans[i]);
		}else printf("IMPOSSIBLE");
		printf("\n");
	}
		
}
