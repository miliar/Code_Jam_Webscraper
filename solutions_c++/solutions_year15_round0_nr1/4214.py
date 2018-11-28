//#include<bits/stdc++.h>
#include<iostream>
#include<string>
#include<cstring>
#include<iomanip>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cmath>
#include<set>
#include<ctime>
#include<cctype>
#include<memory>
#include<cstdlib>
#include<map>
#include<list>
#include<queue>
#include<stack>
#include<climits>
#include<complex>
#include<utility>
#include<functional>
#define INF 0x7fffffff
#define FILL_NINF 0xef
#define FILL_INF 0x3f
#define RE cerr<<"REdebuge"<<endl;
#define M7 1000000007
#define M9 1000000009
#define ifor(s,n) for(int i=(s);i<(n);i++)
#define rep(rep_val) for(int REP_i=0;REP_i<(rep_val);REP_i++)
#define tmin(a,b,c) min((a),min((b),(c)))
#define tmax(a,b,c) max((a),max((b),(c)))
#define eps 1e-8
using namespace std;
typedef long long ll;
typedef pair<int, int> Poi;

const int maxv=100005;
int T,t=0;
string s;
int sm;
int main(){
  freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);
	cin>>T;
	while(T--){
		t++;
		cin>>sm;
		cin>>s;
		int sum=0;
		int ans=0;
		for(int i=0;i<=sm;i++){
			if(sum<i){
				ans+=i-sum;
				sum=i+s[i]-'0';
			}
			else sum+=s[i]-'0';
		}
		printf("Case #%d: %d\n",t,ans);
	}
    return 0;
}