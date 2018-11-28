#include <cstdio>

int main() {
	double c,f,x,t,v,go,farm;
	int T;
	scanf("%d",&T);
	for(int z=1;z<=T;z++) {
		scanf("%lf%lf%lf",&c,&f,&x);
		t = 0;
		v = 2;
		go = x/v;
		farm = c/v + x/(v+f);
		while(go > farm) {
			t += c/v;
			v += f;
			go = x/v;
			farm = c/v + x/(v+f);
		}
		t += go;
		printf("Case #%d: %.7lf\n",z,t);
	}
	return 0;
}
			
		
