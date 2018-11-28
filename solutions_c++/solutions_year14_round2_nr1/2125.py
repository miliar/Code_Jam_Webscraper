#include <iostream>
#include <algorithm>
#include <cmath>
#include <time.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <queue>
#include <utility>
#include <vector>
#include <time.h>
#include <stdio.h>
#include <list>
#include <limits> // for numeric_limits
#include <set>
#include <iterator>
#include <memory.h>

using namespace std;

#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define var(a,b)  __typeof(b) a = b
#define rep(i,n)  for(int i = 0;(i) < (n);  ++i)
#define rept(i,a,b) for(var(i,a); i < (b); ++i)
#define tr(v,it)  for(var(it,v.begin());it!=v.end();++it)
#define fill(a,val) memset(a,val,sizeof(a))
#define gi(n) scanf("%d",&n);
#define all(v) v.begin(),v.end()
#define max(a,b) a>b?a:b
#define min(a,b) a>b?b:a
#define MOD 1000000007
#define INF 99999999
#define a_max 100100
#define ll long long int
#define debug_lld(a) printf("Debug here %lld\n",a);

typedef pair<ll,ll> pll;
typedef pair<int,int > pii;
typedef pair<ll,pii>plp;

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		int n;
		cin >> n;
		string temp;

		vector<string > str;
		vector< vector<char> > ch;
		vector< vector<int> > score;

		int ans = 0;
		for(int j = 0; j<n ; ++j){
			cin >> temp;
			str.pb(temp);

			vector<char> t_ch;
			vector<int> t_in;

			t_ch.pb(temp[0]);
			int sc = 1;

			for(int k = 1; k<temp.size(); ++k){
				if(temp[k] == temp[k-1])
					sc++;
				else{
					t_in.pb(sc);
					t_ch.pb(temp[k]);
					sc = 1;
				}
			}
			t_in.pb(sc);

			ch.pb(t_ch);
			score.pb(t_in);
			t_ch.clear();
			t_in.clear();
		}

		// cout << ch.size();
		// cout << score.size();
		
		// for(int k = 0; k<n; k++)
		// {
		// 	for(int j = 0; j< ch[k].size(); j++){
		// 		cout << ch[k][j] << "->" << score[k][j] << endl;
		// 	}
		// }
		
		if(ch[0].size() == ch[1].size()){
			for(int j = 0; j<ch[0].size() ; ++j){
				if(ch[0][j] == ch[1][j]){
					ans += abs(score[0][j] - score[1][j]);
				}
				else
				{
					ans =-1;
					break;
				}
			}
		}
		else
			ans = -1;
		printf("Case #%d: ", i+1);
		if(ans == -1)
			printf("Fegla won\n");
		else
			printf("%d\n", ans);

	}
	return 0;
}