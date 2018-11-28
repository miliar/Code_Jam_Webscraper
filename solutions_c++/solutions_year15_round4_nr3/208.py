#include <stdio.h>
#include <functional>
#include <algorithm>
#include <sstream>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
using namespace std;

int t[20];

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test); for (int Case=1;Case<=Test;Case++){
		printf ("Case #%d: ",Case);

		int N;
		scanf ("%d ",&N);
		map<string, vector<int> > chk;
		for (int i=0;i<N;i++){
			char S[20000];
			gets(S);
			istringstream in(S);
			string a;
			while (in >> a) chk[a].push_back(i);
		}

		vector<pair<int, vector<int> > > u;
		for (auto p : chk) u.push_back(make_pair(1,p.second));
		for (int i=1;i<u.size();i++){
			if (u[i-1].second == u[i].second){
				u[i-1].first++;
				u.erase(u.begin()+i); i--;
			}
		}

		int ans = 125215;
		for (int i=0;i<(1<<(N-2));i++){
			t[0] = 0; t[1] = 1;
			for (int j=0;j<N-2;j++) t[j+2] = (i & (1 << j)) > 0;

			int cnt = 0;
			for (auto p : u){
				bool good = 1;
				for (auto i : p.second){
					for (auto j : p.second) if (i != j && t[i] != t[j]){
						good = 0; cnt += p.first;
						break;
					}
					if (!good) break;
				}
			}
			if (ans > cnt)
				ans = cnt;
		}

		printf ("%d\n",ans);
	}

	return 0;
}