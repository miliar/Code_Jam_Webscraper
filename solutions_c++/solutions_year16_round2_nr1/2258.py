#include <bits/stdc++.h>
using namespace std;

#define FOR(i,j,n) for(i=j;i<n;i++)
#define si(i) scanf("%d",&i)
#define sli(i) scanf("%ld",&i)
#define slli(i) scanf("%lld",&i)
#define sc(i) scanf("%c",&i)
#define ss(i) scanf("%s",i);

#define pi(i) printf("%d\n",i)
#define pli(i) printf("%ld\n",i)
#define plli(i) printf("%lld\n",i)
#define pc(i) printf("%c\n",i)
#define ps(i) printf("%s\n",i);

typedef long long int lli;

void solve()
{
	//print the answer and nothing less or more. 
	string s;
	cin>>s;
	int count[26],i;
	FOR(i,0,26)
	{
		count[i]=0;
	}
	int len=s.size();
	FOR(i,0,len)
	{
		count[(int)s[i]-65]++;

	}
	
	int arr[10];
	
	arr[0]=count[(int)'Z' - 65];
	
	count[(int)'E' - 65]=count[(int)'E' - 65] - count[(int)'Z' - 65];
	count[(int)'R' - 65]=count[(int)'R' - 65] - count[(int)'Z' - 65];
	count[(int)'O' - 65]=count[(int)'O' - 65] - count[(int)'Z' - 65];
	count[(int)'Z' - 65]=count[(int)'Z' - 65] - count[(int)'Z' - 65];

	arr[2]=count[(int)'W' - 65];
	count[(int)'T' - 65]=count[(int)'T' - 65] - count[(int)'W' - 65];
	
	count[(int)'O' - 65]=count[(int)'O' - 65] - count[(int)'W' - 65];
	count[(int)'W' - 65]=count[(int)'W' - 65] - count[(int)'W' - 65];
	arr[8]=count[(int)'G' - 65];
	count[(int)'E' - 65]=count[(int)'E' - 65] - count[(int)'G' - 65];
	count[(int)'I' - 65]=count[(int)'I' - 65] - count[(int)'G' - 65];

	count[(int)'H' - 65]=count[(int)'H' - 65] - count[(int)'G' - 65];
	count[(int)'T' - 65]=count[(int)'T' - 65] - count[(int)'G' - 65];
	count[(int)'G' - 65]=count[(int)'G' - 65] - count[(int)'G' - 65];
	arr[6]=count[(int)'X' - 65];
	count[(int)'S' - 65]=count[(int)'S' - 65] - count[(int)'X' - 65];
	count[(int)'I' - 65]=count[(int)'I' - 65] - count[(int)'X' - 65];
	count[(int)'X' - 65]=count[(int)'X' - 65] - count[(int)'X' - 65];

	arr[7]=count[(int)'S' - 65];

	count[(int)'E' - 65]=count[(int)'E' - 65] - count[(int)'S' - 65];
	count[(int)'V' - 65]=count[(int)'V' - 65] - count[(int)'S' - 65];
	count[(int)'E' - 65]=count[(int)'E' - 65] - count[(int)'S' - 65];
	count[(int)'N' - 65]=count[(int)'N' - 65] - count[(int)'S' - 65];
	count[(int)'S' - 65]=count[(int)'S' - 65] - count[(int)'S' - 65];
	arr[5]=count[(int)'V' - 65];
	count[(int)'F' - 65]=count[(int)'F' - 65] - count[(int)'V' - 65];
	count[(int)'I' - 65]=count[(int)'I' - 65] - count[(int)'V' - 65];

	count[(int)'E' - 65]=count[(int)'E' - 65] - count[(int)'V' - 65];
	count[(int)'V' - 65]=count[(int)'V' - 65] - count[(int)'V' - 65];
	arr[3]=count[(int)'T' - 65];
	
	count[(int)'H' - 65]=count[(int)'H' - 65] - count[(int)'T' - 65];
	count[(int)'R' - 65]=count[(int)'R' - 65] - count[(int)'T' - 65];
	count[(int)'E' - 65]=count[(int)'E' - 65] - count[(int)'T' - 65];
	count[(int)'E' - 65]=count[(int)'E' - 65] - count[(int)'T' - 65];
	count[(int)'T' - 65]=count[(int)'T' - 65] - count[(int)'T' - 65];
	arr[4]=count[(int)'F' - 65];

	count[(int)'O' - 65]=count[(int)'O' - 65] - count[(int)'F' - 65];
	count[(int)'U' - 65]=count[(int)'U' - 65] - count[(int)'F' - 65];
	count[(int)'R' - 65]=count[(int)'R' - 65] - count[(int)'F' - 65];
	count[(int)'F' - 65]=count[(int)'F' - 65] - count[(int)'F' - 65];
	arr[1]=count[(int)'O' - 65];

	count[(int)'N' - 65]=count[(int)'N' - 65] - count[(int)'O' - 65];
	count[(int)'E' - 65]=count[(int)'E' - 65] - count[(int)'O' - 65];
	count[(int)'O' - 65]=count[(int)'O' - 65] - count[(int)'O' - 65];
	arr[9]=count[(int)'I' - 65];
	count[(int)'N' - 65]=count[(int)'N' - 65] - count[(int)'I' - 65];

	count[(int)'N' - 65]=count[(int)'N' - 65] - count[(int)'I' - 65];
	count[(int)'E' - 65]=count[(int)'E' - 65] - count[(int)'I' - 65];
		count[(int)'I' - 65]=count[(int)'I' - 65] - count[(int)'I' - 65];
	int j;
	
	FOR(i,0,10)
	{
		FOR(j,0,arr[i])
		{
			printf("%d",i);
		}
	}
	


		


}

int main()
{
	lli i,t;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cout<<"Case #"<<i<<": ";
		solve();
		cout<<endl; 	
	}
	   
    return 0;
}