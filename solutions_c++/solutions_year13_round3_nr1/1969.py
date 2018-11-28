#include<iostream>
using namespace std;
int main()
{
	freopen("A-small-attempt0 (6).in","r",stdin);
	freopen("out1.in","w",stdout);
	int i,n,tempsum,sum,count,t,c;
	string l;
	cin>>t;
	c=1;
	while(t--)
	{
	cin>>l>>n;
	count=0;
	tempsum=0;
	sum=0;
	for(i=l.length()-1;i>=0;i--)
	{	
//	cout<<"i is "<<i<<" tempsum is "<<tempsum<<" sum is "<<sum<<" n  is "<<n<<" count is"<<count<<"sum "<<sum<<"l at i "<<l.at(i)<<endl;
		if(l.at(i)!='a'&&l.at(i)!='e'&&l.at(i)!='i'&&l.at(i)!='o'&&l.at(i)!='u')
		{
//		cout<<"inside if"<<endl;
		count++;if(count>=n)
		{
			tempsum=l.length()-i-n+1;
		}	
		}
		else count=0;
		sum=sum+tempsum;
		
	}
	cout<<"Case #"<<c++<<": "<<sum<<endl;
}
	
return 0;
}
