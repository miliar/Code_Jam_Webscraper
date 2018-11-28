#include <iostream>
#include <map>
#include <limits>
int findOptimal(std::map< int, int, std::greater< int > >::iterator& it, const std::map< int, int, std::greater< int > >::iterator& end, int special_minutes, int largest_cut) {
	if (it == end) {
		return largest_cut+special_minutes;
	}
    std::pair< int, int > current = *it;
    if (current.first <= largest_cut){
        return largest_cut + special_minutes;
    }
    int cuts_needed = current.first/largest_cut;
    if (current.first % largest_cut == 0) {
        --cuts_needed;
    }
	if (cuts_needed * current.second >= current.first - largest_cut){
		return current.first + special_minutes;
	}
	return findOptimal(++it, end, special_minutes + cuts_needed*current.second, largest_cut);
}

int main () {
    int T;
    std::cin >> T;

    for (int test = 1; test <= T; ++test) {
        int D;
        std::cin >> D;

        std::map< int, int, std::greater< int > > plates;
        for (int i = 0; i < D; ++i) {
        	int plate;
        	std::cin >> plate;
        	++plates[plate];
        }

        std::pair< int, int > largest = *plates.begin();
        int optimal = largest.first;
        for (int i = 2; i <= largest.first/2 + 1; ++i){
        	int possible_optimal = findOptimal(++(plates.begin()), plates.end(), largest.second*(i-1), (largest.first+(i-1))/i);
        	if (possible_optimal < optimal) {
        		optimal = possible_optimal;
        	}
        }

        std::cout << "Case #" << test << ": ";
        std::cout << optimal << std::endl;

    }

    return EXIT_SUCCESS;
}