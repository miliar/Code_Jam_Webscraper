#include<bits/stdc++.h>
#define ll long long
#define MOD 1000000007
#define MAX 2000007

using namespace std;

char str[MAX],ans[MAX];
int main()
{
	int tc,test,n,i,left,right;
	cin.sync_with_stdio(0);
	cout.sync_with_stdio(0);
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>tc;
	for(test = 1 ; test <= tc;test++)
	{
		cout<<"Case #"<<test<<": ";
		cin>>str;
		left = 2000;
		right = 2000;
		ans[2000] = str[0];
		n = strlen(str);
		for(i=1;i<n;i++)
		{
			if(str[i] >= ans[left])
			{
				left--;
				ans[left] = str[i];
			}
			else
			{
				right++;
				ans[right] = str[i];
			}
		}
		for(i=left;i<=right;i++)
		{
			cout<<ans[i];
		}
		cout<<"\n";
	}
	return 0;
}
