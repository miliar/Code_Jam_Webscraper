#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("in.txt","r", stdin);
	freopen("out.txt" , "w" , stdout);
	int t,i;
	cin>>t;
	set<int>s;
	for(i=1;i<=t;i++)
	{
		s.clear();
		long n;
		cin>>n;
		if(n==0)
	    printf("Case #%d: INSOMNIA\n",i);
		else
		{
		long long n2=n,j;
		for(j=1;;j++)
		{
			n2=n*j;
		    while(n2)
			{ 
				s.insert(n2%10);
				n2/=10;
			}
			if(s.size()==10)
			break;
		}
		printf("Case #%d: %d\n",i,n*j);
	    }
	}
	return 0;
}
