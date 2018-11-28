#include <iostream>
#include<stdio.h>
using namespace std;

int main() {
	long long int t_in[101],visited[10],v[101],store[101][10000];
	int count=0,i=0,j,k,t,n,a,b,flag=1,t_c=0;
	int t_c1=0,t_c2=0,t_c3=0,t_c4=0,t_c5=0,t_c6=0,t_c7=0,t_c8=0,t_c9=0;
	int g;
	while(1)
	{
	    scanf("%lld",&t_in[i]);
	    i++;
	    
	    if(count==t_in[0])
	    {
	        break;
	    }
	    count++;
	}
	
	    for(j=1;j<=t_in[0];j++)
	    {
	        int t = t_in[j]; 
	      for(k=0;k<=200;k++)
	      { 
	         store[j][k] = t * k;
	       }
	    }
	    
	 for(i=1;i<=t_in[0];i++)
	  {
	    flag=1;
	    t_c=0,t_c1=0,t_c2=0,t_c3=0,t_c4=0,t_c5=0,t_c6=0,t_c7=0,t_c8=0,t_c9=0;
	    for(k=1;k<=200;k++)
	    {
	          
	    n = store[i][k];
	    g = n;
	     while(n!=0)
        {
         a=n%10;
         n=n/10;
         if(a==0)
         {
          visited[0]=0;
          t_c++;
         }
         else if(a==1)
         {
          visited[1]=1;
          t_c1++;
         }
         else if(a==2)
         {
          visited[2]=2;
          t_c2++;
         }
         else if(a==3)
         {
          visited[3]=3;
          t_c3++;
         }
         else if(a==4)
         {
          visited[4]=4;
          t_c4++;
         }
         else if(a==5)
         {
          visited[5]=5;
          t_c5++;
         }
         else if(a==6)
         {
          visited[6]=6;
          t_c6++;
         }
         else if(a==7)
         {
          visited[7]=7;
          t_c7++;
         }
         else if(a==8)
         {
          visited[8]=8;
          t_c8++;
         }
         else if(a==9)
         {
          visited[9]=9;
          t_c9++;
         }
         
          
        }
        if(t_c>=1 && t_c1>=1 && t_c2>=1 && t_c3>=1 && t_c4>=1 && t_c5>=1 && t_c6>=1 && t_c7>=1 && t_c8>=1 && t_c9>=1) 
         {
            break;
         }
	   }
	   for(b=0;b<10;b++)
	   {
	    
        if(visited[b]==b)
            flag=0;
        else
            flag=1;
	  }
	  if(flag == 0)
	  {
	      printf("Case #%d: %d",i,g);
	      printf("\n");
	  }
	  else
	  {
	      printf("Case #%d: INSOMNIA",i);
	      printf("\n");
	  }
	  }
	
	return 0;
}
