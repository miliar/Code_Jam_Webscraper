#include<iostream>
using namespace std;
int main()
{
	int a[4],b[4];
	int fir,sec,test,i,j,waste,count,ans,c;
	scanf("%d",&test);
	c=1;
	while(test--)
	{
		count=0;
		scanf("%d",&fir);
		for(i=0;i<4;i++)
		{
				if((i+1)==fir)
				scanf("%d %d %d %d",&a[0],&a[1],&a[2],&a[3]);
				else
				scanf("%d %d %d %d",&waste,&waste,&waste,&waste);
		}
		scanf("%d",&sec);
		for(i=0;i<4;i++)
		{
			if((i+1)==sec)
				scanf("%d %d %d %d",&b[0],&b[1],&b[2],&b[3]);
				else
				scanf("%d %d %d %d",&waste,&waste,&waste,&waste);
		}
		printf("%d %d %d %d\n",a[0],a[1],a[2],a[3]);
		printf("%d %d %d %d\n",b[0],b[1],b[2],b[3]);
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		if(a[i]==b[j])
		{
		ans=a[i];
		count++;
		}
		
		if(count==0)
		printf("Case #%d: Volunteer cheated!\n",c++);
		else if(count==1)
		printf("Case #%d: %d\n",c++,ans);
		else
		printf("Case #%d: Bad magician!\n",c++);
	}
	return 0;
}