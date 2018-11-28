#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	int caseno=0;
	while(t--){
		caseno++;
		long long n,temp,ans;
		cin>>n;
		int c[11]={};
		int k=0,f=0;
		for(int i=1;i<10000;i++)
		{
			temp = n*i;
			ans=temp;
			while(temp){
				if(c[temp%10]==0)
				{
					c[temp%10]=1;
					k++;
				}
				temp/=10;
			}
			if(k==10)
			{
				f=1;
				break;
			}
				
		}
		if (f==1)
		{
			cout<<"Case #"<<caseno<<": "<<ans<<endl;
		}
		else
		{
			cout<<"Case #"<<caseno<<": INSOMNIA"<<endl;
		}
	}
	
	return 0;
}
