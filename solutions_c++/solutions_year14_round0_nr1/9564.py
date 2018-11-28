// Problem A. Magic Trick 

#include <iostream>    
#include <algorithm>		
#include <vector>

#define ROW_SIZE 4
#define BOARD_SIZE 16

int
main ()
{
	std::ios_base::sync_with_stdio(false);
	
    int test_cases;

	std::cin >> test_cases;

	// std::cout << "test_cases=" << test_cases << std::endl;
	
	// while (test_cases--) {
	for (int i(0); i < test_cases; ++i) {
	
		int answer1;
		std::cin >> answer1;
		// std::cout << "answer1=" << answer1 << std::endl;

		std::vector<int> arrangement1;
		arrangement1.reserve(BOARD_SIZE);
		
		for (int i(0); i < BOARD_SIZE; ++i)
			std::cin >> arrangement1[i];
			
		// std::cout << "arrangement1 below:" << std::endl;
		// for (int i(0); i < BOARD_SIZE; ++i)
			// std::cout << arrangement1[i] << " ";
		// std::cout  << std::endl;
			
		int answer2;
		std::cin >> answer2;
		// std::cout << "answer2=" << answer2 << std::endl;

		std::vector<int> arrangement2;
		arrangement2.reserve(BOARD_SIZE);
		
		for (int i(0); i < BOARD_SIZE; ++i)
			std::cin >> arrangement2[i];		

		// std::cout << "arrangement2 below:" << std::endl;
		// for (int i(0); i < BOARD_SIZE; ++i)
			// std::cout << arrangement2[i] << " ";
		// std::cout  << std::endl;
		
		std::vector<int>::iterator arrangement1_begin_it(arrangement1.begin() + ((--answer1)*ROW_SIZE)), arrangement1_end_it(arrangement1_begin_it + ROW_SIZE);
		std::vector<int>::iterator arrangement2_begin_it(arrangement2.begin() + ((--answer2)*ROW_SIZE)), arrangement2_end_it(arrangement2_begin_it + ROW_SIZE);
		
		std::sort (arrangement1_begin_it, arrangement1_end_it);
		std::sort (arrangement2_begin_it, arrangement2_end_it);

		// std::cout << "arrangement1 SORTED below:" << std::endl;
		// for (int i(0); i < BOARD_SIZE; ++i)
			// std::cout << arrangement1[i] << " ";
		// std::cout  << std::endl;
		
		// std::cout << "arrangement2 SORTED below:" << std::endl;
		// for (int i(0); i < BOARD_SIZE; ++i)
			// std::cout << arrangement2[i] << " ";
		// std::cout  << std::endl;
		
		std::vector<int> arrangement_intersection;
		arrangement_intersection.reserve(ROW_SIZE);
		
		std::vector<int>::const_iterator it;

		it = std::set_intersection (arrangement1_begin_it, arrangement1_end_it, arrangement2_begin_it, arrangement2_end_it, arrangement_intersection.begin());
		
		std::cout << "Case #" << (i+1) << ": ";
		
		// std::cout << "COMMON ELEMENTS" << (it-arrangement_intersection.begin()) << std::endl;
		// std::cout << arrangement_intersection.size() << std::endl;
		switch(it-arrangement_intersection.begin()) {
			case 0:std::cout << "Volunteer cheated!" << std::endl;break;
			case 1:std::cout << arrangement_intersection[0] << std::endl;break;
			default:std::cout << "Bad magician!" << std::endl;
		}
			
	}
	
	return 0;
}
