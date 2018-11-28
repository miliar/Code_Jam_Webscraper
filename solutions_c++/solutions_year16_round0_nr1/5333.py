#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int t,input;
bool sudah[10];
bool cek()
{
	for(int i=0;i<10;i++)
	{
		if(!sudah[i])
		return false;
	}
	return true;
}
void ambil(int a)
{
	if(a==0)
	sudah[0]=true;
	while(a>0)
	{
		sudah[a%10]=true;
		a/=10;
	}
}
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		memset(sudah,false,sizeof(sudah));
		scanf("%d",&input);
		long long angka=input;
		ambil(input);
		if(input!=0)
		{
			while(!cek())
			{
				angka+=input;
				ambil(angka);
			}
		}
		printf("Case #%d: ",i);
		if(input==0)
		printf("INSOMNIA\n");
		else printf("%lld\n",angka);
		
	}
}
