#include<stdio.h>

void main()
{
	char temp_ch,is_Sucess=0;
	int TTT[100][100]={0,},temp,M=0,N=0,max=0,k=0;
	int T,l,i,j;
	FILE *pFile,*pFile1;
	pFile=fopen("C:\\Users\\ABC\\Desktop\\input.txt","r");
	pFile1=fopen("E:\\output.txt","a");
	fscanf(pFile,"%d",&T);
	temp_ch=fgetc(pFile);
	for(l=1;l<=T;l++)
	 {
		 fscanf(pFile,"%d",&N);
		 temp_ch=fgetc(pFile);
		 fscanf(pFile,"%d",&M);
		 temp_ch=fgetc(pFile);
	  for(i=0;i<N;i++)
	  {
		  for(j=0;j<M;j++)
		  {
			fscanf(pFile,"%d",&temp);
			TTT[i][j]=temp;
		  }
		  temp_ch=fgetc(pFile);
	  } 
	 	for(i=0;i<N;i++)
		  {
			  for(j=0;j<M;j++)
			  {
					  max=TTT[i][j];
					  for(k=0;k<N;k++)
					  {
						  if(TTT[k][j]>max)
							  max=TTT[k][j];
					  }
					  if(max>TTT[i][j])
					  {
						  is_Sucess=0;
					  }
					  else
					  {
						is_Sucess=1;
					  }
					  if(!is_Sucess)
					  {
						  max=TTT[i][j];
						  for(k=0;k<M;k++)
						  {
							  if(TTT[i][k]>max)
								  max=TTT[i][k];
						  }
						  if(max>TTT[i][j])
						  {
							  is_Sucess=0;
							  i=N;
							  j=M;
							  break;
						  }
						  else
						  {
							is_Sucess=1;
						  }
					  }
			  }
		 }
		
	   if(is_Sucess)
	   fprintf(pFile1,"Case #%d: %s\n",l,"YES");
	   else
	   fprintf(pFile1,"Case #%d: %s\n",l,"NO");
	   is_Sucess=0;
	}
	fclose(pFile1);
}