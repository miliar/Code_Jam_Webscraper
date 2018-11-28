#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <vector>

void read(std::vector< std::vector<int> > &v){
	for(int K=0; K<v.size(); ++K)
		for(int L=0; L<v[K].size(); ++L)
			std::cin>>v[K][L];
}

void magia(std::vector<int> a, std::vector<int> b){
	std::sort(a.begin(), a.end());
	std::sort(b.begin(), b.end());

	std::vector<int> c;

	std::set_intersection( a.begin(), a.end(), b.begin(), b.end(), std::back_inserter(c) );

	if(c.empty())
		std::cout << "Volunteer cheated!";
	else if(c.size()==1)
		std::cout << c[0];
	else
		std::cout << "Bad magician!";
}

int main(){
	int casos;
	std::cin >> casos;
	std::vector< std::vector<int> >
		first(4, std::vector<int>(4)),
		second(4, std::vector<int>(4));
	for(int K=1; K<=casos; ++K){
		int first_row, second_row;
		std::cin >> first_row;
		read(first);
		std::cin >> second_row;
		read(second);
		std::cout << "Case #" << K << ": ";
		magia(first[first_row-1], second[second_row-1]);
		std::cout << '\n';
	}
}
