#include <fstream>
#include <iostream>
#include <algorithm>
using namespace std;

//#define f cin
//#define g cout
ifstream f("A-small-attempt0.in"); ofstream g("A-small-attempt0.out");

const int nmod = 1000002013;

int i, j, n, m, k, x, y, z, t, u, top;
long long sum1, sum2;
int v[111111], times[1111];
int in[11111], out[1111];

int main(){
	f>>t;
	for (int ii=1; ii<=t; ii++){
		f>>n>>m;
		for (i=1; i<=n; i++) v[i]=in[i]=out[i]=times[i]=top=sum1=sum2=0;
		for (i=1; i<=m; i++){
			f>>x>>y>>z;
			u = n-(y-x);
			sum1 += (((n*(n+1)) - (u*(u+1)))/2)*z;
			sum1 %= nmod;
			in[x]+=z;
			out[y]+=z;
		}
		for (i=1; i<=n; i++){
			for (j=1; j<=top; j++) v[j]--;
			if (in[i]) {
				v[++top] = n;
				times[top] = in[i];
			}
			while (out[i]){
				x = min(times[top], out[i]);
				out[i]-=x;
				times[top] -= x;
				if (!times[top]) top--;
			}
			for (j=1; j<=top; j++){
				sum2+=v[j]*times[j];
			}
			sum2 %=nmod;
		}
		
		sum1-=sum2;
		while (sum1<0) sum1+=nmod;
		
		g<<"Case #"<<ii<<": "<<sum1<<"\n";
	}
}
