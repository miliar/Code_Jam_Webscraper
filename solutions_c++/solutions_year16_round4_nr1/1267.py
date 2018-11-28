#include <bits/stdc++.h>
#define M (2<<12)
using namespace std;
int a[M],n,b[3],x,y,z;
char k[3];

void input(void){
	scanf("%d %d %d %d",&n,&y,&x,&z);
}

void process(void){
	int i,j,l,p[3],m;
	k[0]='P';k[1]='R';k[2]='S';
	for(l=0;l<3;l++){
		p[0]=p[1]=p[2]=0;
		a[0]=l;
		for(i=n;i>=1;i--){
			for(j=0;j<(1<<n);j+=(1<<i)){
				a[j+(1<<(i-1))]=(a[j]+1)%3;
			}
		}
		for(i=0;i<(1<<n);i++){
			p[a[i]]++;
		}
		if(p[0]==x && p[1]==y && p[2]==z){
			for(i=0;i<n;i++){
				for(j=0;j<(1<<n);j+=(1<<(i+1))){
					bool pp=false;
					int ll,rr;
					for(ll=j,rr=j+(1<<i);rr<j+(1<<(i+1));ll++,rr++){
						if(a[ll]<a[rr]){
							pp=false;
							break;
						}else if(a[ll]>a[rr]){
							pp=true;
							break;
						}
					}
					if(pp){
						for(ll=j,rr=j+(1<<i);rr<j+(1<<(i+1));ll++,rr++){
							swap(a[ll],a[rr]);
						}
					}
				}
			}
			for(i=0;i<(1<<n);i++){
				printf("%c",k[a[i]]);
			}
			return;
		}
	}
	printf("IMPOSSIBLE");
}

int main(void){
	freopen("input.txt","r",stdin);

	int t,i;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		input();
		printf("Case #%d: ",i);
		process();
		printf("\n");
	}

	return 0;
}
