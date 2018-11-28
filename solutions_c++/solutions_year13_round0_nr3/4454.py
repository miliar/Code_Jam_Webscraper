#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <cmath>
bool isFair(int a)
{
	if((int)(sqrt(a)*1000000)%1000000 != 0)
		return false;
	std::string front = std::to_string(a);
	std::string back = front;
	reverse(front.begin(), front.end());
	if(back != front)
		return false;
	int b = sqrt(a);
	front = std::to_string(b);
	back = front;
	reverse(front.begin(), front.end());
	if(back!= front)
		return false;
	return true;
}

int main()
{
	std::ifstream fin;
	fin.open("C-small-attempt0.in");
	if(fin.fail())
	{
		std::cout << "Fail..." << std::endl;
		return 0;
	}
	int num;
	fin >> num;
	//std::cin >> num;
	std::ofstream fout("C-small-attempt0.out");
	for(int i = 0; i < num; i++)
	{
		int min, max;
		fin >> min;
		fin >> max;
		int total = 0;
		for(int i = min; i <= max; i++)
		{
			if(isFair(i))
				total++;
		}
		
		
		
		fout <<"Case #"<< i+1 << ": " << total << std::endl;
		
	}
	fout.close();
	return 0;
}