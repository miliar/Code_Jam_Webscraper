#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define inf 2000000005
#define mod 1000000007
#define ll long long int 
#define PI 3.1415926535897932384626433832795
#define one(mask,i) ((mask>>i)&1)
#define FILENAME ""
using namespace std;
int test,ot;
double c,f,x,per,res,d[200000],b[200000];
int main(){
//	freopen(FILENAME".in","r",stdin);
//	freopen(FILENAME".out","w",stdout);
	scanf("%d",&test);
	ot = test;
	while(test){

	scanf("%lf%lf%lf",&c,&f,&x);
	res = 0.0;
	per = 2.0;
	d[0] = x / per;
	int i = 0;
	do{
		i++;
		d[i] = c / per + x / (per + f) + b[i-1];
		b[i] = c / per + b[i-1];
		per += f;
	}while(d[i] < d[i-1]);
	printf("Case #%d: %.7lf\n",ot - test + 1,d[i-1]);	

	test--;
	}
	return 0;
}







