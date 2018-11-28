#include <iostream>
#include <iomanip>

int main(void)
{
	
	const double cps0 = 2.0;
	
	unsigned int tc = 0;
	std::cin >> tc;
	
	for(unsigned int i=0; i<tc; i++)
	{
		double farm_cost=0.0, farm_extra=0.0, goal=0.0;
		
		std::cin >> farm_cost >> farm_extra >> goal;
		
		double cps = cps0;
		double ls = 0.0, lfs = 0.0, ps = 0.0;
		
		while(1)
		{
			ls = ps + goal / cps;
			lfs = ps + farm_cost / cps + goal / (cps + farm_extra);
			
			if(ls < lfs)	// no more construct farm
				break;
			else			// construct 1 more farm
			{
				ps += farm_cost / cps;
				cps += farm_extra;
			}
		}
		
		std::cout << std::fixed << std::setprecision(7) << "Case #" << i+1 << ": " << ls << std::endl;
	}
	
	return 0;
}