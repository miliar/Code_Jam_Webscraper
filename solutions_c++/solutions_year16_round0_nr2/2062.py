#include <bits/stdc++.h>
#define ll long long int
#define MAX 105
#define MOD 1e9+7
#define vint vector <int>
#define vpint vector <pair<int,int> >
#define pb push_back
using namespace std;

char str[MAX];

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

int value(char ch)
{
	if(ch=='-')
		return 0;
	if(ch=='+')
		return 1;
}

int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>str;
		int len=strlen(str);
		int j=0;
		int flag=value(str[0]);
		int ans=0;
		for(j=0;j<len;j++)
		{
			if(flag!=value(str[j]))
			{
				ans++;
				flag=value(str[j]);
			}
		}
		if(str[len-1]=='-')
			ans++;
		cout<<"Case #"<<i<<": "<<ans<<"\n";
	}
	return 0;
}