
#include <cassert>
#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <complex>
#include <cmath>
using namespace std;
typedef long long i64;
#define fu(i,m,n) for(int i=m; i<n; i++)
#define fr(i,m,n) for(typeof(m) i=m; i!=n; i++)
#define fa(i,c) fr(i,(c).begin(),(c).end())

typedef complex<long> P;
typedef complex<double> PD;


bool cmp(const P& x, const P& y) {
    return x.imag() < y.imag();
}

long gcd(long a, long b) {
    if(b==0) return a;
    if(a<b) swap(a,b);
    while(a>=b) a-=b;
    return gcd(b,a);
}

int main(void) {
	int T;
	cin >> T;
	for(int ts=1; ts<=T; ts++) {
		cout << "Case #" << ts << ": ";

        int N; double V,X;
        cin >> N >> V >> X;
        long iV = (long)round(V*10000);
        long iX = (long)round(X*10000);
        P target(iV, iV*iX);
        PD targetD(iV, iV*iX);
        //cout << target << endl;
        //cout << targetD << endl;

        vector<P> pools;

        fu(i,0,N) {
            double R,C;
            cin >> R >> C;
            long iR = (long)round(R*10000);
            long iC = (long)round(C*10000);
            pools.push_back(P(iR,iC));
        }

        sort(pools.begin(), pools.end(), cmp);
        fu(i,0,N) pools[i] = P(pools[i].real(), pools[i].real()*pools[i].imag());

        vector<P> vertices;
        vertices.push_back(0);
        fu(i,0,N) vertices.push_back(vertices.back() + pools[i]);

        vector<P> vertices2;
        vertices2.push_back(0);
        fu(i,0,N-1) vertices2.push_back(vertices2.back() + pools[N-i-1]);
        reverse(vertices2.begin(),vertices2.end());
        fu(i,0,N-1) vertices.push_back(vertices2[i]);

        int N2 = vertices.size();
        //fu(i,0,N2) cout << vertices[i] << " "; cout << endl;

        vector<PD> verticesD(N2);
        fu(i,0,N2) verticesD[i]=vertices[i];
        //fu(i,0,N+1) cout << vertices[i] << " "; cout << endl;

        double ret=1000000000000000.0;
        bool done=false;

        fu(i,1,N2) if(vertices[i]/__gcd(vertices[i].real(),vertices[i].imag()) == target/__gcd(target.real(),target.imag())) {
            ret = min(ret, (targetD/verticesD[i]).real());
            //cout << "A" << ret << endl;
            done=true;
        }

        if(!done) fu(i,1,N2-1) if((targetD/verticesD[i]).imag()>0 && (targetD/verticesD[i+1]).imag()<0) {
            PD a = verticesD[i+1]/targetD*abs(targetD);
            PD b = verticesD[i]/targetD*abs(targetD);
            double x = (-a.real() * b.imag() + b.real() * a.imag()) / (a.imag()-b.imag());
            ret = abs(targetD)/x;
            //cout << "B" << x << a.imag() << " " << b.imag() << " " << a << " " << b << " " << ret << endl;
            //cout << verticesD[i] << " " << verticesD[i+1] << endl;
            done = true;
        }

        if(!done) cout << "IMPOSSIBLE" << endl;
        else printf("%.8lf\n", ret);
	}
}
