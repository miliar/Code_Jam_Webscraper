#include <stdio.h>
#include<string.h>
int main(void) {
    int t,c,i,j,flag1,flag2,n;
    scanf("%d\n",&t);
    for(i=1;i<=t;i++)
    {
	    char a[101];
	    scanf("%s",a);
	    FILE *fptr;
	    fptr=fopen("output.txt","a");
	   n=strlen(a);
	    c=0;j=0;
	     while(j<n)
	    {
	    	flag1=1,flag2=1;
	        while(a[j]=='+')
	        {
	            j++;
	            flag1=0;
	        }
	        while(a[j]=='-')
	        {
	           
	            j++;
	            flag2=0;
	        }
	        if(flag1==0 && flag2==0)
	        c=c+2;
	        else if(flag1==0 && flag2==1)
	        c;
	        else
	        c++;
	    }
 fprintf(fptr,"Case #%d: %d\n",i,c);
    }
	return 0;
}


