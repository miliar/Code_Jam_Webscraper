#include<iostream>
#include<cmath>
#include<vector>
using namespace std;

int t, w, h, b, XP0[1000], XP1[1000], YP0[1000], YP1[1000];
bool explr[1001];
vector<int> front[1001];

int getdist(int s, int e) {
	int xdiff=0, ydiff=0;
	
	if(XP1[s] < XP0[e] || XP0[s] > XP1[e])
		xdiff = min(abs(XP1[s] - XP0[e]) - 1, abs(XP0[s] - XP1[e]) - 1 );
	
	if(YP1[s] < YP0[e] || YP0[s] > YP1[e])
		ydiff = min(abs(YP1[s] - YP0[e]) - 1, abs(YP0[s] - YP1[e]) - 1 );
	
	return max(xdiff, ydiff);
}


int main() {
	cin.sync_with_stdio(false);
	cin >> t;
	
	for(int TCASE=0; TCASE < t; TCASE++) {
		cin >> w >> h >> b;
		for(int i=0;i<b;i++)
			cin >> XP0[i] >> YP0[i] >> XP1[i] >> YP1[i], front[XP0[i]].push_back(i);
		front[w].push_back(b);
		
		int mincost = 100000;
		for(int i=0;i<=w && mincost > w;i++) {
			for(int j = 0;j<front[i].size();j++) {
				int pos = front[i][j];
				
				if(pos == b) {
					mincost = i;
					break;
				}
				
				if(explr[pos])
					continue;
				explr[pos] = true;
					
				for(int k=0;k<b;k++)
					if(i + getdist(pos, k) < w)
						front[i + getdist(pos, k)].push_back(k);
				
				front[i + w - XP1[pos] - 1].push_back(b);
			}
		}
		
		cout << "Case #" << TCASE + 1 << ": " << mincost << '\n';
		
		for(int i=0;i<1001;i++)
			front[i].clear(), explr[i] = false;
	}
	
	return 0;
}































