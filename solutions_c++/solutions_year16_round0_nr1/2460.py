#include<bits/stdc++.h>
using namespace std;

bool chk[10];

bool store(long long n)
{
	bool flag=0;
	while(n>0)
	{
		//cout<<" "<<n%10<<endl;
		chk[n%10]=1;
		n/=10;
	}
	for(int i=0; i<10; i++)
	{
		if(!chk[i]) {
			flag=1;
			break;
		}
	}
	if(flag) return 1;
	else return 0;
}

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	freopen("C:/Users/HP/Desktop/CodeJam/codejam1_large_input.txt","r",stdin);//redirects standard input
	freopen("C:/Users/HP/Desktop/CodeJam/codejam1_large_output.txt","w",stdout);//redirects standard output
	int t;
	long long n;
	cin>>t;
	for(int tc=1; tc<=t; tc++)
	{
		for(int i=0; i<10; i++)
		{
			chk[i]=0;
		}
		
		cin>>n;
		if(n==0) {
			cout<<"Case #"<<tc<<": INSOMNIA"<<endl;
			continue;
		}
		for(long long i=1; ;i++)
		{
			//cout<<" "<<n*i<<endl;
			if(!store(n*i)) {
				cout<<"Case #"<<tc<<": "<<n*i<<endl;
				break;
			}
		}
	}
	return 0;
}
