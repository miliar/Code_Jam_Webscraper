#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <cassert>

#define FOR(i,n) for(int i=0,_n=n;i<_n;i++)
#define FORR(i,s,n) for(int i=s,_n=n;i<_n;i++)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define pli pair<ll,int>
#define vi vector<int>
#define fs first
#define sec second

#define maxn 100000
using namespace std;
typedef long long ll;

string line;
int main(){
	int T,n;
	cin>>T;
	FOR(tt,T){
		cin>>n;
		cin>>line;
		n++;
		
		int ans = 0,nup = 0;
		FOR(i,n){
			if(line[i] != '0' && nup < i){
				ans += i - nup;
				nup = i;
			}
			nup += (line[i] - '0');
		}
		cout<<"Case #"<<tt + 1<<": "<<ans<<"\n";
	}
	return 0;
}
