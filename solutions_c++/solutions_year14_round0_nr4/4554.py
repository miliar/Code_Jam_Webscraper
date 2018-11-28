#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <vector>
#include <cassert>
#include <algorithm>
#include <cctype>
#define INF 2000000000
#define M 1000000007LL

using namespace std;

int main()
{
	int T;
	cin>>T;
	int t = 0;
	while (t++<T){
		int n;
		cin>>n;
		double N[1010] = {0};
		for (int i = 1; i<=n; i++) cin>>N[i];
		double K[1010] = {0};
		for (int i = 1; i<=n; i++) cin>>K[i];
		sort(N+1, N+n+1);
		sort(K+1, K+n+1);
		int res1 = 0, res2 = 0;
		int tail = n;
		int head = 1;
		int v[1010] = {0};
		for (int i = n; i>=1; i--){
			if (K[tail]>N[i]) tail--;
			else{
				head++;
				res2++;
			}
		}
		tail = n;
		for (int i = 1; i<=n; i++){
			int flag = 1;
			for (int j = i; j<=n; j++){
				if (N[j]<K[j-i+1]){
					flag = 0; 
					break;
				}
			}
			if (flag){
				res1 += n-i+1; break;
			}
			if (N[i]<K[tail]) tail--;
		}
		cout<<"Case #"<<t<<": "<<res1<<" "<<res2<<endl;
	}
}