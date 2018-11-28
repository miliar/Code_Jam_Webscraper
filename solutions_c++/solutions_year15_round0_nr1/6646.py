#include <iostream>
using namespace std;
 
int main() {
	int t,a,i,count,cf,count1,x=1;
	cin>>t;
	while(t--)
	{
		count=0;
		cin>>a;
		int b[a+1];
		char c[a+1];
		for(i=0;i<=a;i++)
		{
			cin>>c[i];
			b[i]=c[i]-'0';
		}
		cf=b[0];
		
		for(i=1;i<=a;i++)
		{
			count1=0;
			if(b[i]!=0)
			{
			if(cf<i)
				count1=i-cf;
			count+=count1;
			cf+=b[i]+count1;
			}
			
		}
		cout<<"Case #"<<x<<": "<<count<<"\n";
		x++;
	}
}
	
