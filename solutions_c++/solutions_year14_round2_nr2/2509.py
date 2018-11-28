#include<iostream>
using namespace std;
int main()
{
	long int t,a,b,k;
	long int c,ans;
	cin>>t;
	for(int i = 0;i<t;i++)
	{
		ans = 0;
		cin>>a>>b>>k;
		for(int  j =0;j<a;j++)
		{
			for(int l = 0;l<b;l++)
			{
				c = l & j;
				if(c<k)
					ans++;
			}
		}
	
		cout << "Case #" << i+1 << ": "<<ans  <<endl;
		
	}
return 0;
}
