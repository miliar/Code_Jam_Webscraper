#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int calcMinRequired(int smax,char str1[])
{
	int i=0,count=0,req=0,si;
	//printf("smax:%d, str:%s ",smax,str1);
	count += str1[0]- '0';
	for(i=1;i<=smax;i++)
	{
		si = str1[i]-'0';
		if(si!=0 && i > (count+req))
			req = i-count;
		count +=si;
		//printf("count:%d,req:%d,i:%d",count,req,i);		
		
	}
	//printf("case:", req);
	return req;
}


int main(int argc,char** argv)
{
    int numberofTestCases = 0,i=0,smax[100];
	char str[100][1000];
    scanf("%d",&numberofTestCases);
	if(numberofTestCases <= 0)
		return 0;
	for(i=0;i<numberofTestCases;i++) 
    {
		scanf("%d",&smax[i]);
		scanf("%s",&str[i]);
	}
    for(i=0;i<numberofTestCases;i++) 
    {
		printf("case #%d: %d\n", i+1,calcMinRequired(smax[i],str[i]));
     
    }
	return 0;
}

