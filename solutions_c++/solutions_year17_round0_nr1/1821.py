#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
#define forr(i, n) for(int i=0;i<(n);i++)
#define forv(i, v) for(int i=0;i<(int)v.size();i++)
#define fords(it, ds) for(auto it = ds.begin();it!=ds.end();it++)
#define OO (int)1e9
#define fr first
#define se second
#define II pair<int, int>
#define pb push_back
#define dist(x,y,xx,yy) sqrt((x-xx)*(x-xx)+(y-yy)*(y-yy))
///////////////////// Solution Code

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	#ifndef ONLINE_JUDGE
		#ifdef _WIN64
		freopen("C:\\Users\\mamdouh\\Desktop\\a1.in","r",stdin);
		freopen("C:\\Users\\mamdouh\\Desktop\\A2.out","w",stdout);
		#elif __linux__
		freopen("/media/mamdouh/System/Users/Mamdouh/Desktop/a1.in","r",stdin);
		freopen("/media/mamdouh/System/Users/Mamdouh/Desktop/A2.out","w",stdout);
		#endif
	#endif
	int t,tt=0;
	cin>>t;
	while(tt++<t)
	{
		cout<<"Case #"<<tt<<": ";
		string s;
		int k,i=0,sol=0;
		cin>>s>>k;
		int n=s.length();
		for(;i<n;i++)
		{
			if(s[i]=='+')
				continue;
			if(n-i>=k)
			{
				for(int j=i;j<k+i;j++)
					if(s[j]=='-')s[j]='+';
					else s[j] = '-';
					i--;
					sol++;
			}
			else break;
		}
		if(i!=n)
			cout<<"IMPOSSIBLE\n";
		else cout<<sol<<"\n";

	}
	return 0;
}