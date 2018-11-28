#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <vector>

typedef long double number;

std::vector<number>
read(int n){
	std::vector<number> v(n);
	for(int K=0; K<n; ++K)
		std::cin >> v[K];
	return v;
}

#if 1
int deceitful( const std::vector<number> &ken, const std::vector<number> &naomi ){
	typedef std::vector<number>::const_iterator iterator;
	iterator
		k = ken.begin(),
		n = std::upper_bound(naomi.begin(), naomi.end(), *k);

	while(k not_eq ken.end() and n not_eq naomi.end()){
		++k;
		n = std::upper_bound(n+1, naomi.end(), *k);
	}
	return std::distance(ken.begin(), k);
}
#endif

#if 0
int deceitful( const std::vector<number> &ken, const std::vector<number> &naomi ){
	typedef std::vector<number>::const_iterator iterator;
	iterator
		ka = std::upper_bound(ken.begin(), ken.end(), *naomi.rbegin()),
		kb = ken.end(),
		na = naomi.begin(),
		nb = std::upper_bound(naomi.begin(), naomi.end(), ken[0]);
	
	return
		ken.size()
		- std::max(
			std::distance(na, nb),
			std::distance(ka, kb)
		);
}
#endif

#if 0
int deceitful2( const std::vector<number> &ken, const std::vector<number> &naomi ){
	typedef std::vector<number>::const_iterator iterator;
	iterator 
		ka = std::upper_bound( ken.begin(), ken.end(), naomi[0] ),
		kb = ken.end(),
		na = naomi.begin(),
		nb = std::upper_bound( naomi.begin(), naomi.end(), *ken.rbegin() );

	return std::min(
		std::distance(ka,kb),
		std::distance(na,nb)
	);
}
#endif

int normal( const std::vector<number> &ken, const std::vector<number> &naomi ){
	typedef std::vector<number>::const_iterator iterator;
	iterator 
		n = naomi.begin(),
		k = std::upper_bound(ken.begin(), ken.end(), *n);
	
	while(k not_eq ken.end() and n not_eq naomi.end()){
		++n;
		k = std::upper_bound(k+1, ken.end(), *n);
	}
	return std::distance(n, naomi.end());
}

void magia( std::vector<number> &ken, std::vector<number> &naomi ){
	std::sort(ken.begin(), ken.end());
	std::sort(naomi.begin(), naomi.end());

	std::cout << deceitful(ken, naomi) << ' ';
	std::cout << normal(ken, naomi);
}

int main(){
	int casos;
	std::cin >> casos;
	for(int K=1; K<=casos; ++K){
		int n;
		std::cin >> n;
		std::vector<number> 
			naomi = read(n),
			ken = read(n);

		std::cout << "Case #" << K << ": ";
		magia(ken, naomi);
		std::cout << '\n';
	}
}
