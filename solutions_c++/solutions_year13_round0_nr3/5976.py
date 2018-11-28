#include <iostream>
#include <string>
#include <math.h>
using namespace std;
int main()
{
	int number,count,k,m,n,k2,m2,n2,num,num2;
	bool flag,flag2;
		string blank,str;
	cin>>number;
	double d_sqrt;
	unsigned long long a[number][2],i_sqrt;
	int s[15],s2[15];
	getline(cin,blank);
	for(int i=0;i<number;i++)
	{
		cin>>a[i][0];
		cin>>a[i][1];
		getline(cin,blank);
	}
	for(int i=0;i<number;i++)
	{
		count=0;
		for(unsigned long long j=a[i][0];j<=a[i][1];j++)
		{
			flag=true;
			k=0;
			d_sqrt=0;
			i_sqrt=0;
			d_sqrt=sqrt(j);
			i_sqrt=sqrt(j);
			if(d_sqrt==i_sqrt)
			{
				num = j;
				flag=true;
				while(num>0)
				{
					s[k]=num%10; 
					num = floor(num/10);		
					k++;
				}
				for(m=0,n=k-1;m<=n;m++,n--)
				{
					if(s[m]==s[n])
					{
						flag=true;
					}
					else
					{
						flag=false;
						break;
					}
				}
			}
			else
			{
				flag=false;
			}
			if(flag)
			{
				k2=0;
				num2=i_sqrt;
				
				while(num2>0)
				{
					s2[k2]=num2%10;
					num2=floor(num2/10);
					k2++;
				}
				for(m2=0,n2=k2-1;m2<=n2;m2++,n2--)
				{
					if(s2[m2]==s2[n2])
					{
						flag2=true;
					}
					else
					{
						flag2=false;
						break;
					}
				}
				if(flag2)
				{ 
					count++;
				}
				
			}
			
		}
		cout<<"Case #"<<i+1<<": "<<count<<"\n";
		
	}
	return 0;
}