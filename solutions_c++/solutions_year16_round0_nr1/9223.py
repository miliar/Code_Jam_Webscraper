#include<bits/stdc++.h>
using namespace std;
bool arr[10];
typedef long long int ll;
bool check(ll N)
{
	ll k,l;
	
	while(N!=0)
	{
		int i;
		i=N%10;
		//printf("%d  shakhsi",N );
		N/=10;
		if(!arr[i])
			arr[i]=true;
	}
	bool raj=true;
	for(int i=0;i<10;++i)
	{
		if(!arr[i])
			raj = false;
	}
	return raj;
}
void solve(int K)
{
	int N;
	ll temp;
	printf("Case #%d: ",K);
	memset(arr,false,sizeof(arr));
	scanf("%lld",&N);
	if(N==0)
		printf("INSOMNIA\n");
	else
	for(ll i=1;;++i)
	{
		temp = i*N;
		//printf("%d  SOnveer",temp );
		bool raj=check(temp);
		if(raj)
		{
			printf("%lld\n",temp);
			break;
		}	
	}
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;++i)
		solve(i);
	return 0;
}