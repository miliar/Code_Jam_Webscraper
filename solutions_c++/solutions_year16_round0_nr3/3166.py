#include<stdio.h>
#include<math.h>
int main()
{
	 int n,j,i,k,flag=0,x=0,c=0;
	 unsigned long long int m;
	 int s[17];
	 s[0]=1;
	 s[15]=1;
	 FILE *fptr;
     fptr=fopen("output.txt","a");
     fprintf(fptr,"Case #1: \n");
     for(j=1;j<=16384;j++)
     {
      int rem;
      for(i=1;i<=14;i++)
      {
      	s[i]=0;
	  }
      i=14;
      n=j;
      while (n!=0)
      {
        rem=n%2;
        n/=2;
        s[i]=rem;
        i--;
      }
      i=0;
      for(i=2;i<=10;i++)
      {
      	m=0;
      	 for(k=0;k<=15;k++)
      	{
      	 	m=m*i+s[k];
		}
		 for(k=2;k<=sqrt(m);k++)
		 {
		 	if(m%k==0)
		 	{
		 		flag=1;
		 		break;
			}
		 }
		 if(flag==1)
		 x++;
		 flag=0;
	  }
	  if(x==9)
	  {
	  	for(i=0;i<=15;i++)
	  	{
	  		fprintf(fptr,"%d",s[i]);
		}
			fprintf(fptr," ");
	  	for(i=2;i<=10;i++)
       {
      	m=0;
      	 for(k=0;k<=15;k++)
      	{
      	 	m=m*i+s[k];
		}
		 for(k=2;k<=sqrt(m);k++)
		 {
		 	if(m%k==0)
		 	{
		 		fprintf(fptr,"%d ",k);
		 		break;
			}
		 }
		 
	  }
	  fprintf(fptr,"\n");
	  c++;
	  if(c==50)
	  break;
	  }
	  x=0;
	  flag=0;
     }
    return 0;
}

