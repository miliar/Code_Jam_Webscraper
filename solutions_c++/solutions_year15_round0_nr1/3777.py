#include<bits/stdc++.h>

using namespace std;
char strings[1000010];





int main()


{
    freopen("ques.txt","r",stdin);
    freopen("ans2.txt","w",stdout);


	int k;
	int t;
	cin>>t;
	int request=0;
	int clapping=0;
	int cs=0;

	while(t--)
	{
		cs++;
		request=0;
		clapping=0;
		cin>>k;
		cin>>strings;
		clapping+=strings[0]-'0';

		for(int j=1;j<=k;j++)
		  {
			 if(clapping>=j)
			{
				clapping+=(strings[j]-'0');

			}
			else
			{
				if(strings[j]-'0'>0)
				{
				request+=(j-clapping);
				clapping=clapping+(j-clapping)+(strings[j]-'0');
			    }
			}
		}
	   cout<<"Case #"<<cs<<": "<<request<<endl;
	}
	return 0;
}
