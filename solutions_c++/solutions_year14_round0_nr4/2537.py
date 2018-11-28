#include<stdio.h>
#include<conio.h>
int main()
{
	FILE *fp,*fp1;
	int j,k,i,testcase,wins,arraysize;
	double arrayelement1[1000],temp,arrayelement2[1000];
	fp = fopen("a.txt","r"); // read mode
	fp1=fopen("b.txt","w");
	fscanf(fp,"%d",&testcase);
	for(i=1;i<=testcase;i++)
	{
		fscanf(fp,"%d",&arraysize);
		for(k=0;k<arraysize;k++)
		{
			fscanf(fp,"%lf",&temp);
			for(j=k-1;j>=0;j--)
			{
				if(temp>arrayelement1[j])
					break;
				else
					arrayelement1[j+1]=arrayelement1[j];
			}
			arrayelement1[j+1]=temp;
		}
		for(k=0;k<arraysize;k++)
		{
			fscanf(fp,"%lf",&temp);
			for(j=k-1;j>=0;j--)
			{
				if(temp>arrayelement2[j])
					break;
				else
					arrayelement2[j+1]=arrayelement2[j];
			}
			arrayelement2[j+1]=temp;
		}
		j=arraysize-1;
		wins=0;
		fprintf(fp1,"\nCase #%d: ",i);
		for(k=arraysize-1;k>=0&&j>=0;)
		{
			if(arrayelement1[k]>arrayelement2[j])
			{
				k--;
				j--;
				wins++;
			}
			else
			{
				j--;
			}
		}
		fprintf(fp1,"%d ",wins);
		j=0;
		wins=arraysize;
		for(k=0;k<arraysize&&j<arraysize;)
		{
			if(arrayelement1[k]<arrayelement2[j])
			{
				k++;
				j++;
				wins--;
			}
			else
			{
				j++;
			}
		}
		fprintf(fp1,"%d",wins);
	}
	fclose(fp);
	fclose(fp1);
	return(1);
}



