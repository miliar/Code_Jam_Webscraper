									/*ba yade oo */
//Mehrdad AP

//#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <cstring>
#include <sstream>
#include <queue>
#include <vector>
#include <stack>
#include <set>
#include <map>
#include <time.h>

using namespace std;

#define absol(x) ((x)>(0) ? (x):(-1)*(x))
#define pow2(x) ((x)*(x))
#define EPS 1e-9
#define MAX 30000
#define MOD 1000000007
#define Left(x) (2*x)
#define Right(x) ((2*(x)+1)
#define mP make_pair
#define pB push_back

//#define inRange(x,y) (x>=0 && x<N && y>=0 && y<M)

typedef long long int LL;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<int,pii> piii;

const double PI = 2.0*acos(0.0);
const int INF = 1000*1000*1000;
const int maxn=15;

#define assert(x) { cerr  << #x << ": "<< (x) << endl;}
#define SP system("pause")


bool vis[30];
string str[maxn];
int N;
LL memo[1<<12][12];

LL solve(int bt,int last)
{
	if (bt==(1<<N)-1)
		return 1;

	if (memo[bt][last]!=-1)
		return memo[bt][last];

	bool tmpvis[30];
	memset(tmpvis,false,sizeof tmpvis);
	for (int i=0;i<N;i++){
		if ( (bt & (1<<i))!=0 )
			for (int j=0;j<str[i].size();j++)
				tmpvis[str[i][j]-'a']=true;

	}

	long long int ret=0;
	for (int i=0;i<N;i++){
		if ( (bt & (1<<i))!=0) continue;

		bool can=true;
		for (int j=0;j<str[i].size() && can;j++){
			if (j!=0 && tmpvis[str[i][j]-'a']) can=false;;
			if (j==0 && tmpvis[str[i][j]-'a'] && str[last][(int)str[last].size()-1]!=str[i][0]) can=false;;
		}
		if (can)
			ret = ( ret + solve(bt | (1<<i) , i ) ) % MOD;

	}

	return memo[bt][last]=ret;

}


int main ()
{

	int TC=0,tc;
	cin >>tc;
	string s;
	while (tc--){

		cin >> N;

		bool can=true;
		
		for (int i=0;i<N;i++){
			cin >> s;
			memset(vis,false,sizeof vis);
			int j=1,sz=s.size();
			vis[s[0]-'a']=true;
			string tmpstr="";
			tmpstr+=s[0];
			while (j<sz && can){
				while (j<sz && s[j]==s[j-1])j++;
				if (j<sz){
					if (vis[s[j]-'a'])
						can=false;
					else{
						vis[s[j]-'a']=true;
						tmpstr+=s[j];
					}
					j++;
				}
			}

			str[i]=tmpstr;
		}

		printf("Case #%d: ",++TC);
		/*
		cout << endl;
		cout << can << endl;
		for (int i=0;i<N;i++)
			cout << str[i] <<" ";
		cout << endl;
		*/

		if (can==false)
			cout << 0 << endl;
		else{
			memset(memo,-1,sizeof memo);

			LL ans=0;
			for (int i=0;i<N;i++)
				ans = ( ans + solve(1<<i,i) ) % MOD;
			cout << ans << endl;
		}



	}



}