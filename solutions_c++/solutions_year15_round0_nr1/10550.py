#include <iostream>
using namespace std;
const int size = 1005;
int main()
{
	freopen("D:\\test.txt","w",stdout);
	int t;
	int n;
	scanf("%d",&t);
	char str[size];
	int num;
	int sum;
	int i;
	int countnum = 0;
	while(t--)
	{
		sum = 0;
		scanf("%d",&n);
		scanf("%s",str);
		num = str[0]-'0';
		for(i=1;i<= n;i++)
		{
			if(str[i] != '0')
			{
				if(i-num>0)
				{
					sum+= i-num;
					num+= i-num;
				}
				num+= str[i]-'0';
			}
		}
		printf("Case #%d: %d\n",++countnum,sum);
	}
	return 0;
}