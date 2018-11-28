#include<stdio.h>
#include<stdlib.h>

void main(){
	int n=0;
	int k=0;
	int i=0;
	int j=0;
	int num=0;
    int count=0; 
	float* p1=NULL;
    float* p2=NULL;
	float* p11=NULL;
	float* p22=NULL;
    FILE *in,*out;
    in=fopen("D-large.in","r");
	out=fopen("war-out.txt","a");
    fscanf(in,"%d",&n);
	for(k=0;k<n;k++)
	{
		fscanf(in,"%d",&num);
		p1=(float *)malloc(num*sizeof(float));
	    p2=(float *)malloc(num*sizeof(float));
		p11=(float *)malloc(num*sizeof(float));
		p22=(float *)malloc(num*sizeof(float));
		for(j=0;j<num;j++)
		{
			fscanf(in,"%f",p1+j);
		}
		for(j=0;j<num;j++)
		{
			fscanf(in,"%f",p2+j);
		}
		for(i=0;i<(num-1);i++)
		{
			for(j=(i+1);j<num;j++)
			{ 
				if(*(p1+i)>*(p1+j))
				{
					*(p1+i)=*(p1+i)+*(p1+j);
				    *(p1+j)=*(p1+i)-*(p1+j);
					*(p1+i)=*(p1+i)-*(p1+j);
				}
			}
		}
       for(i=0;i<(num-1);i++)
	   {
			for(j=(i+1);j<num;j++)
			{ 
				if(*(p2+i)>*(p2+j))
				{
					*(p2+i)=*(p2+i)+*(p2+j);
				    *(p2+j)=*(p2+i)-*(p2+j);
					*(p2+i)=*(p2+i)-*(p2+j);
				}
			}
			
	   }
	   for(i=0;i<num;i++)
	   {
	   *(p22+i)=*(p2+i);
	   *(p11+i)=*(p1+i);
	   }
	   count=0;
	   i=0;
		   for(j=0;j<num;j++)
		   {
			   
			   if(*(p11+j)>*(p22+i))
			   {
                   count++;
				   i++;
			   }
		   }
           fprintf(out,"Case #%d: %d",k+1,count);
	   count=num;
	   for(i=0;i<num;i++)
		   for(j=0;j<num;j++)
		   {
		      if(*(p1+i)<*(p2+j))
			  {
		        count--;
                *(p2+j)=-1;
				break;
			  }
		  }
	   fprintf(out," %d\n",count);
		  

	}

    
}