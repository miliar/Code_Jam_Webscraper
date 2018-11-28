#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	
	for(int iii=0; iii<t; iii++)
	{
		int a[1002], count=0, sm, ans=0;
		char c;
		
		cin>>sm;
			
		for(int i=0; i<=sm; i++)
		{
			cin>>c;
			a[i]=(int)c-48;
		}
		
		for(int i=0; i<=sm; i++)
		{
			count+=a[i];
			if(i+1>count)
			{
				ans+=(i+1-count);
				count=i+1;
			}
		}
		cout<<"Case #"<<iii+1<<": "<<ans<<endl;	
	}
	return 0;
}
