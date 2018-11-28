#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <vector>
#include <string>
#include <cassert>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;

inline int bitcount(int a){
	int rez = 0;
	while(a>0){
		if(a&1) rez++;
		a>>=1;
	}
	return rez;
}

int ff[202][202][202];
int ttl[202][202][202];
int curTtl;

double f(const vector<double>& p, int l, int r, int k){
	if(l>=r) return 0.0;
	if(k>(r-l)) return 0.0;
	if(r-l==1){
		if(k==0){
			return 1-p[l];
		}else{
			return p[l];
		}
	}
	if(r-l==2){
		if(k==0){
			return (1-p[l])*(1-p[l+1]);
		}else if(k==1){
			return (1-p[l])*p[l+1] + p[l]*(1-p[l+1]);
		}else{
			return p[l]*p[l+1];
		}
	}
	if(ttl[l][r][k]==curTtl && ff[l][r][k]!=-1){
		return ff[l][r][k];
	}
	double rez = 0;
	for(int i=0; i<=k; i++){
		double cur = f(p, l, l+(r-l)/2, i)*f(p, l+(r-l)/2, r, k-i);
		rez+=cur;
	}
	ff[l][r][k] = rez;
	ttl[l][r][k] = curTtl;
	return rez;
}

double fff(const vector<double>& p, int l, int r, int k){
	int n = p.size();
	assert(k==n/2 && n%2==0);
	int end = (1<<n);
	double rez = 0.0;
	for(int mask=0; mask<end; mask++){
		if(bitcount(mask)==k){
			double cur = 1.0;
			for(int i=0; i<n; i++){
				if(mask & (1<<i)){
					cur*=p[i];
				}else{
					cur*=(1-p[i]);
				}
			}
			rez+=cur;
		}
	}
	return rez;
}

int main(){
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int ntests;
	cin>>ntests;
	for(int i=0; i<202; i++)
		for(int j=0; j<202; j++)
			for(int z=0; z<202; z++){
				ff[i][j][z] = -1;
				ttl[i][j][z] = 0;
			}
	for(int testnum=0; testnum<ntests; testnum++){
		int n, k;
		cin>>n>>k;
		vector<double> p(n);
		for(int i=0; i<n; i++) cin>>p[i];
		int end = (1<<n);
		double rez = 0.0;
		vector<double> chosen(k);
		for(int mask=0; mask<end; mask++){
			if(bitcount(mask)==k){
				int pz = 0;
				for(int i=0; i<n; i++){
					if(mask&(1<<i)){
						chosen[pz] = p[i];
						pz++;
					}
				}
				assert(pz==k);
				curTtl++;
//				double cur = f(chosen, 0, k, k/2);
				double cur2 = fff(chosen, 0, k, k/2);
//				if(abs(cur-cur2)>1e-9){
//					cout<<n<<' '<<k<<endl;
//					for(int i=0; i<k; i++) cout<<chosen[i]<<' ';
//					cout<<endl;
//					cout<<cur<<' '<<cur2<<endl;
//					return 0;
//				}
				rez = max(rez, cur2);
			}
		}
		cout<<"Case #"<<testnum+1<<": "<<setiosflags(ios::showpoint|ios::fixed)<<setprecision(7)<<rez<<endl;
	}
	return 0;
}
