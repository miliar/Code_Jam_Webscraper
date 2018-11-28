#include <stdio.h>
#include <string.h>
#include <stdlib.h>

double c, f, x;

int cmp ( const void *a , const void *b ){
	return *(int *)a - *(int *)b;
}

double min(double a, double b){return a<b?a:b;}

double calc(int in){
	int i;
	double time = 0.0;
	for(i=0; i<in; i++){
		time += c/(i*f+2);	
	}
	time += x/(i*f+2);
	return time;
}

int main(){

  freopen("B-large.in", "r", stdin);
  freopen("test.txt", "w", stdout);
	
//	qsort(map,n,sizeof(map[0]),cmp);
//	memset(map,0,sizeof(map));
	int t, i, j, tp;
	double p ,ans;
	scanf("%d", &t);
	for(i=0; i<t; i++){
		scanf("%lf %lf %lf", &c, &f, &x);
		p = (x*f-c*f-2*c)/(c*f);
		printf("Case #%d: ", i+1);
		
		if(p < 0){
			printf("%.7lf\n",x/2);
		}else{
			tp = (int)p;
			ans =  min(calc(tp), calc(tp+1));
			printf("%.7lf\n",ans);
		}
	}
	return 0;
}