#include <stdio.h>

int m[130][130],x,y,imax[120],jmax[120];
FILE *in = fopen("input.txt","r");
FILE *out = fopen("output.txt","w");

bool check(){
	int i,j;
	for(i=0;i<x;i++){
		for(j=0;j<y;j++){
			if(m[i][j]<imax[i] && m[i][j]<jmax[j])
				return false;
		}
	}
	return true;
}


void main()
{
	int n,i,j,count=0;
		
	fscanf(in,"%d",&n);
	while(count<n)
	{
		count++;
		int com=0;
		fscanf(in,"%d %d",&x,&y);
		for(i=0;i<110;i++){
			imax[i] = -1;
			jmax[i] = -1;
		}
		for(i=0;i<x;i++){
			for(j=0;j<y;j++){
				fscanf(in,"%d",&m[i][j]);
				if(m[i][j] > imax[i])
					imax[i] = m[i][j];
				if(m[i][j] > jmax[j])
					jmax[j] = m[i][j];
			}
		}	
	
		if(check()){
			fprintf(out,"Case #%d: YES\n",count);
		}
		else{
			fprintf(out,"Case #%d: NO\n",count);
		}
	}
}