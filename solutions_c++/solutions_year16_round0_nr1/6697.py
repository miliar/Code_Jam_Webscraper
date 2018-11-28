#include<bits/stdc++.h>
#define sz 1000001
using namespace std;
int main()
{
	int t,n,i,f,j,k;
	set<int> s;
	cin>>t;
	j=1;
	while(t--)
	{
		cin>>n;
		i=1;
		while(i<101)
		{
			f=n*i;
			while(f>0)
			{
				s.insert(f%10);
				f/=10;
			}
			if(s.size()==10)
				break;
			i++;
		}
		cout<<"Case #"<<j++<<": ";
		if(i==101)
			cout<<"INSOMNIA"<<endl;
		else
			cout<<n*i<<endl;
		s.clear();
	}
	return 0;
}










