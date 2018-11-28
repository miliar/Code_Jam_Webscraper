#include <bits/stdc++.h>
#define ll long long int
#define MAX 1000000
#define MOD 1e9+7
#define vint vector <int>
#define vpint vector <pair<int,int> >
#define pb push_back
using namespace std;

ll hash[10];

void scanint(int &number)
{
    bool negative = false;
    register int c;
    number = 0;
    c = getchar();
    if (c=='-')
    {
        negative = true;
        c = getchar();
    }
    for (; (c>47 && c<58); c=getchar())
        number = number *10 + c - 48;

    if (negative)
        number *= -1;
}

void break_up(ll n)
{
	while(n)
	{
		int temp=n%10;
		n=n/10;
		hash[temp]++;
	}
}

bool check(ll n,ll j)
{
	int i;
	break_up(n*j);
	for(i=0;i<10;i++)
	{
		if(hash[i]==0)
			return 1;
	}
	return 0;
}

void clear()
{
	int i;
	for(i=0;i<10;i++)
		hash[i]=0;
}

int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		ll n,j;
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<i<<": INSOMNIA\n";
		}
		else
		{
			for(j=1;check(n,j);j++)
			{

			}
			n=n*j;
			cout<<"Case #"<<i<<": "<<n<<"\n";
			clear();
		}
	}
	return 0;
}