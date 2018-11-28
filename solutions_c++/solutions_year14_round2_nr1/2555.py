#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef unsigned long long ul;
typedef pair<int,int> ii;
typedef pair<ll,ll> pll;
typedef vector<ii> vii;

ul one = 1;

int t;
int n;
string arr[111];
int num[111];
int idx[111];
int ans;
int temp;
int sum;
bool ok;
char cc;

int main(){
	scanf("%d",&t);
	for (int jj=1; jj<=t; jj++){
		scanf("%d",&n);
		for (int i=0; i<n; i++){
			cin >> arr[i];
		}
		memset(idx,0,sizeof idx);
		ans = 0;
		ok = true;
		memset(num,0,sizeof num);
		while (idx[0] < arr[0].length()){
			cc = arr[0][idx[0]];
			sum = 0;
			for (int i=0; i<n; i++){
				ok = false;
				while (idx[i] < arr[i].length() && arr[i][idx[i]] == cc){
					ok = true;
					num[i]++;
					sum++;
					idx[i]++;
				}
				if (!ok) break;
			}
			if (!ok) break;
			sum /= n;
			for (int i=0; i<n; i++){
				ans += abs(num[i]-sum);
				num[i] = 0;
			}
		}
		for (int i=0; i<n; i++){
			if (idx[i] < arr[i].length()){
				ok = false;
				break;
			}
		}
		printf("Case #%d: ",jj);
		if (ok) printf("%d\n",ans);
		else printf("Fegla Won\n");
	}
	return 0;
}
