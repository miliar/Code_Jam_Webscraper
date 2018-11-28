#include <stdio.h>
#include <algorithm>
#include <set>
#include <string>
#include <vector>
#include <string.h>
#define mp make_pair
using namespace std;
#define eps 1e-12
int n;
long double volume, temp, use[101];
bool cannot_full;
struct q{
	long double rate, temp;
	bool operator() (q a, q b){
		return a.temp < b.temp;
	}
}water[101];
bool eq(long double a, long double b){
	return fabs(a - b) <= eps && fabs(a-b) <= eps * min(a,b);
}
long double check(long double time){
	for (int i = 0; i < n; i++)
		use[i] = 0;

	long double sum = 0, now_temp = 0;
	int last;
	for (int i = 0; i < n; i++){
		if (sum + water[i].rate*time > volume){
			use[i] = (volume - sum) / water[i].rate;
			now_temp += (volume - sum) * water[i].temp;
			sum = volume;
			last = i;
		}
		else{
			sum += water[i].rate*time;
			now_temp += water[i].rate*time*water[i].temp;
			use[i] = time;
		}
	}
	if (!eq(sum, volume)) return false;
	if (temp < now_temp && !eq(temp, now_temp)) return false;
	sum = 0; now_temp = 0;
	for (int i = 0; i < n; i++)
		use[i] = 0;
	for (int i = n - 1; i >= 0; i--){
		if (sum + water[i].rate*time > volume){
			now_temp += (volume - sum) * water[i].temp;
			sum = volume;
		}
		else{
			sum += water[i].rate*time;
			now_temp += water[i].rate*time*water[i].temp;
		}
	}
	if (temp > now_temp && !eq(temp,now_temp)) return false;
	return true;
}
int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testt;
	scanf("%d", &testt);
	for (int test = 1; test <= testt; test++){
		scanf("%d %lf %lf", &n, &volume, &temp);
		temp *= volume;
		for (int i = 0; i < n; i++)
			scanf("%lf %lf", &water[i].rate, &water[i].temp);
		sort(water, water + n, q());

		long double low = 0, high = 100000000, print = -100;
		while (high - low > 1e-9){
			long double mid = (low + high) / 2;
			if (check(mid)){
				print = mid;
				high = mid;
			}
			else
				low = mid;
		}
		printf("Case #%d: ", test);
		if (print < -50)
			printf("IMPOSSIBLE");
		else
			printf("%.10lf", print);
		printf("\n");
	}
	return 0;
}