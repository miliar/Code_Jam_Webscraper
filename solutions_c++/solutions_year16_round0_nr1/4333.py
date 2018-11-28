#include<bits/stdc++.h>
using namespace std ;

#define LL long long int 

int main()
{
	ios::sync_with_stdio(0);
	int t;
	cin>>t;
	int test=1;

	while(test < t+1)
	{
		LL input;
		LL ans;
		cin>>input;
		if(input==0)
		{
			cout<<"Case #1"<<": "<<"INSOMNIA"<<endl;
		}
		else
		{
				bool count[10];
				for(int i=0;i<10;i++)
					count[i]=false;

				
				bool flag=false;
				LL val;
				int check=0;// to check the how many has set true;
			

				LL i=1;
				while(check<10)
				{
					val=i*input;
					ans=val;
					while(val>0)
					{
						int index=val%10;
						if( count[index] == false )
						{
							count[index]=true;
							check=check+1;
							//cout<<"check="<<check<<endl;
						}
						val=val/10;
					}

					if(check==10)
					{
						flag==true;
					}

					i++;
					//cout<<"test"<<endl;

				}
				cout<<"Case #"<<test<<": "<<ans<<endl;
			}

		test=test+1;

	}

return 0;

}