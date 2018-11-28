#include<bits/stdc++.h>
using namespace std;
int m[500],n[]={0,6,2,8,3,7,4,1,5,9};
string ss[]={"ZERO", "SIX", "TWO", "EIGHT", "THREE", "SEVEN", "FOUR", "ONE", "FIVE", "NINE"},s;
vector<int> v;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.txt","w",stdout);
	int a,b,c,d,check;
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cin>>a;
	for(b=0;b<a;b++)
	{
		v.clear();
		memset(m,0,sizeof(m));
		cin>>s;
		for(c=0;s[c];c++)
		{
			m[s[c]]++;
		}
		cout<<"Case #"<<b+1<<": ";
		for(c=0;c<10;c++)
		{
			check=1;
			while(check)
			{
				check=0;
				for(d=0;ss[c][d];d++)
				{
					if(m[ss[c][d]]==0)break;
					m[ss[c][d]]--;
				}
				if(d==ss[c].length())
				{
					v.push_back(n[c]);
					check=1;
				}
				else
				{
					for(d=d-1;d>=0;d--)
					{
						m[ss[c][d]]++;
					}
				}
			}
			
		}
		sort(v.begin(),v.end());
		for(c=0;c<v.size();c++)cout<<v[c];
		cout<<"\n";
	}
}
