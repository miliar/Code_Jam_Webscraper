#include <cstdio>
#include <math.h>
using namespace std;

void make() {
	int i;
	double c,f,x;
	int Xmax=100000;
    scanf("%lf",&c);
	scanf("%lf",&f);
	scanf("%lf",&x);

	double m[Xmax];
	double min=Xmax;
	
	for (int i=0;i<Xmax;++i) {
		m[i]=0;
	}
	for (i=1;i<(int)(x);++i) {
		m[i] = m[i-1]+c/(2.0+f*(i-1));
	}
	for (i=0;i<(int)(x);++i) {
	
		m[i] += x/(2.0+f*(i));
    }
	
	for (int i=0;i<(int)x;++i) {
		if (m[i]<min) min=m[i];
	}
    printf("%.7f\n",min);
    return;
}

int main() {
	int counter = 0;
    int t; scanf("%d", &t);
    while(t--) {
		printf("Case #%d: ", ++counter);
        make();
    }
    return 0;
}
