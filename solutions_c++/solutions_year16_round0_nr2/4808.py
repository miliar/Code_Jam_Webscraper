#include<stdio.h>
#include<string.h>
int main(){
	int tc,top,i,j,count,bottom,inc=1,l,mid;
	scanf("%d",&tc);
	while(tc--)
	{
		char str[109],temp;
		scanf("%s",str);
		l=strlen(str);
		count=0;
		while(1)
		{
			bottom=l-1;
			top=0;
			while(str[bottom]=='+')
			bottom--;
			if(bottom>0)
			{
				if(str[top]=='+')
				{
					count++;
					while(str[top]=='+')
					str[top++]='-';
				}
//			if(top==l-1)
//			break;
				top=0;
				mid=(top+bottom)/2;
				count++;
				for( ; top<=mid ; top++,bottom--)
				{
					temp=str[top];
					if(str[bottom]=='-')
					str[top]='+';
					else
					str[top]='-';
					if(temp=='+')
					str[bottom]='-';
					else
					str[bottom]='+';
				}
			}
			else 
			{
				if(bottom==0)
				count++;
				break;
			}
		}
		printf("Case #%d: %d\n",inc++,count);
	}
	return 0;
}
