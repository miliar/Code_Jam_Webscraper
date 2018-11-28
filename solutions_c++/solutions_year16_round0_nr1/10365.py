#include<bits/stdc++.h>
using namespace std;

int main() {
    FILE *fin = freopen("A-small.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-small.out", "w", stdout);
	long long int t,j,x,k;
	int a[10];
	cin>>t;
	for( k = 1; k <= t; k++)

	{
		long long int n,i=1,tmp;
		cin>>n;
		if(n==0)
		cout << "Case #" << k << ": "<<"INSOMNIA"<<endl;

		else
		{
		    memset(a,0,sizeof(a));
			while(1)
			{
				tmp=n*i;
				while(tmp>0)
				{
					x=tmp%10;
					a[x]++;
					tmp/=10;
				}
				for(j=0;j<10;j++)
				if(a[j]==0)
				break;
				if(j==10)
				break;
				i++;
			}
			cout << "Case #" << k << ": "<<n*i<<endl;

		}
	}
	return 0;
}
