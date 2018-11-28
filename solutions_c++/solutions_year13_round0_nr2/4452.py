#include <cstdio>
int a[111][111];
int row_h[111];
int col_h[111];
int main(void){
    
    int t;
    scanf("%d",&t);
    for(int z=1; z<=t; z++){
	int n,m;
	scanf("%d %d",&n,&m);
	for(int i=0; i<n; i++)
	    for(int j=0; j<m; j++) scanf("%d",&a[i][j]);

	for(int i=0; i<n; i++){
	    row_h[i]=a[i][0];
	    for(int j=1; j<m; j++)
		if(row_h[i]<a[i][j]) row_h[i]=a[i][j];
	}

	for(int j=0; j<m; j++){
	    col_h[j]=a[0][j];
	    for(int i=1; i<n; i++)
		if(col_h[j]<a[i][j]) col_h[j]=a[i][j];
	}
	
	bool ok=true;
	for(int i=0; i<n; i++)
	    for(int j=0; j<m; j++)
		if(a[i][j]<row_h[i] && a[i][j]<col_h[j]) ok=false;

	printf("Case #%d: ", z);
	if(ok) printf("YES\n");
	else printf("NO\n");
    }
    return 0;
}
