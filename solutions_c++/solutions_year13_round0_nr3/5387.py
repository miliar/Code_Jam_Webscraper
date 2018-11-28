#include<stdio.h>
#include<math.h>
long int rev(int);
int main()
{
	long int s;
	int i,min,max,t,result[100],c,minsq,maxsq,count=0;
	float f;
	FILE* r=NULL;
	FILE* w=NULL;
	r=fopen("C:\\file.txt","r");
	w=fopen("C:\\output.txt","w");
	fscanf(r,"%d",&t);
	c=0;
	while(t!=c)
	{
		fscanf(r,"%d",&min);
		fscanf(r,"%d",&max);
		for(i=min;i<=max;i++)
		{
		 f=sqrt(i);
		 minsq=int(f);
		 if(pow(minsq,2)>=min)
		 break;
		}
		for(i=max;i>=min;i--)
		{
		 f=sqrt(i);
		 maxsq=int(f);
		 if(pow(maxsq,2)<=max)
		 break;
		}
		for(i=minsq;i<=maxsq;i++)
		{
		if(rev(i)==i)
		{
			s=i*i;
		if(rev(s)==s)
		count++;
		}
		}
		result[c++]=count;
		count=0;
	}	
	for(i=0;i<t;i++)
	fprintf(w,"Case #%d: %d\n",i+1,result[i]);
	fclose(r);
	fclose(w);
	return 0;
}
long int rev(int n)
{
	int rem,rev=0;
	while(n!=0)
	{
		rem=n%10;
		n=n/10;
		rev=rev*10+rem;
	}
}
