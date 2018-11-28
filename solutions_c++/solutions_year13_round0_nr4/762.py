#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <map>
#include <fstream>
#include <algorithm>
#include <utility>

struct chest_s
{
	int key_number;
	std::vector<int> keys;
};

bool have_some_keys(const std::map<int,int>& my_keys)
{
	for(auto c : my_keys)
	{
		if(c.second > 0) return true;
	}

	return false;
}

bool enough_keys( const std::vector<chest_s>& my_chests, std::map<int,int> my_keys)
{
	std::map<int,int> need;
	for(auto c : my_chests)
	{
		need[c.key_number]++;
		for(auto k : c.keys)
		{
			my_keys[k]++;
		}
	}

	for(auto c: need)
	{
		if(c.second > my_keys[c.first])
			return false;
	}

	return true;
}

#include <set>

bool new_keys(const std::map<int,int>& my_keys, const std::set<int>& keys)
{
	for(auto c : keys)
	{
		if(my_keys.find(c) == my_keys.end() || my_keys.at(c) == 0) return true;
	}

	return false;
}

bool is_stuck(const std::vector<int>& to_open, const std::vector<int>& can_open, const std::map<int,int>& my_keys, const std::vector<chest_s>& my_chests)
{
	if(to_open.size() == can_open.size()) return false;

	std::set<int> keys;
	for(auto c : can_open)
	{
		for(auto k : my_chests[c].keys)
		{
			keys.insert(k);
		}
	}

	return !new_keys(my_keys,keys);
}

std::vector<int> chest_i_can_open(const std::map<int,int>& my_keys, const std::vector<chest_s>& my_chests, const std::vector<int>& to_open)
{
	std::vector<int> res;
	unsigned int cpt = 0;

	for(auto c : my_chests)
	{
		if(my_keys.find(c.key_number) != my_keys.end() && my_keys.at(c.key_number) > 0)
		{
			if(std::find(to_open.begin(), to_open.end(), cpt) != to_open.end())
				res.push_back(cpt);
		}

		++cpt;
	}

	return res;
}

std::vector<int> solve(std::map<int,int> my_keys, const std::vector<chest_s>& my_chests, std::vector<int> to_open, int number)
{
	my_keys[my_chests[number].key_number]--;
	to_open.erase(std::find(to_open.begin(),to_open.end(), number));
	std::cout << "Opened " << number << " with " << to_open.size() << " to open" << std::endl;
	if(to_open.empty())
	{
		std::vector<int> res;
		res.push_back(number);
		return res;
	}

	for(auto c : my_chests[number].keys)
	{
		my_keys[c]++;
	}

	if(!have_some_keys(my_keys))
	{
		std::vector<int> res;
		return res;
	}

	auto remaining_chest = chest_i_can_open(my_keys,my_chests, to_open);

	std::vector<int> res;

	if(is_stuck(to_open,remaining_chest,my_keys,my_chests)) return res;

	for(auto c : remaining_chest)
	{
		res = solve(my_keys,my_chests,to_open,c);
		if(!res.empty()) break;
	}

	if(!res.empty()) res.push_back(number);;

	return res;
}



int main()
{
	std::ifstream file("D-small-attempt1.in", std::ifstream::in);
	std::ofstream file2("out.txt", std::ofstream::out);

	int nb;
	file >> nb;

	for(int j = 0; j < nb; ++j)
	{
		int keys, chest;
		file >> keys;
		file >> chest;

		std::map<int,int> my_keys;
		std::vector<chest_s> my_chests;
		for(int n =0; n < keys; n++)
		{
			int key;

			file >> key;
			if(my_keys.find(key) == my_keys.end()) my_keys[key] = 1;
			else my_keys[key]++;
		}

		std::vector<int> chest_to_open(chest);
		for(int n =0; n < chest; n++)
		{
			chest_s c;

			file >> c.key_number;
			int number_key;

			file >> number_key;
			for(int cpt = 0; cpt < number_key; ++cpt)
			{
				int tmp;
				file >> tmp;

				c.keys.push_back(tmp);
			}
			my_chests.push_back(c);
			chest_to_open[n] = n;
			// I'm making a note here : Huge Success
		}

		std::vector<int> res;

		if(enough_keys(my_chests,my_keys))
		{

			auto remaining_chest = chest_i_can_open(my_keys,my_chests, chest_to_open);

			for(auto c : remaining_chest)
			{
				res = solve(my_keys,my_chests,chest_to_open,c);
				if(!res.empty()) break;
			}
		}

		if(res.empty()) file2 << "Case #" << j + 1 << ": IMPOSSIBLE"  << std::endl;
		else
		{
			file2 << "Case #" << j + 1 << ":";
			for(std::vector<int>::reverse_iterator it = res.rbegin(); it != res.rend(); ++it)
			{
				file2 << " " << (*it) + 1;
			}
			file2 << std::endl;
		}

	}
}