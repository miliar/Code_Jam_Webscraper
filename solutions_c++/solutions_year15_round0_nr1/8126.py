#include<cstdio>
#include<iostream>
#include<string>
#define gc getchar_unlocked
using namespace std;
int read_int()
{
	char ch;
	ch=gc();
	while(ch<'0'||ch>'9') ch=gc();
	int ret=0;
	while(ch>='0'&& ch<='9')
	{
		ret=ret*10+ch-48;
		ch=gc();
	}
	return ret;
} 
int main()
{
	int t,s,cnt,no,i,test=1,nop;
	//string str;
	t=read_int();
	while(t--)
	{
		i=0;
		cnt=0;
		nop=0;
		s=read_int();
		s++;
		char str[s+1];
		scanf("%s",str);	
		while(s--)
		{
			cnt+=((int)str[i]-48);
			if(cnt<=i)
			{
				nop++;
				cnt+=1;
			}
			i++;
		}
		printf("Case #%d: %d\n",test,nop);
		test++;	
	}
	return 0;
}
