#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
	int run = 1;
	int tt;
	int a,n;
	int mote[10000];
	long long sum[10000];
	int summer;
	int max;
	long long oper = 0;
	int point = 0;
	int end;
	int ftime;
	int ctmp;
	scanf("%d",&tt);
	while(run<=tt)
	{
		oper = 0;
		point = 0;
		ctmp = 0;
		scanf("%d %d",&a,&n);
		end = n;
		for(int i=0;i<n;i++)
		{
			scanf("%d",&mote[i]);
		}
		sort(mote,mote+n);
		sum[0] = a;
		summer = 0;
		ftime = 0;
		/*for(int i=1;i<=n;i++)
		{
			sum[i] = sum[i-1]+mote[i-1];
		}*/
		while(point<end)
		{
			if(point!=0)
				sum[point] = sum[point-1]+mote[point-1];
			if(sum[point]>mote[point])
			{
				point++;
				continue;
			}
			else
			{
				int count = 0;
				int time = end-point;
				long long tmp = sum[point];
				//ftime = time;
				while(count<=time&&tmp<=mote[point])
				{
					tmp*=2;
					tmp--;
					count++;
					//printf("=%d\n",tmp);
				}
				if(count<time)
				{
					oper+=count;
					sum[point] = tmp;
					//printf("A/%d\n",tmp);
					ctmp+=count;
					//ftime = time;
				}
				else
				{
					//if(oper+time<n)
						oper+=time;
					//else
					//	oper = n;
					//printf("B%d",tmp);
					break;
				}
				if(oper>n)
				{
					oper = n;
					break;
				}
			}
			point++;
		}
		if(oper>n)
		{
			oper = n;
		}
		printf("Case #%d: %lld\n",run,oper); //ANS
		run++;
	}
	return 0;
}
