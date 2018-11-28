#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <cmath>
#include <deque>
#include <stack>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <ctime>

using namespace std;

#define maxn 110
#define datat int
#define ansdatat int

int n;

double c,f,x;

void init_deal(){
}

int main(){
	
	int tttt;
	scanf("%d", &tttt);
	for(int ttt = 1;ttt<=tttt;ttt++){

		scanf("%lf%lf%lf", &c, &f, &x);

		double speed = 2, sum = 0, t = 0, ans = x/speed;

		while(true)
		{
			double tmp_t = c/speed;

			t+=tmp_t;
			speed+=f;

			if(ans > t+x/speed){
			   ans = t+x/speed;
			}
			else{
				break;
			}
		}


		printf("Case #%d: ",ttt);
		printf("%.7lf\n", ans);

	}
	

	return 0;
};

