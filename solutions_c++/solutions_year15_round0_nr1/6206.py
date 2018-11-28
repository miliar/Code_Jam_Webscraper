#include <bits/stdc++.h>
using namespace std;

int main() {
	int t,a,b,c;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	string abc;
	for(a=1;a<=t;a++)
	{
		cin>>b;
		cin>>abc;
		long long sum,count;
		sum=0;count=0;
		for(c=1;c<=b;c++)
		{
			sum+=(long long)(abc[c-1]-'0');
			//cout<<sum<<endl;
			if(sum>=c)
			continue;
			else
			{
				count++;
				sum++;
			}

		}

		cout<<"Case #"<<a<<": "<<count<<endl;
	}
	return 0;
}
