#include<iostream>
#include<cmath>
#include<algorithm>
#include<cstring>
#include<vector>
#include<numeric>

using namespace std;

int main()
{
	int n, t;
	char name[101];
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		cin>>name>>n;
		int count = 0;
		int ans=0, init=-1;
		for(int i=0;name[i+n-1]!='\0';i++)
		{
			int flag = 0;
			for(int j=0;j<n;j++)
			{
				if(name[i+j]=='a'||name[i+j]=='e'||name[i+j]=='i'||name[i+j]=='o'||name[i+j]=='u')
				{
					//cout<<"katta "<<i<<" "<<j<<" ";
					flag = 1;
					break;
				}
			}
			if(flag == 0)
			{
				//count++;
				//ans += strlen(name)-i-n+1;
				ans = ans + (i-init)*(strlen(name)-i-n+1);
				init=i;
			}
			
		}
		/*
		int ln = strlen(name)-n+1;
		int ans=0;
			while(count--)
			{
				ans += ln;
				ln--;
			}*/
			cout<<"Case #"<<k<<": "<<ans<<endl;
	}
	return 0;
}
