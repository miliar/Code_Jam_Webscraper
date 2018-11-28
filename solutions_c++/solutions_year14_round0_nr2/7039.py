/*
 GCJ 2014 Qual B 
 Saurav Shekhar
 */
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <bitset>

using namespace std;
#define EPS 1e-6
#define INF 2000000000
#define P 1000000009
typedef unsigned int ui;
typedef unsigned long long llu; //I64d
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;

const ui LIM = 100005; 
const ui LF = 2000;
double C,F,X;

double caltime(ui f )
{
	double ans = 0.0;
	double speed = 2.0;
	for(ui i=0; i<f; i++) {
		ans = ans + C / speed;
		speed = speed + F;
	}
	speed += F;
	ans += X / speed;

	return ans;
}

int main()
{
  ui T;
  scanf("%u",&T);

  for(ui qq=1; qq<=T; qq++) {
  	cin >> C >> F >> X;
	double speed = 2.0 ;
	
	
	double ti;
	double prevtime = X / speed;
	double nexttime;
	double ctime = C / speed;
	
	nexttime = ctime + X / (speed + F);

	while(islessequal(nexttime, prevtime)) {
		speed += F;
		ctime += C / speed;
		prevtime = nexttime;
		nexttime = ctime + X / (speed + F);
	}
	

	printf("Case #%d: %.7lf\n", qq, prevtime);
	
		
  }

  return 0;
}




















