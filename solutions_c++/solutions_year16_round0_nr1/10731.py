#include <iostream>
using namespace std;
bool ischeck(int n,int c[],int l)
{
	while(n!=0)
	{
		int r=n%10;
		c[r]++;
		n=n/10;
		
	}
	
	for(int i=0;i<10;i++)
	{
		if(c[i]==0)
		{
			return false;
		}
		
	}
	
	return true;
}	
int main() {
	int t;
	cin>>t;
	for(int z=0;z<t;z++)
	{
	
		long long n;
		cin>>n;
		//cout<<n;
		int c[10]={0};
		bool falg=false;
		for(int i=2;i<=10000000;i++)
		{
			if(ischeck(n,c,10))
			{
				cout<<"Case "<<"#"<<z+1<<":"<<" "<<n<<endl;
				falg=true;
				break;
			}
			else
			{
				int t=n*i;
				if(ischeck(t,c,10))
				{
					cout<<"Case "<<"#"<<z+1<<":"<<" "<<t<<endl;
					falg=true;
					break;
				}
			}
		}
		if(falg==false)
		cout<<"Case "<<"#"<<z+1<<":"<<" "<<"INSOMNIA"<<endl;
	}
	return 0;
}