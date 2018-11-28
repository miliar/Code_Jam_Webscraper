#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);
	int t;
	cin>>t;
	int j;
     for(j=0;j<t;j++)
	{
		int n;
		cin>>n;
		char a[n+1];
		cin>>a;
		long long int count=0,i, sum=0;
		for(i=0;i<strlen(a);i++)
		{
		   
		
			
			if(a[i]=='1')
			sum=sum+1;
			 if(a[i]=='2')
			sum=sum+2;
		    if(a[i]=='3')
			sum=sum+3;
			if(a[i]=='4')
			sum=sum+4;
			if(a[i]=='5')
			sum=sum+5;
			if(a[i]=='6')
			sum=sum+6;
			if(a[i]=='7')
			sum=sum+7;
			if(a[i]=='8')
			sum=sum+8;
		    if(a[i]=='9')
			sum=sum+9;
			
			
			//cout<<sum<<endl;
			if(sum<=i)
		    {
		     count++;
		     sum++;
		    }
		}
		
		cout<<"Case #"<<j+1<<": "<<count<<endl;
	}
}
