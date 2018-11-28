#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#include <sstream>
#include <queue>
#include <cctype>
#include <cmath>
#include <fstream>

using namespace std;

typedef long long ll;
#define REP(i,k) for(int (i)=0;(i)<(k);(i)++)
#define INF ~(1<<31)
#define CLR(a) memset((a),0,sizeof((a)))
#define EPS 1e-9
#define DBG 1
#define D(s,v) if(DBG) cout<<(s)<<": "<<(v)<<endl;
#define DVEC(s,v) if(DBG) {cout<<(s)<<": "; for(int i=0;i<(v).size();i++) cout<<(v)[i]<<" "; cout<<endl;}
#define DARR(s,v,n) if(DBG) {cout<<(s)<<": "; for(int i=0;i<n;i++) cout<<(v)[i]<<" "; cout<<endl;}

int main(){
ios_base::sync_with_stdio(0);

int T;
cin>>T;

for(int cs=1;cs<=T;cs++){
	cout<<"Case #"<<cs<<": ";
	int N; cin>>N;
	vector<int> d;
	
	for(int i=0;i<N;i++){
		int p; cin>>p;
		d.push_back(p);
	}
	
	int res = 1000000000;
	
	for(int mx=1;mx<=2000;mx++){
		int cres = mx;
		
		for(int i=0;i<N;i++){
			if(d[i]>mx){
				int rem = d[i]-mx;
				cres += rem/mx;
				if(rem%mx!=0) cres++;
			}
		}
		
		res = min(res,cres);
	}
	
	cout<<res<<endl;
}

}