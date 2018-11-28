    //https://code.google.com/codejam/contest/2974486/dashboard#s=p3
    #include <iostream>
    #include<algorithm>
    
    
    using namespace std;
    
    int main() {
    int t,i;
    scanf("%d",&t);
    for(i=0;i<t;i++)
	{
		int j,SIZE;
		scanf("%d",&SIZE);
		
		double a1[SIZE],b1[SIZE],a2[SIZE],b2[SIZE];
		int ans1=0, ans2=0,ans3=0,m,n;
		for(j=0;j<SIZE;j++)
		{
		scanf("%lf",&a1[j]);
		a2[j]=a1[j];
		}
		for(j=0;j<SIZE;j++)
		{
		scanf("%lf",&b1[j]);
		b2[j]=b1[j];
		}
		sort(a1, a1 + SIZE);
		sort(a2, a2 + SIZE);
		sort(b1, b1 + SIZE);
		sort(b2, b2 + SIZE);
		for(m=SIZE-1;m>=0;m--)
		{
			for(n=0;n<SIZE;n++)
			{
				if(a1[n]>b1[m])
				{
					a1[n]=0.0;
					ans1++;
					break;
				}
			}
		}
		for(m=0;m<SIZE;m++)
		{
			for(n=0;n<SIZE;n++)
			{
				if(a2[m]<b2[n])
				{
					b2[n]=0.0;
					ans3++;
					break;
				}
			}
		}
		ans2=SIZE - ans3;
		printf("Case #%d: %d %d\n",i+1,ans1,ans2);
	}
    return 0;
    }