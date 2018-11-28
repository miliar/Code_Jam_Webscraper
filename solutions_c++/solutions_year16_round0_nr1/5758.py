#include <stdio.h>
int main(void) {
	int t,n,i,c,a[10],k,m,j,p,z;
	scanf("%d",&t);
	for(z=1;z<=t;z++)
	{
	    scanf("%d",&n);
	    FILE *fptr;
	    fptr=fopen("output.txt","a");
	    if(n!=0)
	    {
	        for(i=0;i<10;i++)
	        a[i]=0;
	        p=0;
	        for(i=1;p!=1;i++)
	        {
	            k=i*n;
	            c=k;
	           //	printf("s%d\n",n);
	            while(k!=0)
	            {
	                m=k%10;
	                a[m]=1;
	                k=k/10;
	            }
	            if(a[0]==1 && a[1]==1 && a[2]==1 &&a[3]==1 &&a[4]==1 &&a[5]==1 &&a[6]==1 &&a[7]==1 &&a[8]==1 &&a[9]==1)
	            p=1;
	            /*s=0;
	            for(j=1;j<10;j++)
	            s=s+a[j];*/
	        }
	        fprintf(fptr,"Case #%d: %d\n",z,c);
	    }
	    else
	    fprintf(fptr,"Case #%d: INSOMNIA\n",z);
	}
	return 0;
}


