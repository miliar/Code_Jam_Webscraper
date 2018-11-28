#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
typedef vector<vpii> vvpii;
typedef vector<string> vs;
typedef unsigned long long llu;
#define forl(i,a,b) for(i=a;i<b;i++)


pll get_state(ll no,ll k)
{
	 pll x;
	 if(no%k)
	 	x.first=no/k+1;
	 else
	 	x.first=no/k;
	 x.second=k-1;
	 return x;
}

int main()
{
	ios_base::sync_with_stdio(false);
	//cin.tie(NULL);
	ll t,d,i,j,l,temp,tem,sum,ans,caseno=0;
	cin>>t;
	vpll lstates;
	pll state,state2;
	while(t--)
	{
		ans=999999999;
		lstates.resize(0);
		caseno++;
		vl a;
		cin>>d;
		forl(i,0,d)
		{
			cin>>tem;
			a.push_back(tem);
		}
		sort(a.begin(),a.end());
		forl(i,0,d)
		{
			// generates all active states.
			vpll temp;
			ll profit=1,k=1,temp_time=99999;
			while(profit)
			{
				state = get_state(a[i],k);
				if(temp_time>=state.first+state.second) // check if the new state's time is good
				{
					temp_time=state.first+state.second;
					k++;
					if(k>a[i])
						profit=0;
				}
				else
					profit=0;
				if(!lstates.size())
					temp.push_back(state);
				forl(j,0,lstates.size())
				{
					state2.first=max(state.first,lstates.at(j).first); // get max of highest of both
					state2.second=state.second+lstates.at(j).second;  // add overhead of both
					ll new_state_useless=0;
					forl(l,0,temp.size()) // traverse all new current states and check if the new state we have is useless or not.
					{
						if(temp.at(l).first==state2.first)
						{
							if(temp.at(l).second<=state2.second)
								new_state_useless=1;
						}
					}
					if(!new_state_useless)
						temp.push_back(state2);
				}
			}
			lstates=temp;
		}
		forl(i,0,lstates.size())
		{
			if(ans>(lstates.at(i).first+lstates.at(i).second))
				ans=(lstates.at(i).first+lstates.at(i).second);
		}
		cout<<"Case #"<<caseno<<": "<<ans<<endl;
	}
	return 0;
}