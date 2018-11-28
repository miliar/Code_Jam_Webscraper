#include<bits/stdc++.h>
using namespace std ;

#define LL long long int 


int main()
{
	ios::sync_with_stdio(0);
	int t;
	cin>>t;
	int test=1;

	while(test<t+1)
	{
		string str;
		cin>>str;

		
		char ch=str[0];
		int size1= str.size();

		if(size1==1 && str[0]=='-')
		{
			cout<<"Case #"<<test<<": "<<'1'<<endl;	
		}
		else
		{
			LL count=0;
			for(int i=1; i<size1 ; i++)
			{
				if(i == (size1-1))
				{
					if(str[i]=='-')
						count=count+1;
				}

				if(str[i] != ch)
				{
					count=count+1;
					ch=str[i];
				}
			}
			cout<<"Case #"<<test<<": "<<count<<endl;
		}

		test=test+1;
	}

return 0;

}