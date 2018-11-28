#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <vector>
#define SIZE 1005

using namespace std;

/*
�������������������Ƃ͌���Ȃ�
9
->3 3 3 �� 5
  4 5 �� 6
4 5, 2 3 4, 2 2 2 3, 1 2 2 2 2 x

�ő�ƂȂ�̂����ߑł�(=M) ������AD��[(D+M-1)/M]�ɕ������̂�
M+��([(D+M-1)/M]-1)
�ł���B
[(D+M-1)/M]=i <=> iM<=D+M-1<(i+1)M <=> (i-1)M+1<=D<=iM
�Ȃ̂ŁA���̒��ɂ������imos���ĉ�����
*/
int cnt[3*SIZE];

int get(int s,int t)
{
	return cnt[t]-(s==0?0:cnt[s-1]);
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int n;
		scanf("%d",&n);
		memset(cnt,0,sizeof(cnt));
		for(int i=0;i<n;i++)
		{
			int x;
			scanf("%d",&x);
			cnt[x]++;
		}
		for(int i=1;i<3*SIZE;i++) cnt[i]+=cnt[i-1];
		int ret=SIZE;
		for(int i=1;i<SIZE;i++)
		{
			int sum=0;
			for(int j=1;(j-1)*i+1<SIZE;j++)
			{
				int s=(j-1)*i+1,t=j*i;
				sum+=j*get(s,t);
			}
			ret=min(ret,sum+i-n);
		}
		printf("Case #%d: %d\n",t,ret);
	}
	return 0;
}
