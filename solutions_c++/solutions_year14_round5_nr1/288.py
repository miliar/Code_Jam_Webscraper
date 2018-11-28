#include <stdio.h>

long long a[1000100];
double ssss[1000100];
int main(void)
{
	int t ,i;
	int n ,p ,q ,r ,s;
	long long pp ,qq ,rr ,ss ,j;
	double ans;
	double min ,max ,temp;
	double ans1 ,ans2 ,ans3 ,ans4 ,ans5;
	int p1 ,p2 ,p12;
	
	scanf("%d" ,&t);
	for (i=1 ; i<=t ; i++)
	{
		scanf("%d %d %d %d %d" ,&n ,&p ,&q ,&r ,&s);
		pp=p;
		qq=q;
		rr=r;
		ss=s;
		ssss[0]=0;
		for (j=1 ; j<=n ; j++)
		{
			a[j]=(((j-1)*pp+qq)%rr)+ss;
			ssss[j]=ssss[j-1]+a[j];
		}
		if (n==1)
		{
			ans=0;
		}
		else if (n==2)
		{
			if (a[2]>a[1])
			{
				min=a[1];
			}
			else
			{
				min=a[2];
			}
			ans=min/ssss[2];
		}
		else
		{
			ans=0;
			for (j=2 ; j<n ; j++)			
			{
				p1=j+1;
				p2=n;
				while (p1!=p2)
				{
					p12=(p1+p2)/2;
					ans2=ssss[p12-1]-ssss[j-1];
					ans3=ssss[n]-ssss[p12-1];					
					if (ans2<ans3)
					{
						ans4=ssss[p12]-ssss[j-1];
						ans5=ssss[n]-ssss[p12];		
						if (ans4<=ans5)
						{
							p1=p12+1;		
						}
						else
						{
							if (ans2<ans5)	
							{
								p1=p12+1;
							}
							else
							{
								p2=p12;
							}
						}											
					}
					else
					{
						p2=p12;	
					}
				}
				ans1=ssss[j-1];
				ans2=ssss[p1-1]-ssss[j-1];
				ans3=ssss[n]-ssss[p1-1];
				if (ans1<ans2)
				{
					max=ans2;
				}
				else
				{
					max=ans1;
				}
				if (ans3>max)
				{
					max=ans3;	
				}
				max/=ssss[n];
				temp=1-max;
				if (temp>ans)
				{
					ans=temp;	
				}				
			}
		}
		printf("Case #%d: %.10f\n" ,i ,ans);
	}

	return 0;
}
