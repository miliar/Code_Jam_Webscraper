/*

	NO SALE u.U
*/
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>
#include <string>
using namespace std;

typedef pair<int,int> pii;
typedef vector<int,int> vii;
#define ll long long
const int MaxN = 200005;
const double eps = 1e-7;
const double DINF = 1e100;
const int INF = 1000000006;
const ll LINF = 1000000000000000005ll;

int n,t;
double A[1005],B[1005];
int main(){
	#ifndef ONLINE_JUDGE
	    freopen("in.txt","r",stdin);
	    freopen("out.txt","w",stdout);
	#endif
	 cin>>t;
	 for (int u = 1; u <= t; ++u){
	 	cin>>n;
	 	for (int i = 0; i < n; ++i)cin>>A[i];
	 	for (int i = 0; i < n; ++i)cin>>B[i];
	 	sort(A,A+n);
	 	sort(B,B+n);
	 	// for (int i = 0; i < n; ++i)cout<<A[i]<<" ";cout<<endl;
	 	// for (int i = 0; i < n; ++i)cout<<B[i]<<" ";cout<<endl;
	 	//A
	 	int idx=0,p=0;
	 	for (; p < n; ++p){
	 		double n1=B[p];
	 		while(idx<n&&A[idx]<n1)idx++;
	 		if(idx==n)break;
	 		idx++;
	 	}
	 	cout<<"Case #"<<u<<": "<<p;
	 	//B
	 	idx=0,p=0;
	 	for (; p < n; ++p){
	 		double n1=A[p];
	 		while(idx<n&&B[idx]<n1)idx++;
	 		if(idx==n)break;
	 		idx++;
	 	}
	 	cout<<" "<<n-p<<endl;
	 }
	return 0;
}