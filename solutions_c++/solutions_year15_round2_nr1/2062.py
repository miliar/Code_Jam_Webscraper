#include<cstdio>
#include<queue>
#include<string>
using namespace std;
int arr[1000005];
int main(void)
{
   	freopen("C:\\Users\\user\\Desktop\\A-small-attempt3.in","r",stdin);
freopen("C:\\Users\\user\\Desktop\\out2.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int g;
		scanf("%d",&g);
		int count=0;
		queue <int> qu;
		qu.push(1);
		arr[1]=1;
		
		while(1)
		{
			
			int p,n=0;
			p=qu.front();
			int c=p;
			//printf("%d %d\n",p,arr[p]);
			if(p==g)
			{
				printf("Case #%d: %d\n",i,arr[g]);
				break;
			}
			if(arr[p+1]==0)
			{
				qu.push(p+1);
			    arr[p+1]=arr[p]+1;
			}
            while(c!=0)
			{
				n=n*10;
				n=n+c%10;
				c=c/10;
		    }
			if(arr[n]==0&&n<=g)
			{
			   qu.push(n);
			   arr[n]=arr[p]+1;
			}
			qu.pop();
		}
		memset(arr,0,sizeof(arr));
	}
	return 0;
}