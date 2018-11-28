#include<stdio.h>
#include<string.h>
#include<math.h>
int a1[1001];
int reversDigits(int num)
{
   int rev_num = 0;
    while(num > 0)
    {
        rev_num = rev_num*10 + num%10;
        num = num/10;
    }
    return rev_num;
}
int isPalin(int num)
{
  int x=reversDigits(num);
  if(num==x)return 1;
  else return 0;
}
int isPerfectSquare(int num)
{
	int s=sqrt(num);
	if(s*s==num)return 1;
	else return 0;
	}
		
int main()
{
    //freopen("C-small-attempt2C-small-attempt2.in.in","r",stdin);
   //freopen("outd.txt","w",stdout);
	int t,a,b;
	memset(a1,0,1001);
	a1[1]=1;
	for(int i=2;i<1001;i++)
	{
		int k3;
		int k1=isPalin(i);
		if(k1==1)
		{
			int k2 = isPerfectSquare(i);
			if(k2==1)
			{
				k3=isPalin(sqrt(i));
				if(k3==1)
				a1[i]=1;
				else ;
			}
			}
		}
	scanf("%d",&t);
	int d=1;
	while(t--)
	{
		int c=0;
		scanf("%d%d",&a,&b);
		for(int i=a;i<=b;i++)
			{
				if(a1[i]==1)c++;
				}
				
		printf("Case #%d: %d\n",d,c);
		d++;
		}
	return 0;
	}
