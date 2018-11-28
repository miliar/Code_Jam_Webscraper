#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <iterator>
#include <vector>

typedef long double number;

number next(number target, number production){
	return target/production;
}

//es mejor comprar la granja
bool rinde(number cost, number farm, number target, number production){
	return 
		next(cost, production) + next(target, production+farm)
		< next(target, production);
}

int main(){
	int casos;
	std::cin >> casos;
	for(int K=1; K<=casos; ++K){
		number production = 2;
		number time = 0;
		number cost, farm, target;
		std::cin >> cost >> farm >> target;

		while( rinde(cost, farm, target, production) ){
			time += next(cost, production);
			production += farm;
		}

		std::cout << "Case #" << K << ": ";
		std::cout << std::setprecision(7) << std::fixed << time + next(target, production) << '\n';
	}
}
