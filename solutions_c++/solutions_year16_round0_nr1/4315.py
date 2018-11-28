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
void fill_dig(set<lli>& myset, lli num)
{
	lli n=num,dig;
	while(n!=0)
	{
		dig=n%10;
		myset.insert(dig);
		n=n/10;
	}
}

void solve()
{
	//print the answer and nothing less or more.
	set<lli> myset;
	lli i,n; 
	slli(n);
	bool flag=0;
	lli num,save;
	FOR(i,1,100)
	{
		num=i*n;
		fill_dig(myset,num);
		if(myset.size()==10)
		{
			save=num;
			flag=1;
			break;
		}
	}
	if(flag==1)
	{
		printf("%lld",save);
	}
	else
	{
		printf("INSOMNIA");
	}
}

int main()
{
	lli i,t;
	slli(t);
	for(i=1;i<=t;i++)
	{
		cout<<"Case #"<<i<<": ";
		solve();
		cout<<endl; 	
	}
	   
    return 0;
}