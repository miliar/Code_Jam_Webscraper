#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <map>
#include <set>
#include <algorithm>
using namespace std;
const int maxn = 10000 + 10;
int a[maxn];
int main(){
	int T, cas = 0;
	for (cin>>T; T--;){
		cout<<"Case #"<<++cas<<": ";
		int n, m;
		cin>>n>>m;
		for (int i = 0; i<n; i++) cin>>a[i];
		sort(a, a+n);
		int ct = 0;
		int j = 0;
		for (int i = n-1; i>=0; i--){
			if (a[i] == -1) continue;
			if (j<i && a[j] + a[i] <= m){
				a[j] = -1;
				j++;
				ct++;
			}else{
				ct += 1;
			}
			a[i] = -1;
		}
		cout<<ct<<endl;
	}
	return 0;
}



