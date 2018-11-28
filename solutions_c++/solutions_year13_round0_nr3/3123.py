#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int map[10000005];

int strlen(char* ch)
{
	int cnt = 0;
	for(int i=0; i<sizeof(ch); i++)
	{
		if(ch[i] >= '0' && ch[i] <= '9')cnt++;
		else break;
	}
	return cnt;
}


int test(int n)
{
	char ch[10];
	memset(ch, '*', sizeof(ch));
	int mid = 1;
	sprintf(ch,"%d",n);
	int len = strlen(ch);
	for(int j=0; j<len; j++)
	{
		if(ch[j] != ch[len-j-1])
		{
			mid = 0;
			break;
		}
	}
	return mid == 0 ? 0 : 1;
}

int test2(int n)
{
	for(int i=1; i<=n/2+1; i++)
	{
		if(i*i == n) return i;
	}
	return 0;
}

int main()
{
#ifndef ONLINE_JUDGE
//freopen("D:\\in.txt","r",stdin);
//freopen("D:\\out.txt", "w", stdout);
#endif
	int k, th = 1,i;
	cin>>k;
	memset(map, 0, sizeof(map));
	for(i=1; i<=10000; i++)
	{
		int ii = test2(i);
		if(test(i) && ii && test(ii))map[i] = 1;
	}
	while(k--)
	{
		int a, b, cnt = 0;
		scanf("%d %d", &a, &b);
		for(i=a; i<=b; i++)
		{
			if(map[i])	
			{
				cnt++;
			}
		}
		printf("Case #%d: %d\n", th++, cnt);
		
	}
	return 0;
}

