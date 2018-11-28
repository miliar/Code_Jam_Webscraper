#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int ar[2000];
char s[2000];
int main()
{
    long int i,j,k,l,m,n,p,q,t,sum;	
	FILE *fi,*fo;
	fo=fopen("test.txt", "w+");
	fi=fopen("abc.txt","r");
	fscanf(fi,"%d",&t);
	for(q=0;q<t;q++)
	{
           fscanf(fi,"%d %s",&n,&s);
           //fprintf(fo,"%da\n%s",n,s);
           for(i=0;i<strlen(s);i++)
           ar[i]=s[i]-'0';
           sum=0;
           m=0;
           if(ar[0]==0)
           {
                       m++;
                       sum++;
           }
           else
           sum+=ar[0];
           for(i=1;i<=n;i++)
           {
                            if(sum<i)
                            {
                                //fprintf(fo,"a%d\n",i);
                                m++;
                                sum++;
                            }
                            sum+=ar[i];
           }
           fprintf(fo,"Case #%d: %d\n",q+1,m);
    }
    return(0);
}
