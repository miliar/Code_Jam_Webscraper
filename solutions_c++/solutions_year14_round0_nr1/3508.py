
#include<cstdio>
#include<cstring>
FILE *fp_in,*fp_out;
int main(){
	int t,i,j,k=1,a[4][4],b[4][4],x,y;
	if((fp_in=fopen("A-small-attempt6.IN","r"))==NULL)
	{
		printf("1error\n");
		return 0;
	}
	if((fp_out=fopen("out","w"))==NULL)
	{
		printf("2error\n");
		return 0;
	}
	fscanf(fp_in,"%d",&t);
	while(t--){
		fscanf(fp_in,"%d",&x);
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			fscanf(fp_in,"%d",&a[i][j]);
		fscanf(fp_in,"%d",&y);
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			fscanf(fp_in,"%d",&b[i][j]);
		int th,cnt=0;
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			if(a[x-1][i]==b[y-1][j])
				th=i,cnt++;
		fprintf(fp_out,"Case #%d: ",k++);
		if(cnt==1)fprintf(fp_out,"%d\n",a[x-1][th]);
		else if(cnt==0)fprintf(fp_out,"Volunteer cheated!\n");
		else fprintf(fp_out,"Bad magician!\n");
	}
	fclose(fp_in);
	fclose(fp_out);
	return 0;
}
