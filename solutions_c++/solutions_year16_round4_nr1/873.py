#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <cctype>
#include <set>
#include <limits>
using namespace std;

#define FOR(i,f,t) for(int i=f; i<t; i++)
#define ms(obj, val) memset(obj, val, sizeof(obj))
#define pb push_back
#define ri(x) scanf("%d", &x)
#define rii(x,y) scanf("%d %d", &x, &y)
#define SYNC ios_base::sync_with_stdio(false)

typedef long long ll;

string dp[500][20];

int main(){
	dp['R'][0] = "R";
	dp['P'][0] = "P";
	dp['S'][0] = "S";
	dp['R'][1] = "RS";
	dp['P'][1] = "PR";
	dp['S'][1] = "PS";
	FOR(n,2,14){
		string r1 = dp['R'][n-1];
		string r2 = dp['S'][n-1];
		if(r1 < r2){
			dp['R'][n] = r1 + r2;
		}else{
			dp['R'][n] = r2 + r1;
		}
		r1 = dp['P'][n-1];
		r2 = dp['R'][n-1];
		if(r1 < r2){
			dp['P'][n] = r1 + r2;
		}else{
			dp['P'][n] = r2 + r1;
		}
		r1 = dp['P'][n-1];
		r2 = dp['S'][n-1];
		if(r1 < r2){
			dp['S'][n] = r1 + r2;
		}else{
			dp['S'][n] = r2 + r1;
		}
	}
	int TC; ri(TC);
	FOR(tc,1,TC+1){
		int N, R, P, S;
		cin>>N>>R>>P>>S;
		string ret = "Z";
		int cr, cp, cs; cr=cp=cs=0;
		FOR(i,0,dp['R'][N].size()){
			if(dp['R'][N][i] == 'R') cr++;
			if(dp['R'][N][i] == 'P') cp++;
			if(dp['R'][N][i] == 'S') cs++;
		}
		if(cr == R && cp == P && cs == S){
			if(dp['R'][N] < ret) ret = dp['R'][N];
		}
		cr=cp=cs=0;
		FOR(i,0,dp['P'][N].size()){
			if(dp['P'][N][i] == 'R') cr++;
			if(dp['P'][N][i] == 'P') cp++;
			if(dp['P'][N][i] == 'S') cs++;
		}
		if(cr == R && cp == P && cs == S){
			if(dp['P'][N] < ret) ret = dp['P'][N];
		}
		cr=cp=cs=0;
		FOR(i,0,dp['S'][N].size()){
			if(dp['S'][N][i] == 'R') cr++;
			if(dp['S'][N][i] == 'P') cp++;
			if(dp['S'][N][i] == 'S') cs++;
		}
		if(cr == R && cp == P && cs == S){
			if(dp['S'][N] < ret) ret = dp['S'][N];
		}
		cout<<"Case #"<<tc<<": ";
		if(ret[0] == 'Z') cout<<"IMPOSSIBLE\n";
		else cout<<ret<<endl;;
	}

	
}

