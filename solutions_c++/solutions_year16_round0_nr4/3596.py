#include<bits/stdc++.h>
long long int check();
long long int arr[1000]={NULL};
int k,c,s;
int main()
{
	//freopen("input.in","r",stdin);
	//freopen("output.in","w",stdout);
	int test,t,len;
	scanf("%d",&test);
	t=test;
	while(test--)
		{
			scanf("%d %d %d",&k,&c,&s);
			len = check();
			if(len == 0)
				printf("Case #%d: IMPOSSIBLE\n",t-test);
			else
				{
				printf("Case #%d: ",t-test);
				for(int i=0;i<len;i++)
					printf("%lld ",arr[i]);
				printf("\n");
				}
		}
}
long long int check()
{
long long int i,j,l,flag=0;
memset(arr,0,sizeof(arr));
if(c==1)
	{
	if(s<k)
	flag = 1;
else
	{
		for(j=0;j<k;j++)
		arr[j]=j+1;
	}

	}
else
	{
		i=0;
		l=k;
		j=0;
		while(i!= (k%2==0?k/2:k/2 +1))
		{
			arr[j++] = k*i + l;
			i++;
			l--;
			if(j>s)
				{
					flag=1;
					break;
				}
		}
	}
if(flag == 1)
	return 0;
else
	return j;
}
