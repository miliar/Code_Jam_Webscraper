#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <string.h>
#include <numeric>
using namespace std;

 typedef vector<int> vi; 
 typedef vector<vi> vvi; 
 typedef pair<int,int> ii; 
 typedef long long ll;
 #define sz(a) int((a).size()) 
 #define pb push_back 
 #define all(c) (c).begin(),(c).end() 
 #define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
 #define present(c,x) ((c).find(x) != (c).end()) 
 #define cpresent(c,x) (find(all(c),x) != (c).end()) 

double C,F,X;

double calc (double R , double D)
{
	return D/R;
}

double solve (double R)
{
	//cout << R << endl;
	double cur = X/R;
	double next = C/R + X/(R+F);
	
	if (cur < next) return cur;
	return (C/R) + solve(R+F);
}

int main ()
{
	freopen("cookie.in","r",stdin);
	freopen("cookie.out","w",stdout);
	
	int TC;
	cin >> TC;
	int CC=1;
	while (TC--)
	{
		cin >> C >> F >> X;
		printf("Case #%d: %.7lf\n",CC++,solve(2.0));
	}
}
