#include<bits/stdc++.h>
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(auto i = (c).begin(); i != (c).end(); i++) 
#define F(i,n) for(int i=0;i<n;i++)
#define VE(i,v) for(int i = 0;i < sz(v);i++)
using namespace std;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef long long ll;
typedef unsigned int ui;
const double PI  =3.141592;

int main()
{
	//std::ios::sync_with_stdio(false);
	cin.tie(NULL);
	int T;
	cin >> T;
	for(int tc= 1; tc<= T; tc++)
	{
		cout <<"Case #"<<tc<<": ";
		int K, C, S;
		cin>> K>>C>>S;
		vector<vector<ll> > mat(C, vector<ll>(K));
		if (S <K)
		{
			cout <<"IMPOSSIBLE\n";
			continue;
		}
		for(int i = 0; i < K; i++)
			mat[0][i] = i+1;
		ll len = K*1LL;
		ll temp = 1LL;
		for(int j = 1; j < C; j++)
		{
			for(int i =0; i < K; i++)
			{
				mat[j][i] = i*1LL+1LL+(len*temp*i);
			}
			temp = (temp <<1)|1;
		}
		for(int i=0; i < K; i++)
		{
			cout<<mat[C-1][i]<<" ";
		}
		cout <<"\n";
	}

}
		



