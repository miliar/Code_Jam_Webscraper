#include <cmath>
#include <ctime>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <functional>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#define MAXN 1000005
#define inf 1e8
#define eps 1e-8
#define zero(x) (((x)>0?(x):-(x))<eps)
using namespace std;
typedef __int64 ll;
int main(){
	int ncase;
	double c, f, x;
	int id=0;
	cin>>ncase;
	while(ncase--){
		scanf("%lf%lf%lf", &c, &f, &x);
		id++;
		double cur=2.0;
		double sum=0;
		double cnt=0;
		double buyfarm, goon;
		while(true){
			buyfarm = c/cur+x/(cur+f);
			goon = x/cur;
			if(goon < buyfarm){
				sum+=goon;break;
			}
			sum+=c/cur;
			cur += f;
		}
		//sum+=x/cur;
		printf("Case #%d: %.7lf\n", id, sum);
	}
}