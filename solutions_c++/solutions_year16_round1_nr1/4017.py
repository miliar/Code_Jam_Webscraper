#include<bits/stdc++.h>
using namespace std;
int tc,b,n;
char arr[100000];
deque<char>dq;
int main(){
	freopen("A-large (1).in","r",stdin);
	freopen("A-large (1).out","w",stdout);
	scanf("%d",&tc);
	for(int b=1;b<=tc;b++)
	{
		scanf("%s",&arr);
		n=strlen(arr);
		for(int d=0;d<=n-1;d++)
		{
			if(d==0)
			{
				dq.push_back(arr[d]);
			}
			else if(arr[d]>=dq.front())
			{
				dq.push_front(arr[d]);
			}
			else
			{
				dq.push_back(arr[d]);
			}
		}
		printf("Case #%d: ",b);
		for(int f=0;f<=n-1;f++)
		{
			printf("%c",dq.front());
			dq.pop_front();
		}
		printf("\n");
	}
}
