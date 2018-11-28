#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define min(a,b) (a<b?a:b)
#define max(a,b) (a>b?a:b)
int main()
{
    long int i,j,k,l,m,n,p,q,t,x,r,c;	
	FILE *fi,*fo;
	fo=fopen("test.txt", "w+");
	fi=fopen("abc.txt","r");
	fscanf(fi,"%d",&t);
	for(q=0;q<t;q++)
	{
                    
                    fscanf(fi,"%d%d%d",&x,&r,&c);
                    p=c;
                    n=r;
                    r=min(p,n);
                    c=max(p,n);
                    if(x==1)
                    m=0;
                    else if(x==4)
                    {
                         if(r==3&&c==3)
                         m=1;
                         else if(r==3||r==4)
                         m=0;
                         else
                         m=1;
                    }
                    else if(x==2)
                    {
                         if(r%2!=0&&c%2!=0)
                         m=1;
                         else 
                         m=0;
                    }
                    else
                    {
                        if(r==1&&c==3)
                        m=1;
                        else if(r==3||c==3)
                        m=0;
                        else
                        m=1;
                    }
                    if(m==0)
                    fprintf(fo,"Case #%d: GABRIEL\n",q+1);
                    else
                    fprintf(fo,"Case #%d: RICHARD\n",q+1);
   }
   return(0);
}
