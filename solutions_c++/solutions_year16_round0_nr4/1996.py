#include <bits/stdc++.h>
#define ll long long int
#define MAX 1000000
#define MOD 1e9+7
#define vint vector <int>
#define vpint vector <pair<int,int> >
#define pb push_back
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

int main()																						
{
	ios::sync_with_stdio(false);
	int t,i;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		ll k,c,s,j;
		cin>>k>>c>>s;
		cout<<"Case #"<<i<<": ";
		if(c==1)
		{
			if(s<k)
				cout<<"IMPOSSIBLE\n";
			else
			{
				for(j=1;j<=k;j++)
				{
					cout<<j<<" ";
				}
				cout<<"\n";
			}
		}
		else
		{
			ll pos,f,l;
			ll rep=(k%c==0?k/c:k/c+1);
			if(s<rep)
				cout<<"IMPOSSIBLE\n";
			else
			{
				for(j=1;j<=rep;j++)
				{
					pos=1;
					if(j!=rep)
					{
						for(l=1;l<=c;l++)
						{
							f=c*(j-1)+l;
							pos=(pos-1)*k+f;	
						}
						cout<<pos<<" ";
					}
					else
					{
						for(l=1;l<=c;l++)
						{
							f=c*(j-1)+l;
							f=(f<=k?f:k);
							pos=(pos-1)*k+f;	
						}
						cout<<pos<<" ";	
					}
				}
				cout<<"\n";
			}
		}
	}
	return 0;
}

/*
pos=1;
pos=(pos-1)*k+2;
pos=(pos-1)*k+3;
pos=(pos-1)*k+4;

pos=5;
pos=(pos-1)*k+6;
pos=(pos-1)*k+7;
pos=(pos-1)*k+8;

pos=9;
pos=(pos-1)*k+9;
pos=(pos-1)*k+9;
pos=(pos-1)*k+9;
*/