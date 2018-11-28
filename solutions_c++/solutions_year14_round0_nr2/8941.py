#include <stdio.h>
#include <vector>
using namespace std;

int main() {
	unsigned int t;
	double c, f, x;
	scanf("%d\n", &t);
	for (int i = 0; i < t; ++i) {
		scanf("%lf %lf %lf\n", &c, &f, &x);
		vector<double> time_to_farm;
		vector<double> time_to_farm_end;
		double cookies_per_sec = 2;
		time_to_farm.push_back(0);
		time_to_farm_end.push_back(x/cookies_per_sec);
		while(true) {
			//Lo que tarde hasta llegar acá (tardo en llegar a la granja anterior) + (tardo en llegar a esta granja)
			time_to_farm.push_back(c/cookies_per_sec + time_to_farm[time_to_farm.size()-1]);
			//Asumo que tomé la fábrica, aumento la producción y calculo cuanto tardo
			cookies_per_sec += f;
			//Lo que tardo en ganar es lo que tardo en conseguir las x galletitas + lo que tardo en llegar a la granja donde estoy
			time_to_farm_end.push_back((x/cookies_per_sec) + time_to_farm[time_to_farm.size()-1]);
			if(time_to_farm_end[time_to_farm_end.size()-2] < time_to_farm_end[time_to_farm_end.size()-1]) {
				break;
			}
		}
		double min = time_to_farm_end[0];
		for (unsigned int j = 1; j < time_to_farm_end.size(); ++j) {
			if(min > time_to_farm_end[j]) {
				min = time_to_farm_end[j];
			}
		}
		printf("Case #%d: %.7lf\n", i+1, min);
	}

}