#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int n,i,j,m;
int tc,ii;
int a[2000];
struct abc{
	int x,y,z;
}b[2000];
int fk[20000];
bool abcd(abc c,abc d){
	if(c.x==d.x)return c.y<d.y;
	return c.x<d.x;
}
int main(){
//freopen("A-small-attempt1.in","r",stdin);
//freopen("A-small-attempt1.out","w",stdout);
scanf("%d",&tc);
for(ii=1;ii<=tc;ii++){
	scanf("%d %d",&n,&m);
	for(i=1;i<=m;i++)scanf("%d %d %d",&b[i].x,&b[i].y,&b[i].z);
//	sort(b+1,b+m+1,abcd);
	int ori=0;
	for(i=1;i<=m;i++){
		int k=b[i].y-b[i].x;
		ori+=(2*n-k+1)*k*b[i].z/2;
	}
	for(i=1;i<=19999;i++)fk[i]=0;
	for(i=1;i<=m;i++){
		for(j=b[i].x;j<b[i].y;j++){
			fk[j]+=b[i].z;
		}
	}
	
	int New=0;
	for(i=1;i<=10001;i++){
		int tp=0;
		for(j=1;j<=n-1;j++){
		    if(fk[j]>=i)tp++,New+=n-tp+1;
		    else tp=0;
		}
	}
	//printf("%d %d\n",ori,New);
	printf("Case #%d: %d\n",ii,max(0,ori-New) );
	
		    
		    
		    
		    
	
}
	
	return 0;
}
