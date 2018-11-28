//gdjA counting sheep
#include <iostream>
#include <string.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("large.out","w",stdout);
	int Tcase,n,flag,temp;
	int count[10];
	cin>>Tcase;
	int i,j,k;
	for(i=0;i<Tcase;i++)
	{
		cin>>n;
		cout<<"Case #"<<i+1<<": ";
		if(!n)
			cout<<"INSOMNIA"<<endl;
		else
		{
			for(j=0;j<10;j++)
				count[j]=0;
			j=1;
			flag=0;
			while(flag<10)
			{
				temp=j*n;
				while(temp>0)
				{
					count[temp%10]++;
					temp/=10;
				}
				flag=0;
				for(k=0;k<10;k++)
				{
					if(count[k]!=0)
						flag++;
				}
				j++;
			}
			//flag已经到达10
			cout<<(j-1)*n<<endl;
		}

	}
	return 0;
}