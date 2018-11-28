/*
name:Hatsune_Miku
*/
#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
typedef long long LL;
bool num[10]; 
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	int temp=T;
	while(T--)
	{
		for(LL i=0;i<=9;i++)
		{
			num[i]=false;
		}
		LL n;
		cin>>n;
		if(n==0)
		{
			printf("Case #%d: ",temp-T);
			printf("INSOMNIA\n");
		}
		else
		{
			int k=1;
			while(1)
			{
				LL res=n*k;
				while(res>0)
				{
					num[res%10]=true;
				    res/=10;
				}
				int count=0;
				for(LL i=0;i<=9;i++)
				{
					if(num[i]==false)
					{
						break;
					}
					else count++;	
				}
				if(count==10)
				{
					printf("Case #%d: ",temp-T);
			        printf("%lld\n",n*k);
			        break;
				 }
				 k++;
			}
		}
	}
	return 0;
 } 
