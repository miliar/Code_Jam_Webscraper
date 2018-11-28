#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#include<cstdlib>
#include<iostream>
#include<vector>
using namespace std;
vector<int>v;
int a[5000];
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t;
	cin >> t;
	int cas = 1;
	int n;
	while (t--){
		cin >> n;
		memset(a,0,sizeof(a));
		int x;
		for (int i = 0; i < (2*n-1)*n; i++){
			cin >> x;
			a[x] ++;
		}
		for (int i = 1; i <= 2500; i++){
			if (a[i] % 2 == 1)
				v.push_back(i);
		}
		sort(v.begin(),v.end());
		printf("Case #%d:",cas++);
		for (int i = 0; i < v.size(); i++){
			printf(" %d",v[i]);
		}
		v.clear();
		printf("\n");
	}
	return 0;
}