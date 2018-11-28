#include <iostream>
#include <algorithm>
#include <vector>
#include <set>


template<typename S>
S union_sets(const S& s1, const S& s2)
{
     S result = s1;

     result.insert(s2.cbegin(), s2.cend());

     return result;
}

void run_test()
{
	int r0, r1;
	int c0[16], c1[16];

	std::cin >> r0; r0--;
	for(int i = 0; i < 16; i++)
		std::cin >> c0[i];

	std::cin >> r1; r1--;
	for(int i = 0; i < 16; i++)
		std::cin >> c1[i];

	std::set<int> s0(c0 + r0*4, c0+r0*4+4);
	std::set<int> s1(c1 + r1*4, c1+r1*4+4);

	std::vector<int> s2;
	std::set_intersection(s0.begin(), s0.end(), s1.begin(), s1.end(), std::back_inserter(s2));

	switch(s2.size())
	{
	case 0: std::cout << "Volunteer cheated!\n";break;
	case 1: std::cout << s2[0] << "\n";break;
	default: std::cout << "Bad magician!\n";break;
	}
}

int main()
{
	int count;
	std::cin >> count;
	for(int i = 0; i < count; i++)
	{
		std::cout << "Case #" << i+1 << ": ";
		run_test();
	}
}
