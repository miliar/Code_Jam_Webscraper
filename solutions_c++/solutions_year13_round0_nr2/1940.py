#include <stdio.h>
int n,m;
int a[101][101];
int max_line[101];
int max_col[101];
bool judge()
{
	for(int i=0;i<n;i++){
		max_line[i]=0;
		for(int j=0;j<m;j++){
			if(max_line[i]<a[i][j])
				max_line[i]=a[i][j];
		}
	}
	for(int j=0;j<m;j++){
		max_col[j]=0;
		for(int i=0;i<n;i++){
			if(max_col[j]<a[i][j])
				max_col[j]=a[i][j];
		}
	}
	
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(a[i][j]<max_line[i] && a[i][j]<max_col[j])
				return false;
		}
	}
	return true;
}
int main(int argc, char **argv)
{
	int tc=0;
	scanf("%d",&tc);
	for (int c = 1; c <= tc; ++c)
	{
			scanf("%d %d",&n,&m);
			for(int i=0;i<n;i++){
				for(int j=0;j<m;j++){
					scanf("%d",&a[i][j]);
				}
			}
			
			if(judge()){
				printf("Case #%d: YES\n",c);
			}else{
				printf("Case #%d: NO\n",c);
			}
	}
	return 0;
}
