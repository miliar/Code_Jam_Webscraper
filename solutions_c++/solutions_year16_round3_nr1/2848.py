#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int T,n;
	cin>>T;
	vector<char> vx(27);
	for(int i=1; i<=26; i++)
		vx[i]='A'+i-1;
	for(int tc=1; tc <= T; tc++)
	{
		cin>>n;
		vector<int> v(n+1,0);
		int ss = 0;
		for(int i=1; i<=n; i++)
		{
			cin>>v[i];
			ss+=v[i];
		}
		cout<<"Case #"<<tc<<": ";
		while(ss>0)
		{
			bool none = true;
			for(int i=1; i<=n; i++)
			{
				for(int j=1; j<=n; j++)
				{
					if(v[i]==0||v[j]==0||ss<2)
						continue;
					ss-=2;
					v[i]--;
					v[j]--;
					bool can = true;
					for(int k=1; k<=n; k++)
					{
						if((2*v[k])>ss)
						{
							can = false;
							break;
						}
					}
					if(!can)
					{
						ss+=2;
						v[i]++;
						v[j]++;
					}
					else
					{
						none = false;
						cout<<vx[i]<<vx[j]<<" ";
					}
				}				
			}
			for(int i=1; i<=n; i++)
			{
				if(v[i]==0||ss<1)
					continue;
				ss--;
				v[i]--;
				bool can = true;
				for(int k=1; k<=n; k++)
				{
					if((2*v[k])>ss)
					{
						can = false;
						break;
					}
				}
				if(can)
				{
					cout<<vx[i]<<" ";
				}
				else
				{
					v[i]++;
					ss++;
				}
			}
		}
		cout<<"\n";
	}
}