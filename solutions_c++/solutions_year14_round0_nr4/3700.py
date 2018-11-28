#include <iostream>
#include <algorithm>
#include <list>
int main()
{

	int test;
	std::cin >> test;
	int N;
	std::list<double> naomi;
	std::list<double> ken;

	std::list<double> naomiCopy;
	std::list<double> kenCopy;
	
	for(int i = 1 ; i <= test; i++)
	{
		std::cin >> N;
		
		naomi.clear();
		ken.clear();
		
		int pointWar = 0;
		int pointDecWar = 0;
		for(int j = 0 ; j < N ; j++)
		{
			double t;
			std::cin >> t;
			naomi.push_back(t);
		}
		
				
		for(int j = 0 ; j < N ; j++)
		{
			double t;
			std::cin >> t;
			ken.push_back(t);
		}
		
		
		naomi.sort();
		naomi.reverse();
		
		ken.sort();
		ken.reverse();
		
		naomiCopy.clear();
		naomiCopy = std::list<double>(naomi);
		
		kenCopy.clear();
		kenCopy = std::list<double>(ken);
		
		std::cout << "Case #" << i << ": ";
		while(naomi.empty()!=true)
		{
			
			double num = naomi.front();
			naomi.erase(naomi.begin());
			for(std::list<double>::iterator it = ken.begin() ; it!=ken.end() ; ++it)
			{	
				if(num > (*it))
				{
					ken.erase(it);
					break;
				}
			}
		}	
		
		std::cout << N-ken.size() << " ";
	
		
		while(kenCopy.empty()!=true)
		{
			
			double num = kenCopy.front();
			kenCopy.erase(kenCopy.begin());
			for(std::list<double>::iterator it = naomiCopy.begin() ; it!=naomiCopy.end() ; ++it)
			{	
				if(num > (*it))
				{
					naomiCopy.erase(it);
					break;
				}
			}
		}

		
		std::cout << naomiCopy.size() << std::endl;
			
	}
	
	
	return 12;
}
