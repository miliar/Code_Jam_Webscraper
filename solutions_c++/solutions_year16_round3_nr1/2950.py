#include <iostream>
#include <cstdio>
#include <algorithm>
#include <climits>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>

using namespace std;

bool mycmp(pair<int,int> &i,pair<int,int> &j) {	
	return (i.first <= j.first);
}


int main()
{	int T;
	cin >> T;
	for(int t=1; t<=T; t++) {
		int N;
		cin >> N;
		vector< pair<int, int> > p;
		
		int x;
		for(int i=0; i<N; i++) {
			cin >> x;
			p.push_back(make_pair(x,i));
		}
		
		string ans = "";
		string alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		while(true) {
			//Checking termintation condition
			bool zf = true;
			for(int i=0; i<N; i++) {
				zf &= (p[i].first==0);
			}
			if(zf) {
				break;
			}
			
			sort(p.begin(), p.end());
			
			// for(int i=0; i<N; i++) {
				// cout << "(" << p[i].first << ", " << p[i].second << ")\t";
			// }
			// cout << endl; 
			
			if(p[N-1].first==p[N-2].first) {
				int s=0;
				for(int i=N-1; i>=0; i--) {
					s += p[i].first;
				}
				if(s==N && N%2==1) {
					ans =  ans + alpha[p[N-1].second] + " ";
					p[N-1].first--;
				}
				else {
					ans =  ans + alpha[p[N-1].second] + alpha[p[N-2].second] + " ";
					p[N-1].first--;
					p[N-2].first--;
				}
			}
			else {
				if(p[N-1].first-2 >= 0) {
					int x = p[N-1].first-2;
					int s=x;
					for(int i=N-2; i>=0; i--) {
						s += p[i].first;
					}
					bool bf = false;
					for(int i=N-2; i>=0; i--) {
						bf |= (p[i].first > s/2);
					}
					if(!bf) {
						ans = ans + alpha[p[N-1].second] + alpha[p[N-1].second] + " ";
						p[N-1].first -= 2;
					}
					else {
						ans = ans + alpha[p[N-1].second] + " ";
						p[N-1].first--;
					}
				}
				else {				
					ans = ans + alpha[p[N-1].second] + " ";
					p[N-1].first--;
				}
			}
			// cout << ans << endl << endl;
		}
		
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}