#include<stdio.h>
#include<string.h>
main()
{
	int test,test1=1,test2=1;
	long long ans[105];
	scanf("%d",&test);
	
	char s[11];
	int i,top,top1;
	long long count=0;
	
	while(test1!=test+1)
	{
	
		scanf("%s",s);
	int start = 0; 
	int end;
	end=strlen(s)-1;
	
    while (start< end)
    {
        char temp = s[start];
        s[start] = s[end];
        s[end] = temp;
        start++;
        end--;
    }
	top=strlen(s)-1;
	if(top==0)
	{
		if(s[0]=='-')
		{
			count=1;
			ans[test1]=count;
			count=0;
			test1=test1+1;
			continue;
			
		}
		else
		{
			count=0;
			ans[test1]=count;
			test1=test1+1;
			count=0;
			continue;
		}
	}
//	printf("%s %d",s,top);
	top1=top;
	while(1)
	{
		if(s[top1]=='-' && s[top1-1]=='+')
		{
			while(top+1!=top1)
			{
				s[top1++]='+';
				
			}
			count=count+1;
			top1=top1-1;
		}
		else if(s[top1]=='+' && s[top1-1]=='-')
		{
			while(top!=top1)
			{
				s[top1++]='-';
	
			}	
			count=count+1;
			top1=top1-1;
		}
		else if(top1==0)
		{
	
				if(s[top1]=='-')
				{
				count=count+1;
				}
			
			

			ans[test1]=count;
			count=0;
			test1=test1+1;
			break;
		}
		else
		{
		top1=top1-1;
		}
	}
	//printf("t2%d",test1);
}
while(test2!=test+1)
{
	printf("Case #%d: %llu\n",test2,ans[test2]);
	test2=test2+1;
}
}
