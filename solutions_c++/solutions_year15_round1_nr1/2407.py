#include <bits/stdc++.h>

#define F(i,a,b) for(int i = a; i < b; i++)
#define pb push_back
#define mp make_pair
#define all(a) a.begin(), a.end()


using namespace std;

typedef vector<int> vi;
typedef vector<vi> vii;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<vs> vvs;
typedef  long long ll;

int main()
{
	std::ios_base::sync_with_stdio(false);
	
	int T,N = 0;
	cin >> T;
	F(cs,0,T)
	{
		cout << "Case #" << cs+1 << ": ";
		cin >> N;
		vi V(N);
		int maxN = 0,ind;
		F(i,0,N)
		{
			cin >> V[i];
			if(i > 0 && (V[i-1] > V[i]))
				maxN = max(maxN,V[i-1] - V[i]);
		}
			
		long long X = 0, Y = 0,curr = 0;
		curr = V[0];
		for(int i = 1 ; i < N;i++)
		{
			if(V[i-1] > V[i])
				X += (V[i-1] - V[i]);
			else
				curr = V[i];	
		}
		for(int i = 0 ; i < N-1;i++)
		{
			if(V[i] <= maxN)
				Y += V[i];
			else
				Y += maxN;
		}
		cout << X << " " << Y << endl;
	}
	return 0;
}
