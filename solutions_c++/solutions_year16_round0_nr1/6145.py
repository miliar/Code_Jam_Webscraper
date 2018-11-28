#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
using namespace std ;
map<int,bool>mp1;
void Mark(int x)
{
	while(x)
	{
		mp1[x%10]=1;
		x/=10;
	}
}
bool Check()
{
	for(int i=0 ; i < 10 ; i++)
	{
		if(!mp1[i])
			return 0;
	}
	return 1;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	cin >> n;
	for(int i=1 ; i <= n ; i++)
	{
		mp1.clear();
		long long x;
		cin >> x;
		printf("Case #%d: ",i);
		if(x==0)
			printf("INSOMNIA");
		else
		{
			long long tmp=1,x2=x;
			while(!Check())
			{
				x2=x*tmp;
				Mark(x2);
				tmp++;
			}
			cout << x2;
		}
		printf("\n");
	}
}
