#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
typedef long long ll;
//typedef mod 1000000007;
int book[15],c=1;
using namespace std;
int main()
{
	ll t,i,j,n,num,k;
	freopen("A-large.in","r",stdin); //输入重定向，输入数据将从in.txt文件中读取 
	freopen("out.out","w",stdout); //输出重定向，输出数据将保存在out.txt文件中 
	scanf("%lld",&t);
	while(t--)
	{
		num=0;
		j=2;
		memset(book,0,sizeof(book));
		scanf("%d",&n);
		k=n;
		if(!n)
		{
			printf("Case #%d: INSOMNIA\n",c++);
			continue;
		}
		while(num!=10)
		{
			ll tmp=k;
			while(tmp>0)
			{
				ll tmp1=tmp%10;
				if(!book[tmp1])
				{
					num++;
					book[tmp1]++;
				}
				tmp/=10;
			}
			if(num<10)
			k=n*(j++);
		}
		printf("Case #%d: %lld\n",c++,k);
	}
	fclose(stdin);//关闭文件 
	fclose(stdout);//关闭文件 
	return 0;
 } 		
