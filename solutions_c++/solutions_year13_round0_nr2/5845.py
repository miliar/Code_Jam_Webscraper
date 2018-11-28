#include<conio.h>
#include<stdio.h>
using namespace std;

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int i,j,k,m,n,t,ca,cb,maxh,maxi,flag,p;
	int a[110][110];
	scanf("%d",&p);
	for(int z=1;z<=p;z++){
		flag=0;
		printf("Case #%d: ",z);
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				scanf("%d",&a[i][j]);	
			}
		}
		int fx,fy;
		for(i=0;i<n;i++){		//ппеп╤о 
			maxh=a[i][0];
			maxi=0;
			fx=0;
			for(j=1;j<m;j++){
				if(a[i][j]!=a[i][j-1])fx=1;
				if(maxh<a[i][j]){
					maxh=a[i][j];
					maxi=j;
				}
			}
			if(fx==1){
				for(k=0;k<m;k++){
					if(flag==1)break;
					if(a[i][k]==maxh)continue;
					for(t=0;t<n;t++){
						if(a[t][k]>a[i][k]){
							flag=1;
							printf("NO\n");
							break;
						}
					}
				}
			}
			if(flag==1)break; 
		}
		if(flag==1)continue;
		for(j=0;j<m;j++){		//апеп╤о 
			maxh=a[0][j];
			maxi=0;
			fy=0;
			for(i=1;i<n;i++){
				if(a[i][j]!=a[i-1][j])fy=1;
				if(maxi<a[i][j]){
					maxh=a[i][j];
					maxi=i;
				}
			}
			if(fy==1){
				for(k=0;k<n;k++){
					if(flag==1)break;
					if(a[k][j]==maxh)continue;
					for(t=0;t<m;t++){
						if(a[k][t]>a[k][j]){
							flag=1;
							printf("NO\n");
							break;
						}
					}
				}
			}
			if(flag==1)break; 
		}
		if(flag==1)continue;
		else printf("YES\n");
	}
    getch();
    return 1;
}
