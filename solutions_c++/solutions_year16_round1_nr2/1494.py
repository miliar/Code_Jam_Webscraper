//Naman Agarwal
//IIT Mandi
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <iomanip>
#include <string>

using namespace std;

#define lli long long int

int main() {
	ios::sync_with_stdio(false);
	int t,tc=1;
	cin>>t;
	while(t--){
		int n;
		cin>>n;
		int a[2*n-1][n];
		int ht[3000];
		for(int i=0;i<3000;i++){
			ht[i]=0;
		}
		vector<int> ans;
		for(int i=0;i<2*n-1;i++){
			for(int j=0;j<n;j++){
				cin>>a[i][j];
				ht[a[i][j]]++;
			}
		}
		cout<<"Case #"<<tc<<": ";
		for(int i=0;i<3000;i++){
			if(ht[i]&1){
				cout<<i<<" ";
			}
		}
		cout<<"\n";
		tc++;
	}
	return 0;
}