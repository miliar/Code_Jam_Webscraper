#include <bits/stdc++.h>
#include <fstream>
using namespace std;

bool check[10];

int f(long long n);
bool chk();
void init();

int main()
{
	ifstream inf;
	ofstream out;
	inf.open("A-large.in");
	out.open("A-large.out");

    int t;
    // cin>>t;
    inf>>t;
    for(int i=1;i<=t;i++)
    {
    	init();
    	long long n,j;
    	// cin>>n;
    	inf>>n;
    	for(j=1;j<=1000000;j++)
    	{
    		f(n*j);
    		if(chk())
    		{
    			// printf("Case #%d: %d\n",i,n*j);
    			out<<"Case #"<<i<<": "<<n*j<<endl;
    			break;
    		}
    	}
    	if(j==1000001)
    	{
    		out<<"Case #"<<i<<": INSOMNIA"<<endl;
    		// printf("Case #%d: INSOMNIA\n",i);
    	}
    }
}

int f(long long n)
{
	while(n)
	{
		check[n%10]=true;
		n=n/10;
	}
}

bool chk()
{
	for(int i=0;i<10;i++)
	{
		if(!check[i]) return false;
	}
	return true;
}

void init()
{
	for(int i=0;i<10;i++) check[i]=false;
}