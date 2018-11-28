#include<iostream>
#include<string>

using namespace std;
int main()
{
freopen("A-large.in", "r", stdin);
    freopen("a_large.out", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
	char str[1000];
	int i=0;
	int t;
	int before=0;
	int after=0;
	scanf("%d",&t);
	int case1=1;	
	while(t>0)
	{
		scanf("%s",str);
		//printf("%s.......",str);
		int len=strlen(str);
		int mid=0;
		int min=0;
		char temp[len+1];
		int front=-1;
		int rear=-1;
		front =0;
		rear=1;
		temp[0]=str[0];
		for(i=1;i<len;i++)
		{
			if(str[i]>=temp[front])
			{
				if(front-1<0)
					front = len-1;
				else
					front--;
				temp[front] = str[i];
			}
			else
			{
				temp[rear] = str[i];
				rear++;
			}
		}
		printf("Case #%d: ",case1);
		case1++;
		for(i=0;i<len;i++)
		{
			
			printf("%c",temp[front]);
			if(front+1==len)
				front=0;
			else
				front++;
		}
		cout<<endl;
		t--;
	}
}
