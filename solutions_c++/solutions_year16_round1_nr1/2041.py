#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("round21l.in","r",stdin);
	freopen("out21l.txt","w",stdout);
	int t,i=2,j=1,k=1;
	string s,q;
	cin>>t;
	while(k<=t)
	{
		cin>>s;
		q=s[0];
		while(i!=s.length()+1)
		{
			if(q[0]>s[j])
			{
				q.insert(q.end(),1,s[j]);
			}
			else
			{
				q.insert(0,1,s[j]);
			}
			j++;
			i++;
		}
		cout<<"Case #"<<k<<": "<<q<<endl;
		i=2;
		j=1;
		k++;
	}
	return 0;
}
