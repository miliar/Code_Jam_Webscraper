#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;
#define maxn 1000000
int a[maxn];
struct Node
{
	int value;
	int cnt;
}queue[maxn];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,N,A;
	scanf("%d",&T);
	for(int csT = 1; csT <= T; csT++)
	{
		int i;
		scanf("%d%d",&A,&N);
		for(i = 0; i < N; i++)
		{
			scanf("%d",a + i);
		}
		sort(a,a + N);	
		int front,rear;
		front = rear = 0;
		queue[rear].value = A;
		queue[rear++].cnt = 0;
		for(i = 0; i < N; i++)
		{
			int tt = rear;
			int j;
			for(j = front; j != rear;)
			{
				if(queue[j].value > a[i])
				{
					queue[tt].value = queue[j].value + a[i];
					queue[tt].cnt = queue[j].cnt;
					tt++;
				}else
				{
					int tmp = queue[j].value;
					int tcnt = 0;
					if(queue[j].value != 1)
					{
						while(tmp <= a[i])
						{
							tmp += tmp - 1;
							tcnt++;
						}
						queue[tt].value = tmp + a[i];
						queue[tt].cnt = tcnt + queue[j].cnt;
						tt++;
					}
					queue[tt].value = queue[j].value;
					queue[tt].cnt = queue[j].cnt + 1;
					tt++;
				}
				j = (j + 1)%maxn;
			}
			front = rear % maxn;
			rear = tt % maxn;
		}
		int ans = 0x3f3f3f3f;
		for(i = front; i != rear;)
		{
			ans = min(ans, queue[i].cnt);
			i = (i + 1)%maxn;
		}
		printf("Case #%d: %d\n",csT,ans);
	}
	return 0;
}
