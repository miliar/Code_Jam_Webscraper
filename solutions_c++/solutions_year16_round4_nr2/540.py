#include <bits/stdc++.h>
using namespace std;
typedef long long               ll;
const int mod = 1e9+7;
#ifndef M_PI
#define M_PI acos(-1.0)
#endif

int tests;
int k, n;
double p[222];

int main(){
	cout<<fixed<<setprecision(10);
	cin>>tests;
	for(int ct=0; ct<tests; ++ct){
		cin>>n>>k;
		for(int i=0; i<n; ++i){
			cin>>p[i];
		}
		sort(p,p+n);
		double res=0;
		for(int i=0; i<=k; ++i){
			vector<double> p_of(k+1);
			p_of[0]=1.0;
			for(int j=0; j<i; ++j){
				vector<double> p_nxt(k+1);
				for(int l=0; l<k; ++l){
					p_nxt[l+1]+=p_of[l]*p[j];
					p_nxt[l]+=p_of[l]*(1.0-p[j]);
				}
				swap(p_of, p_nxt);
			}
			for(int j=n-1; j>=n-k+i; --j){
				vector<double> p_nxt(k+1);
				for(int l=0; l<k; ++l){
					p_nxt[l+1]+=p_of[l]*p[j];
					p_nxt[l]+=p_of[l]*(1.0-p[j]);
				}
				swap(p_of, p_nxt);
			}
			res=max(res, p_of[k/2]);
		}
		cout<<"Case #"<<ct+1<<": "<<res<<"\n";
	}
	return 0;
}
