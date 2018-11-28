#include <cstdio>

int a[100][100],C[100],R[100];
int min(int a,int b){
	return (a<b)?a:b;
}
bool ok(int n,int m){
	for (int i=0;i<n;i++)
		for (int j=0;j<m;j++)
			if (R[i]>a[i][j]&&C[j]>a[i][j])
				return false;
	return true;
}
int main()
{
	int cases,n,m;
	scanf("%d",&cases);
	for (int t=1;t<=cases;t++){
		printf("Case #%d: ",t);
		scanf("%d %d",&n,&m);
		for (int i=0;i<n;i++)
			R[i]=0;
		for (int j=0;j<m;j++)
			C[j]=0;
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++){
				scanf("%d",&a[i][j]);
				if (a[i][j]>R[i])
					R[i]=a[i][j];
				if (a[i][j]>C[j])
					C[j]=a[i][j];
			}
		puts((ok(n,m))?"YES":"NO");
	}
}
