#include<bits/stdc++.h>
using namespace std;
int result[1000010];
int a[10];

int ifallten()
{
	for (int i = 0; i < 10; ++i)
	{
		if(!a[i]) return 0;
	}
	return 1;
}

void split(int n)
{
	while(n)
	{
		a[n%10]++;
		n=n/10;
	}
}

int main()
{
    ifstream cin("A-large.in");
    ofstream cout("output.txt");
	int T;
	cin>>T;
	int n;
	for(int i = 1; i <= T; ++i)
	{
		memset(a,0,sizeof(a));
		cin>>n;
		int j, f=0;
		for (j = 1;j<987654321; ++j)
		{
		    if(n==0)
            {
                break;
            }
			split(j*n);
			if(ifallten())
            {
                f=1;break;
            }
		}
		int k=j*n;
		if(!f) cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		else cout<<"Case #"<<i<<": "<<k<<endl;
	}
	return 0;
}
