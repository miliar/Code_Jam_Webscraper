#include <iostream>
using namespace std;

int main() {
	// your code goes here
	std::ios::sync_with_stdio(false);
	int t,n,i,count,stand,j,a;
	cin>>t;
	for(j=1;j<=t;j++)
	{
		int ar[1002]={0};
		cin>>n;
		string st;
		cin>>st;
		for(i=0;i<=n;i++)
		{
			
			a=st[i]-'0';
			ar[i]=a;
		}
		count=0;
		stand=0;
		for(i=0;i<=n;i++)
		{
			if(i==0)
			{
				if(ar[i]==0)
				{
					stand++;
					count++;
				//	cout<<i<<endl;
				}
				else
				{
					stand+=ar[0];
				}
			}
			else
			if(stand>=i)
			{
				stand+=ar[i];
			}
			else
			{
				stand++;
				stand+=ar[i];
				count++;
			//	cout<<i<<endl;
			}
		}
		cout<<"Case #"<<j<<":"<<" "<<count<<endl;;
	}
		
	return 0;
}
