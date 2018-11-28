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
const int maxn=100009;

#define assert(x) { cerr  << #x << ": "<< (x) << endl;}
#define SP system("pause")


int main()
{

	int tc,TC=0;

	double C,F,X;
	cin >>tc;
	while (tc--){
		cin >> C >> F >> X;
		double best=-1.0;
		bool upd=true;
		double f=2.0,tot=0;
		while (upd){
			double t=X/f+tot;
			if (t-best<EPS || best==-1.0){
				best=t;
				upd=true;
			}else upd=false;
			tot+=C/f;
			f+=F;
			
		}
		printf("Case #%d: %.7lf\n",++TC,best);
	}
	return 0;

}