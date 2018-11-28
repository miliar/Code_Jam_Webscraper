#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

#define nMax 110

#define bug puts("Fuck");

int a[nMax][nMax];
int n,m;

bool check(int tx,int ty){
//	printf("tx=%d ty=%d %d\n",tx,ty,a[tx][ty]);
	bool ok = false;
	int x = tx;
	while(x >=0 && ((!a[x][ty]) || (a[x][ty] == a[tx][ty]))) x--;
	if(x==-1){
		x=tx;
		while(x<n && ((!a[x][ty]) || (a[x][ty] == a[tx][ty]))) x++;
		if(x==n){
			x=tx;
			while(x>=0) {a[x][ty] = 0;x--;}
			x=tx;
			while(x<n) { a[x][ty] = 0;x++;}
			ok = true;
		//	bug
		}
	}
	int y = ty;
	while(y>=0 && ((!a[tx][y]) || (a[tx][y] == a[tx][ty]))) y--;
	if(y==-1) {
		y=ty;
		while(y<m && ((!a[tx][y]) || (a[tx][y] == a[tx][ty]))) y++;
		if(y == m){
			y=ty;
			while(y>=0) {a[tx][y] = 0;y--;}
			y=ty;
			while(y<m) {a[tx][y] = 0;y++;}
			ok = true;
			//bug
		}
	} 
	return ok;
}

int main(){
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int cas = 1;
    while(t--){
		scanf("%d%d",&n,&m);
		bool ok = true;
		for(int i=0;i<n;i++) for(int j=0;j<m;j++) scanf("%d",&a[i][j]);
		while(1){
			int Ma = 110;
			int tx,ty;
			for(int i=0;i<n;i++) {
				for(int j=0;j<m;j++) {
					if(a[i][j] && a[i][j] < Ma){
						tx=i,ty=j,Ma = a[i][j];
					}
				}
			}
			if(Ma == 110) break;
			if(!check(tx,ty)) {
				ok = false;
				break;
			}
		//	for(int i=0;i<n;i++){
		//		for(int j=0;j<m;j++)printf("%d ",a[i][j]);
		//		printf("\n");
		//	}
		}
		printf("Case #%d: ",cas++);
		if(ok) printf("YES\n");
		else printf("NO\n");
    }
    return 0;
}
