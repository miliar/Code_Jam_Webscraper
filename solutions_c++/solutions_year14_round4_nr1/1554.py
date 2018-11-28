#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <vector>
#include <cassert>
#include <algorithm>
#include <cctype>
#include <iomanip>
#include <queue>
#define INF 200000000000LL
#define M 1000000007LL
#define PI 3.14159265358

using namespace std;

int T;
int a[100000];

int main()
{
	cin>>T;
	int t = 0;
	while (T--){
		t++;
		int n;
		int x;
		cin>>n>>x;
		for (int i = 1; i<=n; i++){
			scanf("%d", a+i);
		}
		sort(a+1, a+n+1);
		int l, r;
		l = 1; r = n;
		int tmp = x;
		int res = 0;
		while (l<=r){
			//cout<<l<<" "<<r<<endl;
			if (a[l]+a[r]<=x){
				l++; r--; 
			}
			else{
				r--;
			}
			res++;
		}
		cout<<"Case #"<<t<<": "<<res<<endl;
	}
}