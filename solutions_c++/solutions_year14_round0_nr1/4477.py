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

int n,a;
int main(){
	#ifndef ONLINE_JUDGE
	    freopen("in.txt","r",stdin);
	    freopen("out.txt","w",stdout);
	#endif
	cin>>n;
	for (int c = 1; c <= n; ++c){
		vector<int>	V;
		int v;
		cin>>a;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j){
				cin>>v;
				if(i==a-1)V.push_back(v);
		}
		cin>>a;
		int r=-1,cnt=0;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j){
			cin>>v;
			if(i==a-1){
				for (int k = 0; k < 4; ++k){
					if(V[k]==v){
						r=v;cnt++;
					}
				}
			}
		}
		if(cnt==0)cout<<"Case #"<<c<<": Volunteer cheated!"<<endl;
		if(cnt==1)cout<<"Case #"<<c<<": "<<r<<endl;
		if(cnt>1)cout<<"Case #"<<c<<": Bad magician!"<<endl;
	}
	return 0;
}