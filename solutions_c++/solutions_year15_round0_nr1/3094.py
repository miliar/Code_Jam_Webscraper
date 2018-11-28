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
	int n; cin>>n;
	string s; cin>>s;
	
	int have = s[0]-'0';
	int req = 0;
	
	for(int sl=1;sl<=n;sl++){
		if(have<sl){
			req += sl-have;
			have += sl-have;
		}
		have += s[sl]-'0';
	}
	
	cout<<req<<endl;
}

}