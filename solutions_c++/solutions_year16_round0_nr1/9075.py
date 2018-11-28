#include <bits/stdc++.h>
using namespace std;
int main()
{   int t,r=1;
	#ifndef ONLINE_JUDGE
	    freopen("prateek4.txt","r",stdin);
	    // freopen("output.txt","w",stdout);
	  #endif
	cin>>t;
	while(t--)
	{
		int n,p,q,f;
		cin >> n;
		if(n==0)
			{
				cout<<"Case #"<< r <<": "<< "INSOMNIA" <<endl;
				r++;
				continue;
			}
		int check[10]={0};
		int flag=0;
		for (int i = 1; flag==0 ; i++)
		{
			//cout << "hi" << endl;
			flag=1;
			//n*=i;
			p=n*i;
			f=p;
			while(p>0)
			{
				//cout << "ti" ;
				q=p%10;
			//	cout << q << " " ;
				if(check[q]==0)
				{
					check[q]=1;
				}
				p/=10;
			}
			for (int j = 0; j < 10 ; j++)
			{
				//cout << "ki";
				if(check[j]==0)
				{
					//cout << "li";
					flag=0;
				}
			}
			//cout << flag;
		}
		if(flag==1)
		{
			cout<<"Case #"<< r <<": "<< f <<endl;
		}
		r++;
	}
	return 0;
}