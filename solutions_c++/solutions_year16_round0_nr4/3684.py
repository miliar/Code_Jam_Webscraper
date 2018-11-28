#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t,k,c,s; int l=1;
	cin>>t;
   while(t--)
   {   cin>>k>>c>>s;
		if(c==1&& s<k)
		{
           cout<<"Case #"<<l++<<": IMPOSSIBLE"<<endl;
		}
		else if(c==1 && s==k)
		{
            cout<<"Case #"<<l++<<": ";
            for(int i=1;i<=k;i++)
            	cout<<i<<" ";
            cout<<endl;
		}
		else if(k==1)
		{
			cout<<"Case #"<<l++<<": 1"<<endl;
		}
		else
		{
			cout<<"Case #"<<l++<<": ";
			for(int i=0;i<k-1;i++)
			{
				cout<<k*i + i+2<<" ";
			}
			cout<<endl;
		}
   } 
}