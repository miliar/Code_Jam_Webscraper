#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	ofstream out;
	out.open("standout.txt");
int t,t1=1;
scanf("%d",&t);
while(t--)
{

	int n,i=-1,count=0;
	char str[1001];
	int a[1002];
	int a1[1002];
	scanf("%d",&n);
	scanf("%s",str);

	while(++i<=n)
		{
			a[i]=(int)(str[i]-'0');
			a1[i]=a[i];
		}
	i=-1;
	while(++i<n)
		a[i+1]+=a[i];
i=0;

			while(++i<=n)
			{	
				if(a1[i]>0)
				{
					if(a[i-1]>=i)
						a[i]=a[i-1]+a1[i];
					else
					{
						count+=i-a[i-1];
						a[i]+=i-a[i-1];
					}
				}
				else
				{
					a[i]=a[i-1];
				}
			}
			
	out<<"Case #"<<t1<<": "<<count<<endl;		
printf("Case #%d: %d\n",t1,count);
t1++;
}
return 0;
}