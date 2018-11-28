#include <iostream>
#include <cstring>
using namespace std;

long long DP[128][2010];
long long saved[128][128];
long long gold[128];
long long life[128];
int P, Q, N;

long long solve(int i, int t)
{
	if(DP[i][t]!=-1) return DP[i][t];
	
	long long& ans=DP[i][t];
	ans=0;
	
	if(i==N) return ans;
	
	if(t>=saved[i][0]) ans=max(ans, solve(i+1, t-saved[i][0])+gold[i]);
	ans=max(ans, solve(i+1, t+(life[i]+Q-1)/Q));
	
	
	//cout << saved[i][0] << endl;
	//cout << i << " " << t << " " << ans << endl;
	return ans;
}

int main()
{
	freopen("B-large.in","r", stdin);
	freopen("B-large.out","w", stdout);
	
	int T; cin >> T;
	for(int tc=0; tc<T; tc++)
	{
		cin >> P >> Q >> N;
		for(int i=0; i<N; i++) cin >> life[i] >> gold[i];
		life[0]+=Q;
		
		memset(saved, 0x3f, sizeof(saved));
		for(int i=0; i<N; i++)
		{
			for(int j=0; j*Q<life[i]; j++)
			{
				int rem=life[i]-j*Q;
				saved[i][j]=(rem+P-1)/P-j;
				//cout << i << " " << j << " " << saved[i][j] << endl;
			}
			for(int j=1; j*Q<life[i]; j++)
				saved[i][0]=min(saved[i][0], saved[i][j]);
		}
		
		memset(DP, -1, sizeof(DP));
		long long ans=solve(0,0);
		
		
		cout << "Case #" << tc+1 << ": " << ans << endl;
	}
}
