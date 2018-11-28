#include <iostream>
#include <vector>
#include <string>
#include <fstream>
void print(std::vector<std::vector<int> > vect)
{
	for(int i = 0; i < vect.size(); i++)
	{
		for(int j = 0; j < vect[i].size(); j++)
		{
			std::cout << vect[i][j] << " ";
		}
		std::cout << std::endl;
	}
}
bool equal(std::vector<std::vector<int> > fullVect, std::vector<std::vector<int> > vect)
{
	bool equal = true;

	for(int i = 0; i < vect.size(); i++)
	{
		for(int j = 0; j < vect[i].size(); j++)
		{
			if(fullVect[i][j] != vect[i][j])
				return false;
		}
	}
	return true;
}
int findMax(std::vector<int> vect)
{
	int a = 0;
	 for(int i = 0; i < vect.size(); i++)
	 {
		 if(vect[i] > a)
			 a = vect[i];
	 }
	 return a;
}
std::string find(std::vector<std::vector<int> > vect)
{

	std::vector<std::vector<int> > fullVect;
	for(int i = 0; i < vect.size(); i++)
	{
		std::vector<int> temp;
		for(int j = 0; j < vect[i].size(); j++)
		{
			temp.push_back(100);
		}
		fullVect.push_back(temp);
	}

	for(int i = 0; i < vect.size(); i++)
	{
		int max = findMax(vect[i]);
		for(int j = 0; j < vect[i].size(); j++)
		{
			if(fullVect[i][j] > max)
			{
				fullVect[i][j] = max;
			}
		}
	}
	for(int i = 0; i < vect[0].size(); i++)
	{
		int max = 0;
		for(int j = 0; j < vect.size(); j++)
		{
			if(vect[j][i] > max)
			{
				max = vect[j][i];
			}
		}

		for(int j = 0; j < vect.size(); j++)
		{
			if(fullVect[j][i] > max)
			{
				fullVect[j][i] = max;
			}
		}
	}
	if(equal(fullVect, vect))
		return "YES";
	return "NO";
}

int main()
{
	std::ifstream fin;
	fin.open("B-large.in");
	if(fin.fail())
	{
		std::cout << "Fail..." << std::endl;
		return 0;
	}
	int num;
	fin >> num;
	//std::cin >> num;
	std::ofstream fout("B-large.out");
	for(int i = 0; i < num; i++)
	{
		int row, col;
		fin >> row;
		fin >> col;
		//std::cin >> row;
		//std::cin >> col;
		std::vector<std::vector<int> > vect;
		for(int j = 0; j < row; j++)
		{
			std::vector<int> temp;
			for(int k = 0; k < col; k++)
			{
				int t;
				fin >> t;
				//std::cin >> t;
				temp.push_back(t);
			}
			vect.push_back(temp);
		}

		
		std::string a = find(vect);
		
		fout <<"Case #"<< i+1 << ": " << a << std::endl;
		
	}
	fout.close();
	return 0;
}