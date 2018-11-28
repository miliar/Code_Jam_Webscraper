#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int bt[1<<11], buf[1<<11], sz;
int s[1<<11], e[1<<11];
char p[1001];
int n;

void maketree(int l, int r) {
	if(l+1==r) return;
	for(int i=l;i<r;i+=2) {
		s[i/2]=s[i];
		e[i/2]=e[i+1];
		bt[i/2]=(bt[i]+bt[i+1])%2;
	}
	maketree(l/2,r/2);
}

void upd(int cur, int l, int r) {
	if(s[cur]>r || e[cur]<l) return;
	if(s[cur]==l && e[cur]==r) {
		buf[cur]=(buf[cur]+1)%2;
		return;
	}
	bt[cur]+=(r-l+1); bt[cur]%=2;
	upd(cur*2,l,min(e[cur*2],r));
	upd(cur*2+1,max(s[cur*2+1],l),r);
}

int f(int cur, int l, int r) {
	if(s[cur]>r || e[cur]<l) return 0;
	if(buf[cur]) {
		bt[cur]+=buf[cur]*(e[cur]-s[cur]+1);
		bt[cur]%=2;
		if(cur*2<sz+n) {
			buf[cur*2]+=buf[cur];
			buf[cur*2]%=2;
		}
		if(cur*2+1<sz+n) {
			buf[cur*2+1]+=buf[cur];
			buf[cur*2+1]%=2;
		}
		buf[cur]=0;
	}
	if(s[cur]==l && e[cur]==r) return bt[cur];
	return (f(cur*2,l,min(e[cur*2],r))+f(cur*2+1,max(s[cur*2+1],l),r))%2;
}

int main() {
	FILE* in=fopen("A-Large.in","rt");
	FILE* out=fopen("Aout.txt","wt");
	int t, k;
	fscanf(in,"%d",&t);
	for(int tc=1;tc<=t;tc++) {
		fprintf(out,"Case #%d: ",tc);
		fscanf(in,"%s %d",p,&k);
		int res=0;
		sz=1;
		memset(bt,0,sizeof(bt));
		memset(buf,0,sizeof(buf));
		n=strlen(p); while(sz<n) sz*=2;
		for(int i=0;i<n;i++) {
			if(p[i]=='+') bt[sz+i]=0;
			else bt[sz+i]=1;
		}
		for(int i=sz;i<sz*2;i++)
			s[i]=e[i]=i;
		maketree(sz,sz*2);
		for(int i=0;i+k-1<n;i++) {
			if(f(1,sz+i,sz+i)) {
				res++; upd(1,sz+i,sz+i+k-1);
			}
		}
		bool ok=true;
		for(int i=n-k+1;i<n;i++) {
			if(f(1,sz+i,sz+i)) {
				ok=false; break;
			}
		}
		if(!ok) fprintf(out,"IMPOSSIBLE\n");
		else fprintf(out,"%d\n",res);
	}
	return 0;
}
