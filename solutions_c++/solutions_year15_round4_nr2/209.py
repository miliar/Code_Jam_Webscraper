#include <stdio.h>
#include <functional>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
using namespace std;

int N; double V,X;

struct point{
	point(long long x_, long long y_, long long u_){x = x_; y = y_; u = u_;}
	long long x,y,u;
};


bool cmp(const point& a, const point& b){
	return a.u < b.u;
}

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test); for (int Case=1;Case<=Test;Case++){
		printf ("Case #%d: ",Case);

		scanf ("%d %lf %lf",&N,&V,&X);
		long long v = V * 10000 + 0.1;
		long long x = X * 10000 + 0.1;
		double p=0,u=0,n=0;
		vector<point> conv;
		conv.push_back(point(0,0,-10000000));
		for (int i=0;i<N;i++){
			double R,C; scanf ("%lf %lf",&R,&C);
			long long r = R * 10000 + 0.1;
			long long c = C * 10000 + 0.1;
			conv.push_back(point(r,r*(c-x),c-x));
		}
		sort(conv.begin(),conv.end(),cmp);
		for (int i=1;i<=N;i++){
			conv.push_back(point(-conv[i].x,-conv[i].y,conv[i].u));
		}

		double l = 0;
		for (int i=1;i<conv.size();i++){
			conv[i].x += conv[i-1].x;
			conv[i].y += conv[i-1].y;
			if (conv[i].y >= 0 && conv[i-1].y <= 0){
				double p = 0;
				if (conv[i-1].y == 0 && conv[i].y == 0) p = conv[i].x;
				else{
					p = ((0. + conv[i].x) * conv[i-1].y - (0. + conv[i-1].x) * conv[i].y) / (0. + conv[i-1].y - conv[i].y);
				}
				if (l < p) l = p;
			}
		}
		if (l < 1e-9) puts("IMPOSSIBLE");
		else printf ("%lf\n",V/l*10000);
	}

	return 0;
}