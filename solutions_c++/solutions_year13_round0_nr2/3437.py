/*
ID: rohangu1
LANG: C++
TASK: 
*/

#include <iostream>
#include <fstream>
#include <utility>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cmath>
#include <set>
#include <string>
#include <queue>
#include <cstdio>

using namespace std;

typedef vector<int> vi;
typedef vector< vi > vvi;
typedef pair<int,int> ii;
typedef long long LL;

#define np next_permutation
#define FOR(i,a,b) for(i=a;i<=b;i++)
#define tr(c, it) \
		for(typeof(c.begin()) it = c.begin() ; it != c.end() ; it++)
#define max(a,b) (a>b?(a):(b))
#define min(a,b) (a>b?(b):(a))
#define all(a) (a).begin(),(a).end()
#define mp(i,j) make_pair(i,j)
#define sz(a) a.size()
#define pb(i) push_back(i) 
#define fx first
#define sx second
#define MOD 1000000007

ifstream in("lawn.in",ifstream::in);
ofstream out("lawn.out",ios::out);

int a[111][111];

int main(){
	int i,j,k;
	int n,m,t,c;
	bool valid;
	in>>t;
	FOR(c,1,t){
		in>>n>>m;
		FOR(i,1,n){
			FOR(j,1,m){
				in>>a[i][j];
			}
		}
		valid = true;
		FOR(i,1,n){
			FOR(j,1,m){
				FOR(k,1,m){
					if(a[i][k]>a[i][j]){
						break;
					}
				}
				if(k>m)
					continue;
				FOR(k,1,n){
					if(a[k][j]>a[i][j]){
						valid = false;
						break;	
					}
				}
				if(!valid)
					break;
			}
			if(!valid)
				break;
		}
		out<<"Case #"<<c<<": ";
		if(valid)
			out<<"YES"<<endl;
		else
			out<<"NO"<<endl;
	}
	return 0;
}
