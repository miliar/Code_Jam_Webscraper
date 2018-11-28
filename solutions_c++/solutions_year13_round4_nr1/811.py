#include <bits/stdc++.h>

using namespace std;

int o[1000005], e[1000005], p[1000005];

#define MOD 1000002013

long long modprod(long long A, long long B)
{
	long long P = 0;
	
	while(B)
	{
		if(B & 1) P = (P + A) % MOD;
		
		B >>= 1;
		A = (A << 1) % MOD;
	}
	return P;
}

int main()
{
	int nCasos;
	scanf("%d", &nCasos);
	
	for(int caso=1; caso<=nCasos; caso++)
	{
		int n, m;
		scanf("%d %d", &n, &m);
		
		long long tot1 = 0;
		for(int i=0; i<m; i++)
		{
			scanf("%d %d %d", &o[i], &e[i], &p[i]);
			int d = e[i] - o[i];
			int sum = 1LL * n * d % MOD - (1LL * d * (d-1) / 2) % MOD;
			sum = (sum + MOD) % MOD;
			tot1 = (tot1 + 1LL * sum * p[i]) % MOD;
		}
		
		set < pair <int, int> > evt;
		for(int i=0; i<m; i++)
		{
			evt.insert(make_pair(o[i], -(i+1)));
			evt.insert(make_pair(e[i], +(i+1)));
		}
		
		set < pair <int, int> > S;
		int sz = m;
		
		long long tot2 = 0;
		
		for(set < pair <int, int> > :: iterator it = evt.begin(); it != evt.end(); it++)
		{
			int pos = (*it).first;
			int idx = (*it).second;
			
			if(idx < 0)
			{
				idx = -idx-1;
				
				//assert(p[idx] > 0);
				
				//cout<<"llega a "<<pos<<" "<<idx<<endl;
				S.insert(make_pair(pos, idx));
				
				//if(idx == 61) cout<<pos<<" INSERTTTTTTTTT "<<idx<<endl;
			}
			else
			{
				idx = idx-1;
				
				//assert(p[idx] > 0);
				
				while(p[idx] > 0)
				{
					//cout<<S.size()<<" "<<idx<<" "<<p[idx]<<endl;
					
					set < pair <int, int> > :: iterator it2 = S.end();
					assert(S.size() > 0);
					it2--;
					int idy = (*it2).second;
					
					//cout<<(*it2).first<<" "<<idy<<" "<<p[idy]<<endl;
					if(p[idy] == 0) return 0;
					
					if(idy == idx || (o[idy] <= o[idx]))
					{
						int d = e[idx] - o[idx];
						int sum = 1LL * n * d % MOD - (1LL * d * (d-1) / 2) % MOD;
						sum = (sum + MOD) % MOD;
						tot2 = (tot2 + 1LL * sum * p[idx]) % MOD;
						
						p[idx] = 0;
						//if(idx == 61) cout<<"bbbbbbbbb"<<endl;
					}
					else
					{
						int cnt = min(p[idy], p[idx]);
						assert(cnt != 0);
						
						int d = e[idx] - o[idy];
						int sum = 1LL * n * d % MOD - (1LL * d * (d-1) / 2) % MOD;
						sum = (sum + MOD) % MOD;
						tot2 = (tot2 + 1LL * sum * cnt) % MOD;
						
						p[idx] -= cnt;
						//if(idx == 61) cout<<"xxxxxxxxxxxxxxxxxxxx"<<endl;
						//cout<<p[idx]<<endl;
						
						int q = p[idy] - cnt;
						p[idy] = q;
						if(q == 0)
						{
						//	if(idy == 61) cout<<o[idy]<<" uuuuuuuuuuuuuuuuuuu"<<endl;
							S.erase(make_pair(o[idy], idy));
							evt.erase(make_pair(e[idy], +(idy+1)));
						}
						
						int nidy = sz++;
						//S.insert(make_pair(o[idx], nidy));
						
						o[nidy] = o[idx];
						e[nidy] = e[idy];
						p[nidy] = cnt;
						//if(nidy == 61) cout<<o[idx]<<" INSERTTTTTTTTT "<<nidy<<endl;
						
						S.insert(make_pair(o[idx], nidy));
						evt.insert(make_pair(e[idy], +(nidy+1)));
					}
				}
				S.erase(make_pair(o[idx], idx));
			}
		}
		
		//cout<<tot1<<" "<<tot2<<endl;
		
		long long ans = ((tot1 - tot2) % MOD + MOD) % MOD;
		cout<<"Case #"<<caso<<": "<<ans<<endl;
	}
  
	return 0;
}
