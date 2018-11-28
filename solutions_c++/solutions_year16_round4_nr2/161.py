#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

void proc()
{
	int N,K;
	scanf ("%d %d",&N,&K);
	vector<double> a,o;
	for (int i=0;i<N;i++){
		double p; scanf ("%lf",&p);
		a.push_back(p);
	}
	sort(a.begin(),a.end());
	o = a;
	double ans = 0;
	for (int s=0;s<=K;s++){
		a = o;
		while (a.size() > K){
			a.erase(a.begin()+s);
		}

		double u[202][202] = {0,};
		u[0][0] = 1;
		for (int i=0;i<a.size();i++){
			for (int j=0;j<=i;j++){
				u[i+1][j] += u[i][j] * (1 - a[i]);
				u[i+1][j+1] += u[i][j] * a[i];
			}
		}
		if (ans < u[K][K/2])
			ans = u[K][K/2];
	}

	printf ("%.12lf\n",ans);
}

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test); for (int Case=1;Case<=Test;Case++){
		printf ("Case #%d: ",Case);
		proc();
	}

	return 0;
}