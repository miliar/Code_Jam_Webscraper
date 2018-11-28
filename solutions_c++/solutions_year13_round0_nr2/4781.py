#include <fstream>
using namespace std;

ifstream fi("in.in");
ofstream fo("out.out");

long ok,n,m,j,t,i,k,a[101][101],c[101],b[101][101];

long next(){
	for (long i=100; i; i--) if (c[i]) {c[i]=0; return i;} return 0;
}

void cut(long x,long y,long k){
	int b1=1,b2=1;
	for (long i=1; i<=n; i++) if ((a[i][y]>k)) {b1=0; break;}
	for (long i=1; i<=m; i++) if ((a[x][i]>k)) {b2=0; break;}
	if ((!b1)&&(!b2)) ok=0;
	if (b1) for (long i=1; i<=n; i++) b[i][y]=k;
	if (b2) for (long i=1; i<=m; i++) b[x][i]=k;
}

void afis(){
	for (long i=1; i<=n; i++){
		for (long j=1; j<=n; j++)
			fo << b[i][j] << " ";
		fo << "\n";
	}
}

void check(){
	long x=next();
	while (x){
		for (long i=1; i<=n; i++)
			for (long j=1; j<=m; j++){
				if ((a[i][j]==x)&&(b[i][j]!=x)) cut(i,j,x);
				if (!ok) {fo << "Case #" << k << ": NO\n"; return;}
			}
		x=next();
	}	
	fo << "Case #" << k << ": YES\n";
}



int main(){
	
	fi >> t;
	for (k=1; k<=t; k++){
		ok=1;
		fi >> n >> m;
			for (long i=1; i<=n; i++)for (long j=1; j<=m; j++)fi >> a[i][j],c[a[i][j]]=1;
		check();
	}
	
	
	
	return 0;
}
