#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
	int t,n,a,b,i,j;
	cin>>t;
	n=1;
	int fs[5] = {1,4,9,121,484};
	while(t--)
	{
		cin>>a>>b;
		if(a>484)
		{
			cout<<"Case #"<<n<<": 0"<<endl;
			n++;
			continue;
		}		
		for(i=0,j=4;i<5,j>=0;)
		{
			if(a>fs[i])
			{
				i++;
			}
			if(b<fs[j])
			{
				j--;
			}
			if((fs[i]>=a)&&(fs[j]<=b))
			{
				break;
			}
		}
		cout<<"Case #"<<n<<": "<<j-i+1<<endl;
		n++;
	}		
	return 0;	
}


