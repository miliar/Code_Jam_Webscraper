#include<bits/stdc++.h>
using namespace std;

int main()
{
		int smax,i,ans,t,sum,j=0;
		cin>>t;
		while(t--)
		{

			j++;
			cin>>smax;
			ans=0,sum=0;
			string s;
			cin>>s;

				sum=sum+(s[0]-'0');
			for(i=1;i<=smax;i++)
			{

				if(sum>=i)
				{
					sum=sum+(s[i]-'0');
				}
				else
				{
					if((s[i]-'0')!=0)
					{
						ans=ans+(i-sum);
						sum=sum+i-sum+s[i]-'0';
					} 

				}



			}


				cout<<"Case #"<<j<<": "<<ans<<endl;


		}	

		return 0;




}