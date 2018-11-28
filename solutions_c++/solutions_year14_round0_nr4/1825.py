#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <math.h>
#include <cstdio>
using namespace std;

int main() {
	int T = 0;
	scanf("%d", &T);
	int k = 1;
	while(k <= T) {
		int N = 0;
		scanf("%d", &N);
		vector<double> naomi (N);
		vector<double> ken (N);
		for(int i = 0; i < N; i++) {
			scanf("%lf", &naomi[i]);
		}
		for(int i = 0; i < N; i++) {
			scanf("%lf", &ken[i]);
		}
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		
		int y = 0;
		vector<bool> ytaken(N, false);
		for(int i = 0; i < N; i++) {
			double t = naomi[i];
			bool pass = false;
			for(int j = 0; j < N; j++) {
				if(!ytaken[j]) {
					if(ken[j] < t) {
						y++;
						pass = true;
						ytaken[j] = true;
					}
					break;
				}
			}
			if(!pass) {
				for(int j = N-1; j > -1; j--) {
					if(!ytaken[j]) {
						ytaken[j] = true;
						break;
					}
				}
			}
		}
		
		int z = 0;
		vector<bool> taken(N, false);
		for(int i = 0; i < N; i++) {
			double t = naomi[i];
			bool pass = false;
			for(int j = 0; j < N; j++) {
				if(!taken[j]) {
					if(ken[j] > t) {
						taken[j] = true;
						z++;
						pass = true;
						break;
					}
				}
			}
			if(!pass) {
				for(int j = 0; j < N; j++) {
					if(!taken[j]) {
						taken[j] = true;
						break;
					}
				}
			}
		}
		z = N - z;
		
		printf("Case #%d: %d %d\n", k, y, z);
		k++;
	}
	return 0;
}