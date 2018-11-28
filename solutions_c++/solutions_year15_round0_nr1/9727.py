#include <stdio.h>

int main() {
	int tc,t,Smax,i,temp;
	long stand,count;
	scanf("%d",&tc);
	for(t=1;t<=tc;t++)
	{
	    count=0;
	    scanf("%d\n",&Smax);
	    char shy[Smax+1];gets(shy);
        stand=(int)shy[0]-48;
        for(i=1;i<=Smax;i++)
        {
            if(stand>=i)
                stand+=((int)shy[i]-48);
            else
            {
                temp=i-stand;
                stand+=((int)shy[i]-48+temp);
                count+=temp;
            }
        }
        printf("Case #%d: %ld\n",t,count);
	}
	return 0;
}
