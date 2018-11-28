#include<bits/stdtr1c++.h>
using namespace std;
typedef long long LL;
int n;


int mini;

void solve(map<int,int> m,int p,int d)
{
	int v= (--m.end())->first;
	int kv=(--m.end())->second;
	m.erase(--m.end());
	mini=min(mini,v+p);

	if(v==9)
	{
		map<int,int> th=m;
		int k1=3;
		int k2=v-k1;
		int mx=max(k1,k2);
		int tn=kv;
		th[k1]+=tn;
		if(k2)
		th[k2]+=tn;
		solve(th,p+tn,d+1);
	}
	int k1=v/2 + (v%2!=0);
	int k2=v-k1;
	int mx=max(k1,k2);
	int tn=kv;
	m[k1]+=tn;
	if(k2)
		m[k2]+=tn;
	if(v!=1)
	solve(m,p+tn,d+1);
}
int main()
{
    #ifndef ONLINE_JUDGE
        freopen("2.in","r",stdin);
		freopen("2.out","w",stdout);
    #endif // ONLINE_JUDGE

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t,ic=1;
    cin>>t;
    while(t--)
    {
    	cin>>n;
    	int a;
    	map<int,int> m;
    	vector<int> v;
    	for(int i=0;i<n;i++)
    	{
    		cin>>a;
    		if(m.count(a)==0)
    			v.push_back(a);
    		m[a]++;
    	}
    	sort(v.begin(),v.end());
    	int ret=v.back();
    	for(mini=v.back();mini>=1;mini--)
    	{
    		int f=1;
    		int k=0;
    		for(int j=v.size()-1;j>=0;j--)
    		{
    			if(v[j]<=mini)
    				break;
    			else
    			{
    				int t=v[j]/mini - (v[j]%mini==0) ;//+ (v[j]%mini!=0);
    				k+=t*m[v[j]];
    			}
    		}
    		ret=min(ret,mini+k);
    	}
    	cout<<"Case #"<<ic++<<": "<<ret<<endl;
    }
    return 0;

}
