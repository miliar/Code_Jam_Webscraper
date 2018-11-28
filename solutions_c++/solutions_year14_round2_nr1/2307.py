#include<stdio.h>
#include<math.h>
#include<string.h>
 int main()
{int t;
scanf("%d",&t);
int x=1;
while(t--)
{
	int i,n;
	scanf("%d",&n);
	char arr[105],arr1[105];
	scanf("%s%s",&arr,&arr1);
	int l=strlen(arr);
	int m=strlen(arr1);
	
		{int flag=0;
		long long int count=0;
	
		if(arr[0]!=arr1[0])
         printf("Case #%d: Fegla Won\n",x);
         else
         {
	      int i=1,j=1;
	     
		while(i<l||j<m)
		{
		//	printf("%lld\n",count);
			if(arr[i]==arr[i-1])
		{if(arr1[j]!=arr1[j-1])
		{
		//	printf("%d\n",i);
			count++;i++;
		
		}
		else{i++;
		j++;
		}
			}
			else if(arr[i]!=arr[i-1])
			{
				if(arr1[j]==arr1[j-1])
				{count++;j++;}
				else {
					if(arr[i]==arr1[j])
					{	//printf("%d %d %c\n",i,j,arr[i]);
					i++;j++;
				}
					else {//printf("%c %c %c %c",arr[i-1],arr1[j-1],arr[i],arr1[j]);
					flag=1; //printf("%d %d",i,j);
					}
				}if(flag)
				break;
				}if(flag)
				break;	
						}
					//	printf("%d",flag);
			if(flag){//printf("%c %c %c %c",arr[i-1],arr1[j-1],arr[i],arr[j-1]);
			printf("Case #%d: Fegla Won\n",x);
			}
			else printf("Case #%d: %lld\n",x,count);}}
			
		
x++;}

return 0;
}
