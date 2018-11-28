#include<bits/stdc++.h>
using namespace std;

deque<char> deq;
char in[10005];
int main()
{
	int test;
	scanf("%d",&test);getchar();
	for(int a=1;a<=test;a++)
	{
		gets(in);
		int len=strlen(in);
		deq.push_front(in[0]);
		char ff=in[0];
		for(int b=1;b<len;b++)
		{
			if(in[b]>=ff)
			{
				deq.push_front(in[b]);
				ff=in[b];
			}
			else
			{
				deq.push_back(in[b]);
			}
		}
		printf("Case #%d: ",a);
		while(!deq.empty())
		{
			printf("%c",deq.front());
			deq.pop_front();
		}
		printf("\n");
	}
}
