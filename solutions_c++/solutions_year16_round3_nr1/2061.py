#include<bits/stdc++.h>
using namespace std;
int main()
{

	int t;
	scanf("%d",&t);int t1=0;
	while(t--)
	{t1++;
		int n;
		scanf("%d",&n);
		int arr[100];
		int vis[30];
		vector<string>v;
		for(int i=0;i<27;i++)vis[i] = 0;int cnt=0;
		for(int i=0;i<n;i++) { scanf("%d",&arr[i]); cnt+=arr[i];}
		//	printf("%d\n",cnt);
			printf("Case #%d: ",t1);
		while(1)
		{	if(cnt<=0)break;
			int ma = 0,ma2=0,id;int x=0,id2=0,f3=0;
			for(int i=0;i<n;i++)
			{
				if(arr[i]>ma)
				{
					ma = arr[i];
					id = i;f3=-1;
				}
				else if(arr[i]==ma && f3==-1){id2=i;f3=1;}
				if(arr[i]) x+=arr[i];

			}
			
			if(x==2 )
				 {
				int p=2;int x3=0;
				for(int i=0;i<n;i++)
				{
					if(arr[i]>0){ printf("%c",'A'+i);arr[i]--;x3++;}
					if(x3==2)break;
				}
				printf(" ");cnt-=2;
			}
			else if(f3==1 && x!=3)
			{
				printf("%c%c ",'A'+id,'A'+id2);
				arr[id]--;arr[id2]--;cnt-=2;
			}
			else 
			{
				printf("%c ",'A'+id);
				arr[id]--;cnt--;
			}
			
	}
	
	printf("\n");
}
	return 0;
}