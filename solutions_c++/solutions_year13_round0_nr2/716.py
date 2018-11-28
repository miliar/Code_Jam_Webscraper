#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;

int maxC[101], maxR[101];
int a[101][101];

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int T;
	cin>>T;

	for (int t = 0; t < T; t++){
		int n, m;
		cin>>n>>m;

		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				cin>>a[i][j];

		for (int i = 0; i < n; i++){
			maxR[i] = a[i][0];
			for (int j = 1; j < m; j++)
				maxR[i] = max(maxR[i], a[i][j]);
		}
		
		for (int i = 0; i < m; i++){
			maxC[i] = a[0][i];
			for (int j = 1; j < n; j++)
				maxC[i] = max(maxC[i], a[j][i]);
		}

		bool can = true;

		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++){
				if (maxR[i] > a[i][j] && maxC[j] > a[i][j])
					can = false;
			}

		cout<<"Case #"<<t + 1<<": ";
		
		if (can)
			cout<<"YES";
		else
			cout<<"NO";

		cout<<endl;;
	}
}