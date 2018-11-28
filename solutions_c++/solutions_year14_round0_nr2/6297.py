#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <set>

using namespace std;

#define all(c) (c).begin(),(c).end() 
#define sz(c) int((c).size())
#define pb push_back
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define rep(i,x,y) for(int i = x; i < y; i++)

typedef long long int LL;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii;
typedef vector<ii> vii;

int main()
{
	int t;
	scanf("%d",&t);
	rep(it,1,t+1){
		double c,f,x,fi = 1,se = 0,sum = 0,rate=2;
		scanf("%lf%lf%lf",&c,&f,&x);
		while(fi > se){
			fi = x / rate;
			se = c / rate + x / (rate+f);
			sum += fi > se ? c/rate : fi;
			rate += f;
		}
		printf("Case #%d: %.7lf\n",it,sum);
	}
	return 0;
}