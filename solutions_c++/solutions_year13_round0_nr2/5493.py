#include <stdio.h>
#include <stdlib.h>
#define MAX 100
FILE *fi;
FILE *fo;
int a[MAX][MAX];
int b[MAX][MAX];
int m,n;
int num;
int i,j;

int isokay(int x,int y,int val){
	if(a[x][y]<=val)
		return 1;
	else
		return 0;
}
int search(int x,int y)
{	
	int xresult=0;
	int yresult=0;
	for(int xi=0;xi<n;xi++){
		if(a[xi][y]>a[x][y])
		{	xresult=1;
		break;
		}
	}
	for(int xi=0;xi<m;xi++){
		if(a[x][xi]>a[x][y])
		{	yresult=1;
		break;
		}
	}
	if(xresult==0||yresult==0)
		return 1;
	else
		return 0;
}






int main(){
	fi=fopen("B-large.in","r");
	fo=fopen("B-large.out","w");
	int res=0;
	int z;
	fscanf(fi,"%d",&num);
	for(z=0;z<num;z++){
		res=0;
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				b[i][j]=0;
			}
		}

		//max=0;
		fscanf(fi, "%d %d",&n,&m);
		for(i=0;i<n;i++){
			for (j=0;j<m;j++){
				fscanf(fi,"%d",&a[i][j]);
			}
		}
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				b[i][j]=search(i,j);
			}
		}
		for(i=0;res==0&&i<n;i++){
			for(j=0;res==0&&j<m;j++){
				if(b[i][j]==0){
					res=1;
					fprintf(fo,"Case #%d: NO\n",z+1);
				}
			}
		}
		if (res==0){
			fprintf(fo,"Case #%d: YES\n",z+1);
		}
	}

	fclose(fi);
	fclose(fo);

	return 0;
}