#include <stdio.h>
#include <math.h>
#include <vector>
using namespace std;
int arr[16];
vector <long long int> t;
int check(long long int n)
{
	long long int i;
	if (n==2)
	        return 1;

	if (n%2==0)
	{
		t.push_back(2);
		return 0;
	}
        for (i=3;i<=sqrt(n);i+=2)
	{
		if (n%i==0)
		{
			t.push_back(i);
			return 0;
		}
	}
	return 1;
}
int main()
{
	int a;
	scanf("%d%d%d",&a,&a,&a);
	long long int k,power,i,num,j = 15,count = 0;
	printf("Case #1:\n");
	for(i=32769;i<=65535;i+=2)
	{
		num = i;
		j = 15;
		while(num!=0)
		{
			arr[j] = num%2;
			num/=2;
			j--;
		}
		t.clear();
		int flag = 1;
		for(j=2;j<=10;j++)
		{
			num = 0;
			power = 1;
			for(k=0;k<=15;k++)
			{
				num += arr[k]*power;
				power *= j;
			}
			if(check(num) == 1)
			{
				flag = 0;
				break;
			}
			
		}
		if(flag == 1)
		{
			for(k=15;k>=0;k--)
				printf("%d",arr[k]);
			printf(" ");
			for(k=0;k<t.size()-1;k++)
				printf("%lld ",t[k]);
			printf("%lld\n",t[k]);
			count ++;
		}
		if(count == 50)
			break;
	}
	return 0;
}
