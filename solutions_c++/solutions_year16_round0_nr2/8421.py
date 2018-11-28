#include<bits/stdc++.h>
int tc,n,total;
char arr[1000];
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large-output.txt","w",stdout);
	scanf("%d",&tc);
	int temp;
	for(int a=1;a<=tc;a++)
	{
		total=0;
		scanf("%s",arr);
		n=strlen(arr);
		int y=0;
		for(int b=n-1;b>=0;b--)
		{
			y=0;
			//printf("%c\n",arr[0]);
			if(arr[0]=='+' && arr[b]=='-')
				{
					for(int z=0;z<=1000;z++)
					{
						//printf("%c\n",arr[z]);
						
						if(arr[z]=='-')
						{
							//printf("%d\n",z);
							break;
						}
						arr[z]='-';
						
					}
					y=1;					
					//printf("sdafasdf");
					/*
					printf("first   ");
					for(int t=0;t<=n-1;t++)
					{
						printf("%c",arr[t]);
					}
					printf("\n");
					*/
				}
				if(y==1)
				{
					total++;
				}
			if(arr[b]=='-')
			{	
				for(int c=0;c<=(b)/2;c++)
				{
					temp=arr[c];
					arr[c]=arr[b-c];
					arr[b-c]=temp;
					
				}
				for(int d=0;d<=(b);d++)
				{
					if(arr[d]=='+')
					{
						arr[d]='-';
					}
					else
					{
						arr[d]='+';
					}
				}	
				
				/*
				printf("second   ");
					for(int t=0;t<=n-1;t++)
					{
						printf("%c",arr[t]);
					}
					printf("\n");
				*/
				total++;
			}
		}
		printf("Case #%d: %d\n",a,total);
	}
}
