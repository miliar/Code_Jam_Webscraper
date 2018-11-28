#include<bits/stdc++.h>
using namespace std;
#define mem(arr,x) memset(arr,x,sizeof(arr))

typedef long long LL;

main() {
	FILE *fin = freopen("A-small.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-small.out", "w", stdout);
	int t,n;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cin>>n;
		if(n==0){
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;

		}
		else{
		int count=0,hash[11],now=1,number=n,temp,ans;
		mem(hash,0);

		while(count<10){
			number=now*n;
			ans=number;

			while(number>0){
				temp=number%10;
				if(hash[temp]!=1){
					count++;
					hash[temp]=1;
				}
				number/=10;
			}

			now++;
		}

		cout<<"Case #"<<i<<": "<<ans<<endl;
	}

	}

	exit(0);
}