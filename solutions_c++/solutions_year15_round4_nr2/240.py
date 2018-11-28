#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

struct tap{
	double v,x;
};

const double tol = 1e-9;
int T, u, N;
double V,X;
tap v[110];

int comp(double a, double b){
	if(a+tol < b) return -1;
	if(b+tol < a) return 1;
	return 0;
}

int compara(tap a, tap b){
	return a.x < b.x;
}

bool frio(double t){
	double volume = 0;
	double temperatura = 0;
	for(int i=0; i<N; i++){
		double dVolume = v[i].v * t;
		if(comp(volume+dVolume, V)<0){
			temperatura = (temperatura*volume + dVolume*v[i].x)/(volume+dVolume);
			volume += dVolume;
		}
		else {
			dVolume = V-volume;
			temperatura = (temperatura*volume + dVolume*v[i].x)/(volume+dVolume);
			volume += dVolume;
			return comp(temperatura,X)<=0;
		}
	}
	return false;
}

bool quente(double t){
	double volume = 0;
	double temperatura = 0;
	for(int i=N-1; i>=0; i--){
		double dVolume = v[i].v * t;
		if(comp(volume+dVolume, V)<0){
			temperatura = (temperatura*volume + dVolume*v[i].x)/(volume+dVolume);
			volume += dVolume;
		}
		else {
			dVolume = V-volume;
			temperatura = (temperatura*volume + dVolume*v[i].x)/(volume+dVolume);
			volume += dVolume;
			return comp(temperatura,X)>=0;
		}
	}
	return false;
}

double bb(double low, double high){
	double mid;
	while(high-low > 1e-9){
		mid=(low+high)/2;
		if(frio(mid) && quente(mid)){
			high = mid;
		}
		else{
			low = mid;
		}
	}
	return (low+high)/2;
}

int main(){
	scanf(" %d", &T);
	u = 0;
	while(u<T){
		u++;
		scanf(" %d %lf %lf", &N, &V, &X);
		for(int i=0; i<N; i++){
			scanf(" %lf %lf", &v[i].v, &v[i].x);
		}
		sort(v,v+N,compara);
		
		if(comp(v[0].x,X) > 0 || comp(v[N-1].x,X) < 0) printf("Case #%d: IMPOSSIBLE\n", u);
		else{
			double vl = 0;
			double temp = 0;
			for(int i=0; i<N; i++){
				temp = (temp*vl + v[i].v*v[i].x)/(vl+v[i].v);
				vl+=v[i].v;
			}
			if(comp(temp,X)==0) printf("Case #%d: %.9lf\n", u, V/vl);
			else if(comp(temp,X)>0){
				//tenho mais vazao quente
				vl = 0;
				temp = 0;
				for(int i=0; i<N; i++){
					if( comp((temp*vl + v[i].v*v[i].x)/(vl+v[i].v),X) < 0){
						temp = (temp*vl + v[i].v*v[i].x)/(vl+v[i].v);
						vl+=v[i].v;
					}
					else if( comp((temp*vl + v[i].v*v[i].x)/(vl+v[i].v),X) == 0){
						vl+=v[i].v;
						break;
					}
					else{
						vl += vl*(X-temp)/(v[i].x-X);
						break;
					}
				}
				printf("Case #%d: %.9lf\n", u, V/vl);
			}
			else{
				//tenho mais vazao fria
				vl = 0;
				temp = 0;
				for(int i=N-1; i>=0; i--){
					if( comp((temp*vl + v[i].v*v[i].x)/(vl+v[i].v),X) > 0){
						temp = (temp*vl + v[i].v*v[i].x)/(vl+v[i].v);
						vl+=v[i].v;
					}
					else if( comp((temp*vl + v[i].v*v[i].x)/(vl+v[i].v),X) == 0){
						vl+=v[i].v;
						break;
					}
					else{
						vl += vl*(X-temp)/(v[i].x-X);
						break;
					}
				}
				printf("Case #%d: %.9lf\n", u, V/vl);
			}
		}
	}
	return 0;
}
