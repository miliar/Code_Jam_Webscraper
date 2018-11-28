#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <stack>
#include <cstring>
#include <map>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
unsigned long long one = 1;

int t;
double c,f,x,a,b;
double ans,cur;

int main(){
	scanf("%d",&t);
	for (int jj=1; jj<=t; jj++){
		scanf("%lf%lf%lf",&c,&f,&x);
		a = 2.0;
		ans = 100000000;
		cur = x/a;
		b = 0;
		while (cur < ans){
			ans = cur;
			b += c/a;
			a += f;
			cur = b+(x/a);
		}
		printf("Case #%d: %.7lf\n",jj,ans);
	}
	return 0;
}
