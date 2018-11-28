#include<cstdio>

int main(){
	int q_casos;
	scanf("%d", &q_casos);
	for(int i=0; i < q_casos; i++){
		double c, f, x, r, cookies;
		scanf("%lf %lf %lf", &c, &f, &x);
		r = 2;
		double time = 0;
		cookies = 0;
		while(true){
			double cp = c/r;
			double pa = cp + x/(r+f);
			double pb = x/r;
			if(pa < pb){
				time += cp;
				r += f;
			}
			else{
				time += pb;
				//cookies += r*time;
				break;
			}
		}
		printf("Case #%d: %.7lf\n",i+1, time);
	}
	return 0;
}
