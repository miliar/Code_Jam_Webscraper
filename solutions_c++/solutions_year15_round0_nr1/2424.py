#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>
#include <numeric>
#include <algorithm>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define pb push_back
#define sz(v) ((int)(v).size())


int main(){
	int run, runs;
	scanf("%d",&runs);
	for(run=1;run<=runs;run++){
		int n; char s[10000];
		scanf("%d %s",&n,s);
		int extra=0;
		int have=0;
		for(int i=0;i<=n;i++){
			extra+=max(0,i-have);
			have+=max(0,i-have);
			have+=s[i]-'0';
		}
		printf("Case #%d: %d\n",run,extra);
	}

}
