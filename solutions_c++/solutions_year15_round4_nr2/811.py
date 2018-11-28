#include <iostream>
#include <cstdio>
using namespace std;

double volume,temp;
double v[10],t[10];
int n;

double ans() {
	if (n==1) {
		if (t[1]==temp) return volume/v[1];
		else return -10;
	}
	if (t[1]>temp && t[2] > temp) return -10;
	if (t[1]<temp && t[2] < temp) return -10;
	
	
	if (t[1]!=temp && t[2] == temp) return volume/v[2];
	if (t[1]==temp && t[2] != temp) return volume/v[1];
	if (t[1]==temp && t[2] == temp) return volume/(v[1]+v[2]);
	
	double v1 = v[1]; double v2 = (temp*v1-t[1]*v1)/(t[2]-temp);
	double ido1=1; double ido2 = v2 / v[2];
	
	//cout << t[1] << endl;
	//cout << t[2] << endl;
	
	double k = volume / (ido1*v[1]+ido2*v[2]);
	
	
	//cout << k;
	
	double z1 = ido1*k; double z2 = ido2*k;
	if (z1 > z2) return z1; return z2;
}


int main()
{
	int db; scanf("%d", &db);
	for (int iii = 1; iii<=db; iii++) {
		scanf("%d ", &n);
		scanf("%lf %lf\n", &volume, &temp);
		
		for (int j = 1; j<=n; j++) {
		scanf("%lf %lf\n", &v[j], &t[j]);
		}
		
		//printf("%d %.10f\n", iii, volume);
		
		double re = ans();
		
		if (re < -1) printf("Case #%d: IMPOSSIBLE\n", iii);
		else printf("Case #%d: %.10f\n", iii, re);
		//else cout << "Case #" << iii << ": " << re << endl;
		
	}
    return 0;
}
