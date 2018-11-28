#include<iostream>
using namespace std;
int T,B,N,time[1010],remain[1010];

int maxCommonDivisor(int m, int n) {  
  
        if (m < n) {// 保证m>n,若m<n,则进行数据交换  
            int temp = m;  
            m = n;  
            n = temp;  
        }  
        while (m % n != 0) {// 在余数不能为0时,进行循环  
            int temp = m % n;  
            m = n;  
            n = temp;  
        }  
        return n;// 返回最大公约数  
    }  
  
    // 求最小公倍数  
int minCommonMultiple(int m, int n) {  
        return m * n / maxCommonDivisor(m, n);  
} 


int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int step,res=0,oneround;	
	scanf("%d",&T);
	for(int k=1;k<=T;k++)
	{
		memset(remain,0,sizeof(remain));
		scanf("%d",&B);
		scanf("%d",&N);
		step=0;
		res=-1;
		
		int mintime=0;

		for(int i=0;i<B;i++)
			scanf("%d",&time[i]);
		if(B==1)
			res=1;

		else
		{
			mintime=minCommonMultiple(time[0],time[1]);
			for(int i=2;i<B;i++)
				mintime=minCommonMultiple(mintime,time[i]);
			oneround=0;
			for(int i=0;i<B;i++)
			{
				oneround+=mintime/time[i];
			}
			N%=oneround;
			if(N==0)N+=oneround;
			while(res==-1)
			{
			
				for(int i=0;i<B;i++)
				{
					if(remain[i]==0)
					{
						step++;
						if(step==N){
							res=i+1;
							break;
						}
						remain[i]=time[i];
					}
				}
				for(int i=0;i<B;i++)
					remain[i]--;
			}
		}
		printf("Case #%d: %d\n",k,res);

	}
	fclose(stdin);
	fclose(stdout);

	return 0;
}