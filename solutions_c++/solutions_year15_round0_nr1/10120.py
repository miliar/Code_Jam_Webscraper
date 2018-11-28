#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int ind=1;ind<=t;ind++)
	{
		int n,count=0;
		string s;
		cin>>n>>s;
		//cout<<n<<" "<<s<<endl;
		if(n==0)
			printf("Case #%d: 0\n",ind);
		else
		{
			int sum=(int)(s[0]-'0');
			for(int i=1;i<s.size();i++)
			{
				//cout<<sum<<endl;
				if(i>sum)
				{
					count+=i-sum;
					sum+=i-sum;
				}
				sum+=(int)(s[i]-'0');
			}
			printf("Case #%d: %d\n",ind,count);
		}
		
	}
	return 0;
}
