#include<stdio.h>

void main()
{
	char temp_ch;
	int temp,r,t,paint_left=0,num_blackRings=0,radius_lastBlackRing=0,radius_BlackRing=0,paint_needed=0;
	int T,l,i,j;
	FILE *pFile,*pFile1;
	pFile=fopen("C:\\Users\\ABC\\Desktop\\input.txt","r");
	pFile1=fopen("E:\\output.txt","a");
	fscanf(pFile,"%d",&T);
	temp_ch=fgetc(pFile);
	for(l=1;l<=T;l++)
	 {
		 fscanf(pFile,"%d",&r);
		 temp_ch=fgetc(pFile);
		 fscanf(pFile,"%d",&paint_left);
		 temp_ch=fgetc(pFile);
		 radius_lastBlackRing=r+1;
		 paint_left-=(radius_lastBlackRing*radius_lastBlackRing-r*r);
		 num_blackRings++;
		 while(paint_left>0)
		 {
			radius_BlackRing=radius_lastBlackRing+2;
			paint_needed=(radius_BlackRing*radius_BlackRing-(radius_lastBlackRing+1)*(radius_lastBlackRing+1));
			if(paint_left>=paint_needed)
			{
				num_blackRings++;
				paint_left-=paint_needed;
			}
			else
				paint_left=0;
			radius_lastBlackRing=radius_BlackRing;

		 }
	 	
	   fprintf(pFile1,"Case #%d: %d\n",l,num_blackRings);
	   num_blackRings=0;
	   radius_lastBlackRing=0;
	   radius_BlackRing=0;
	   paint_needed=0;
	}
	fclose(pFile1);
}