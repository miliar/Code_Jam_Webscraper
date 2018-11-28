#include<bits/stdc++.h>
#define ll long long
#define MAXI 2000007
#define MOD 1000000007
using namespace std;

int n,a[MAXI],var;
int check()
{
	int i,cnt=0;
	for(i=0;i<n;i++)
	{
		if(a[i] > 1)
			return 1;
		if(a[i] == 1)
			cnt++;
	}
	if(cnt > 2)
		return 2;

	return 0;
}

int calcmaxpos()
{
	int maxi = 0,maxpos = -1,i,cnt = 0;
	for(i=0;i<n;i++)
	{
	if(a[i] == maxi)
	cnt++;
		else if(a[i] > maxi)
		{
			maxi = a[i];
			maxpos = i;
			cnt = 1;
		}

	}
	if(cnt > 1)
	var = 1;
	return maxpos;
}
int main()
{
	int t,i,k,maxpos,cnt,maxi;
	char ch;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cin>>n;

		for(i=0;i<n;i++)
			{
				cin>>a[i];

			}
			cout<<"Case #"<<k<<": ";
		while(check())
		{
            maxpos = calcmaxpos();
            maxi = a[maxpos];
            cnt = 0;
            if(maxi == 1)
            {
                a[maxpos]--;
                ch = 'A'+maxpos;
                cout<<ch<<" ";
            }
            else{
            for(i=0;i<n;i++)
            {
                if(a[i] == maxi && cnt < 2)
                {
                    cnt++;
                    a[i]--;
                    ch = 'A' + i;
                    cout<<ch;
                }

            }
            cout<<" ";
            }
		}
		for(i=0;i<n;i++)
		{
			if(a[i] == 1)
			{
				ch = 'A' + i;
				cout<<ch;
			}
		}


		cout<<"\n";
		}
	return 0;
}
