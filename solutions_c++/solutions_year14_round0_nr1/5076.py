//magic trick

#include<cstdio>
#include<iostream>

int main()
{

    int t;
    scanf("%d",&t);
    int count=1;
    while(t--)
    {
		int a,b,i,j;
		int arr[5][5];
		scanf("%d",&a);
		
		for(i=1;i<5;i++)
		{
			for(j=1;j<5;j++)
			{
				scanf("%d",&arr[i][j]);
			}
		}
		int f[5];
	  for(i=1;i<5;i++)
	  {f[i]=arr[a][i];
	  //printf("%d\n",f[i]);
	  }
	  
	  scanf("%d",&b);
	  
	  
	 	for(i=1;i<5;i++)
		{
			for(j=1;j<5;j++)
			{
				scanf("%d",&arr[i][j]);
			}
		}
		
		int s[5];
	for(i=1;i<5;i++)
	  {s[i]=arr[b][i];
	  //printf("%d\n",s[i]);
	  }
	  
	  int mat=0,match;
	  for(i=1;i<5;i++)
	  {
			for(j=1;j<5;j++)
			{
				if(f[i]==s[j])
				{mat++;match=f[i];}
			}
		}
		if(mat==0)
		printf("Case #%d: Volunteer cheated!\n",count);
		else if(mat==1)
		printf("Case #%d: %d\n",count,match);
		else
		printf("Case #%d: Bad magician!\n",count);
		count++;
	}
	//system("pause");
}
	
