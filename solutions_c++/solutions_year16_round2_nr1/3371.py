#include <math.h>
#include <time.h>
#include <ctype.h>
#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
 
using namespace std;
const int INF= 2147483647;

#define MAX(a,b) ((a>b)?a:b)
#define MIN(a,b) ((a<b)?a:b)
#define REP(i,a) for(int i=0;i<(a);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define pb(x) push_back(x)
#define SORT(a,n) sort(begin(a),begin(a)+n)
#define REV(a,n) reverse(begin(a),begin(a)+n)
#define ll long long
#define pii pair<int,int>
#define MOD 1000000007
#define DEBUG(x) cout<<">>>> "<<x<<endl
 
string letters[] = {"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"}; 
int flag[26]; 
bool contains(string s,char a){
	for(int i=0;i<s.length();i++){
		if(s.at(i)==a){
			return true;
		}
	}
	return false;
}
int main(){
	ios::sync_with_stdio(false);

	//int n;
	//int m;
	//
	//scanf("%d %d",&n,&m);
	//
	//int T;
	//scanf("%d %d",&T);
	//hope you can see this
	//
	int t;
	
	cin>>t;
	int num=1;
	while(t--){
		int ans[]={0,0,0,0,0,0,0,0,0,0};
		string s;
		cin>>s;
		REP(i,26){flag[i]=0;}
		for(int i=0;i<s.length();i++){
			flag[s.at(i)-'A']++;
		}
		
		while(flag['Z'-'A']!=0){
			flag['Z'-'A']--;
			flag['E'-'A']--;
			flag['R'-'A']--;
			flag['O'-'A']--;
			ans[0]++;
		}
		
		while(flag['X'-'A']!=0){
			flag['X'-'A']--;
			flag['S'-'A']--;
			flag['I'-'A']--;
			ans[6]++;
		}

		while(flag['G'-'A']!=0){
			flag['G'-'A']--;
			flag['E'-'A']--;
			flag['I'-'A']--;
			flag['H'-'A']--;
			flag['T'-'A']--;
			ans[8]++;
		}

		while(flag['H'-'A']!=0){
			flag['H'-'A']--;
			flag['T'-'A']--;
			flag['R'-'A']--;
			flag['E'-'A']-=2;
			ans[3]++;
		}
		
		while(flag['W'-'A']!=0){
			flag['W'-'A']--;
			flag['T'-'A']--;
			flag['O'-'A']--;
			ans[2]++;
		}

		while(flag['U'-'A']!=0){
			flag['U'-'A']--;
			flag['F'-'A']--;
			flag['O'-'A']--;
			flag['R'-'A']--;
			ans[4]++;
		}
		while(flag['O'-'A']!=0){
			flag['O'-'A']--;
			flag['N'-'A']--;
			flag['E'-'A']--;
			ans[1]++;
		}
		while(flag['F'-'A']!=0){
			flag['I'-'A']--;
			flag['V'-'A']--;
			flag['F'-'A']--;
			flag['E'-'A']--;
			ans[5]++;
		}

		while(flag['I'-'A']!=0){
			flag['I'-'A']--;
			flag['N'-'A']-=2;
			flag['E'-'A']--;
			ans[9]++;
		}

		while(flag['S'-'A']!=0){
			flag['S'-'A']--;
			flag['E'-'A']-=2;
			flag['V'-'A']--;
			flag['N'-'A']--;
			ans[7]++;
		}
		string finAns="";
		REP(i,10){
			if(ans[i]==-1)continue;
			REP(j,ans[i]){
				finAns+=to_string(i);
			}
		}
		cout<<"Case #"<<(num)<<": "<<finAns<<endl;
		num++;
	}
	
	return 0;
}
