#include<iostream>
#include<string>
using namespace std;
int main()
{
	int tstcs,i,j,len,smax,a[10000],ctr,popu,diff;
	string	str;
	cin>>tstcs;
	for(i =1;i<=tstcs;i++)
	{
		cin>>smax;
		cin>>str;
		len = str.size();
		for(j=0;j<len;j++)
		{
			a[j] = str[j] -'0';
			
		}
		popu = 0;
		ctr = 0;
		for(j=0;j<len;j++)
		{
			if(popu >= j)
			{
				popu += a[j];
			}
			else
			{
				diff = j - popu;
				ctr  += diff;
				popu = j;
				popu += a[j];
			}
		}
		
		cout<<"Case #"<<i<<": "<<ctr<<endl;	
	}
	return 0;
}
