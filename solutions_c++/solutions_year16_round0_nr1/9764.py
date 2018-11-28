#include<stdio.h>
using namespace std;
bool check(int a[])
{
	int i;
	for(i=0;i<=9;i++)
	{
		if(a[i]==0)
			return false;
	}
	return true;
}
int main()
{
	int t,n,a[10]={0};
	scanf("%d",&t);
int l;
for(l=1;l<=t;l++)
	
	{
		scanf("%d",&n);
		//cin>>n;
	//	printf("enter aim\n");
			int i,k;
		for(i=0;i<=9;i++)
		{
			a[i]=0;
		}
		{
		
			for(i=1;;i++)
			{
			//	cout<<"i value is : "<<i<<endl;
		//	printf("%d dv\n",i);
				int x=i*n;
				if(x==0)
				{
					printf("Case #%d: INSOMNIA\n",l);
					break;
				}
				else
				{
					k=-1;
				while(x>0)
				{
			//		cout<<x<<"   aj"<<endl;
					int l=x%10;
					x=x/10;
					if(a[l]==0)
						a[l]=1;
				}
				bool b=check(a);
				if(b==true)
					break;}	
			}
	if(k==-1)	
printf("Case #%d: %d\n",l,i*n);	
//	cout<<i<<endl;
		}
	}
}
