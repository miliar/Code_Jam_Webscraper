#include <bits/stdc++.h>
using namespace std;
int T;
long long N;
int A[10];
void get(long long s)
{
	long long q,dig;
	while(s>0)
	{
		q=s/10;
		dig=s%10;
		A[dig]=1;
		s=q;
	}
}
int main()
{
	//ifstream cin("A-large.in");
	//ofstream cout("A.out");
	cin>>T;
	for(int cases=1; cases<=T; cases++)
	{
		cin>>N;
		if(N==0){
			cout<<"Case #"<<cases<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		for(int i=0; i<10; i++)
		A[i]=0;
		int curr=1;
		long long ans=0;
		while(true)
		{
			get(curr*N);
			int flag=0;
			for(int i=0; i<10; i++)
			{
				if(A[i]==0){
					flag=1;
					break;
				}
			}
			if(flag==0)
			{
				ans=curr*N;
				break;
			}
			curr++;
		}
		cout<<"Case #"<<cases<<": "<<ans<<endl;
	}
	return 0;
}
