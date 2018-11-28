#include <bits/stdc++.h>
#define ll long long int
#define MAX 10005
#define MOD 1000000007
#define vint vector <int>
#define vpint vector <pair<int,int> >
#define pb push_back
#define ms(x,v) memset(x,v,sizeof x)
#define pr_arr(i,x,size) for(i=0;i<size;i++) cout<<x[i]<<" "
#define ff(i,a,b) for(i=a;i<=b;i++)
#define fb(i,a,b) for(i=a;i>=b;i--)
#define gprint(i) cout<<"Case #"<<i<<": "
using namespace std;

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

long long power(long long base,long long p)
{
    long long temp=1;
    while(p>1)
    {
        if(p%2!=0)
            temp=(1LL*(base*temp)%MOD);
        base=(1LL*(base*base)%MOD);
        p/=2;
    }
    long long ans=(1LL*(base*temp)%MOD);
    return ans;
}

int main()
{
	ios::sync_with_stdio(false);
	int t,i;
	cin>>t;
	ff(i,1,t)
	{
		vector <char> S;
		char str[MAX];
		int j;
		cin>>str;
		int len=strlen(str);
		ff(j,0,len-1)
		{
			if(j==0)
				S.pb(str[j]);
			else
			{
				if(str[j]<S.front())
					S.pb(str[j]);
				else
				{
					vector <char> :: iterator it;
					it=S.begin();
					S.insert( it , str[j] );
				}
			}
		}
		gprint(i);
		vector <char> :: iterator it;
		for(it=S.begin();it!=S.end();it++)
		{
			cout<<*it;
		}
		cout<<"\n";
	}
	return 0;
}