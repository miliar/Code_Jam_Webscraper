#include<vector>
#include<iostream>
#include<iomanip>
#include<vector>
#include<algorithm>
#define f first
#define s second
#define mp make_pair
using namespace std;

int T, n;

double v, x, r, c;




int main() {
	cin.sync_with_stdio(false);
	
	cin >> T;
	
	for(int TCASE = 1; TCASE <= T ; TCASE++) {
		vector<pair<double, double> > side[2];
		double diff[2], volume[2];
		
		diff[0] = 0;
		diff[1] = 0;
		volume[0] = 0;
		volume[1] = 0;
		
		
		cin >> n >> v >> x;
		
		for(int i=0;i<n;i++) {
			cin >> r >> c;
			
			int ind = 1;
			c -= x;
			
			if(c < 0) {
				ind = 0;
				c = -c;
			}
			
			volume[ind] += r;
			diff[ind] += c * r;
			side[ind].push_back(mp(c, r) );
		}
		
		double totalvol = volume[1];
		double diffneed = diff[1];
		int ind = 0;
		
		if(diff[1] > diff[0]) {
			ind = 1;
			totalvol = volume[0];
			diffneed = diff[0];
		}
		
		
		//Finally we calculate how much volume we can add on the heavier side
		
		sort(side[ind].begin(), side[ind].end());
		
		double cdiff = 0;
		
		for(int i=0;i<side[ind].size();i++) {
			if(side[ind][i].s * side[ind][i].f + cdiff <= diffneed) {
				cdiff += side[ind][i].s * side[ind][i].f;
				totalvol += side[ind][i].s;
			}
			
			else {
				double toadd = (diffneed - cdiff) / (side[ind][i].s * side[ind][i].f);
				
				cdiff = diffneed;
				totalvol += side[ind][i].s * toadd;
			}
		}
		
		
		cout << "Case #" << TCASE << ": ";
		
		if(totalvol == 0)
			cout << "IMPOSSIBLE\n";
		else
			cout << fixed << setprecision(7) << v / totalvol << '\n';
	}
	
	return 0;
}





























