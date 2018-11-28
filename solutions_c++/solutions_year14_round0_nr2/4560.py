//Autor: Edwin Payrumani Mamani
//Fecha: April , 2014
//problem; Codejam 2014 A;
//#include <bits/stdc++.h>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
#include <bitset>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <stack>
#include <sstream>

using namespace std;

#define SZ(a) int((a).size())
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())n
#define pb push_back
#define mp make_pair

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,n)  FOR(i,0,n)
#define foreach(c,it) for(__typeof((c).begin())it = (c).begin();it!=(c).end(); it++)
#define CLR(a,b) memset(a,b,sizeof a)

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long LL;


int main(){

	int t;
	double C,F,X;
	cin >> t ;
	int cases = 0;
		
	while(t--){
		double times = 0.0;
		double cook = 2.0;
		double times2= 0.0;
		cases++;
		cin >> C >> F >> X;
		double ans = X/cook;
	
		while( true ){
				times = times + (C / cook);
				cook+=F;
				times2 = X/cook;
				if( times + times2 >= ans ){
					break;
				}

				ans =  times + times2;

		}
			printf("Case #%d: %.7lf\n",cases,ans);

	}	
	
	return 0;
}


