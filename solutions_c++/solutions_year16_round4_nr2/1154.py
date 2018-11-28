#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <queue>
#include <string.h>
#include <set>

#define ll long long

using namespace std;


double tab[30];

double dp[30][30];

double vv(vector<double> input){


	// for(int i=0 ;i<input.size(); ++i)
		// cout<<input[i]<<" ";
	// cout<<" __ \n";

	for(int i=0; i<20; ++i)
		for(int j=0; j<20; ++j)
			dp[i][j] = 0.0;

	dp[0][0] = 1.0;

	for(int i=1; i<=input.size(); ++i)
		for(int j=0; j<=input.size(); ++j){


			double l = 0.0;
			double r = 0.0;


			if(j > 0)
				l = dp[i-1][j-1];
			if(j < input.size());
				r = dp[i-1][j+1];

			// dp[i][j] = max((1.0-input[i-1])*dp[i-1][j], input[i-1]*r + (1.0-input[i-1])*l);
			dp[i][j] = (1.0-input[i-1])*dp[i-1][j] + input[i-1]*l;
		}

		// cout<<dp[1][1]<<"\n";
		return dp[input.size()][input.size()/2];


}


void solve(int t) {
	ll n, k;
	cin>>n>>k;
	unsigned int nmbr = 1;
	
	for(int i=0; i<n; ++i) {
		cin>>tab[i];
		nmbr *= 2;
	}
	// cout<<n<<" "<<nmbr<<"\n";	
	double mx = 0.0;
	for(unsigned int i=0; i<nmbr; ++i){
		if(__builtin_popcount(i) == k) {
			// cout<<"N: "<<i<<"\n";	
			unsigned int j = i;
			int ind = 0;
			vector<double> vals;
			while(j) {
				if(j % 2){
					// cout<<"Adding: "<<ind<<"\n";
					vals.push_back(tab[ind]);
				}

				j /= 2;
				ind++;
			}
				// cout<<"E\n";

			mx = max(mx, vv(vals));

		}
	}	



	cout<<fixed<<"Case #"<<t<<": "<<mx<<"\n";

}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	std::cout.unsetf ( std::ios::floatfield );
	cout.precision(7);

	int T;
	cin>>T;
	int t = 1;
	while(T--)
		solve(t++);

	return 0;

}