#include <iostream>
#include <cstdio>
#define	MAXN	101

using namespace std;
int a[MAXN][MAXN];

int main(){
	int t,k=0,n,m;
	cin>>t;
	while(t--){
		scanf("%d %d\n",&n,&m);		
		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j)	cin>>a[i][j];
		printf("Case #%d: ",++k);
		if(n==1 or m==1){
			printf("YES\n");
			continue;
		}
		bool can=1, dir1=1,dir2=1;
		for(int i=0;i<n;++i){
			for(int j=0;j<m;++j){
				dir1=1; dir2=1;			
				if(i!=n-1)
					for(int p=i+1;p<n;++p)	if(a[p][j]>a[i][j]){	dir1=0;break;}
				if(i!=0)
					for(int q=i-1;q>=0;--q)	if(a[q][j]>a[i][j]){	dir1=0;break;}

				if(j!=m-1)
					for(int p=j+1;p<m;++p)	if(a[i][p]>a[i][j]){	dir2=0;break;}
				if(j!=0)
					for(int q=j-1;q>=0;--q)	if(a[i][q]>a[i][j]){	dir2=0;break;}
				if(!dir1 and !dir2){
					can=0;
					break;	break;
				}				
			}
		}
		if(can)		printf("YES\n");
		else		printf("NO\n");
	}
	return 0;
}
