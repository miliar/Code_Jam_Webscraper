#include <iostream> 
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
using namespace std;
char str[10000000];int m; 
bool yuanyin(char zz)
{
	if(zz=='a'||zz=='e'||zz=='i'||zz=='o'||zz=='u')
		return 1;
	else
		return 0;
}

int main()
{
	int num,i;
	freopen("1.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>num;
	gets(str);
	for(i=0;i<num;i++)
	{
		scanf("%s %d",&str,&m);
		int l=0,n=0,ans=0;
		for(int i=0;i<strlen(str);i++)
		{
			if(yuanyin(str[i]))
			{
				ans = ans + l;
				n=0;
			}
			else
			{
				n++;
				if(n<m)
				{
					ans = ans + l;
				}
				else
				{
					ans = ans + i + 1 - m + 1;
					l = i + 1 - m + 1;
				}
			}
		}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	
}
