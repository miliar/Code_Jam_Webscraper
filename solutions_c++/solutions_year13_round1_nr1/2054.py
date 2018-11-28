#include <iostream>
#include <stdint.h>
using namespace std;

inline __attribute__((always_inline)) uint64_t sq(uint64_t r)
{
	return r * r;
}

void testCase(int i)
{
	cout << "Case #" << i << ": ";
	
	uint64_t totalArea = 0;
	uint64_t r, t;
	uint64_t step = 0;
	uint64_t count = 0;
	
	cin >> r >> t;
	
	step = 2 * r + 1;
	
	while (totalArea < t)
	{
		//totalArea += sq(r + step + 1) - sq(r + step);
		totalArea += step;
		step += 4;
		count++;
	}
	
	if (totalArea != t)
		count --;
	cout << count;
	
	cout << endl;
}


int main()
{
	int i;
	cin >> i;
	for (int k = 1; k <= i; ++k)
		testCase(k);
}