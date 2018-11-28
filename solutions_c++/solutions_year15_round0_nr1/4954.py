//void * memset ( void * ptr, int value, size_t num )
#include<bits/stdc++.h>
using namespace std;

typedef long long LL;
#define MAX 1000000
#define MOD 1000000007
int arr[1001];

int main()
{
	ios_base::sync_with_stdio(false);
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int n,t,i,smax,cnt,need;
	string s;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		cnt=0;
		need=0;
		cin>>smax>>s;
		for(i=0;i<smax+1;i++)
		{
			if(cnt < i)
			{
				need+=i-cnt;
				cnt+=i-cnt;
			}
			cnt+=s[i]-'0';
		}
		cout<<"Case #"<<j<<": "<<need<<endl;
	}
	return 0;
}