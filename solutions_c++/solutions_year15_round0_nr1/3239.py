#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
using namespace std;

int t;
int s;
char str[2000];

void init()
{
	memset(str, 0, sizeof(str));
}

int main()
{
	freopen("A.txt", "r", stdin);
	freopen("A1.txt", "w", stdout);
	cin>>t;
	for(int files=1 ; files<=t; files++)
	{
		init();
		cin>>s;
		cin>>str;
		
		int i;
		int sum=0;
		int ans=0;
		for(i=0;i<=s; i++)
		{
			int now = str[i] - '0';
			if(sum < i)
			{
				ans+= i-sum;
				sum=i;
			}
			sum += now;
		}
		printf("Case #%d: %d\n", files, ans);
	}
	//system("pause");
	return 0;
}





