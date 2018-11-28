#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cctype>
#include <fstream>
using namespace std;

#define lowbit(x) ((x)&(-(x)))
#define sqr(x) ((x)*(x))
#define PB push_back
#define MP make_pair

double a[300],b[300];
double f[300][300];
int n,k;

double calc(){
	// for (int i=0;i<k;i++) printf("%.3f ",b[i]);printf("\n");
	memset(f,0,sizeof(f));
	f[0][0]=1;
	for (int i=0;i<k;i++)
		for (int j=0;j<=i;j++){
			f[i+1][j]+=f[i][j]*b[i];
			f[i+1][j+1]+=f[i][j]*(1-b[i]);
		}
	return f[k][k/2];
}

double getans(){
	scanf("%d%d",&n,&k);
	for (int i=0;i<n;i++)
		scanf("%lf",&a[i]);
	sort(a,a+n);
	double res=0;
	for (int i=0;i<=k;i++){
		for (int q=0;q<i;q++) b[q]=a[q];
		for (int q=i;q<k;q++)
			b[q]=a[n-k+q];
		res=max(res,calc());
	}
	return res;
}

int main(int argc,char ** argv){
	int T;
	scanf("%d",&T);
	for (int t=1;t<=T;t++){
		printf("Case #%d: %.10f\n",t,getans());
	}
	return 0;
}