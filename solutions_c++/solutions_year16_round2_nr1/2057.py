#include<algorithm>
#include<array>
#include<bitset>
#include<cstring>
#include<deque>
#include<functional>
#include<fstream>
#include<iomanip>
#include<iostream>
#include<iterator>
#include<limits>
#include<memory>
#include<queue>
#include<stack>
#include<string>
#include<unordered_map>
#include<unordered_set>
#include<utility>
#include<vector>
using namespace std;

int main()
{
	int T;
	ifstream ifs{"in"};
	ofstream ofs{"out"};
	ifs>>T;
	string waste;
	getline(ifs,waste);
	for(int case_i{0};case_i!=T;++case_i)
	{
		vector<int> vec;
		string str;
		getline(ifs,str);
		unordered_map<char,int> map;
		for(auto val:str)
			++map[val];
		if(map.find('G')!=map.end())
		{
			for(int i{0};i!=map['G'];++i)
				vec.emplace_back(8);
			map['E']-=map['G'];
			map['I']-=map['G'];
			map['H']-=map['G'];
			map['T']-=map['G'];
			map['G']=0;
		}
		if(map.find('X')!=map.end())
		{
			for(int i{0};i!=map['X'];++i)
				vec.emplace_back(6);
			map['S']-=map['X'];
			map['I']-=map['X'];
			map['X']=0;
		}
		if(map.find('U')!=map.end())
		{
			for(int i{0};i!=map['U'];++i)
				vec.emplace_back(4);
			map['F']-=map['U'];
			map['O']-=map['U'];
			map['R']-=map['U'];
			map['U']=0;
		}
		if(map.find('Z')!=map.end())
		{
			for(int i{0};i!=map['Z'];++i)
				vec.emplace_back(0);
			map['E']-=map['Z'];
			map['R']-=map['Z'];
			map['O']-=map['Z'];
			map['Z']=0;
		}
		if(map.find('W')!=map.end())
		{
			for(int i{0};i!=map['W'];++i)
				vec.emplace_back(2);
			map['T']-=map['W'];
			map['O']-=map['W'];
			map['W']=0;
		}
		if(map.find('H')!=map.end())
		{
			for(int i{0};i!=map['H'];++i)
				vec.emplace_back(3);
			map['T']-=map['H'];
			map['R']-=map['H'];
			map['E']-=map['H'];
			map['E']-=map['H'];
			map['H']=0;
		}
		if(map.find('S')!=map.end())
		{
			for(int i{0};i!=map['S'];++i)
				vec.emplace_back(7);
			map['E']-=map['S'];
			map['V']-=map['S'];
			map['E']-=map['S'];
			map['N']-=map['S'];
			map['S']=0;
		}
		if(map.find('V')!=map.end())
		{
			for(int i{0};i!=map['V'];++i)
				vec.emplace_back(5);
			map['F']-=map['V'];
			map['I']-=map['V'];
			map['E']-=map['V'];
			map['V']=0;
		}
		if(map.find('I')!=map.end())
		{
			for(int i{0};i!=map['I'];++i)
				vec.emplace_back(9);
			map['N']-=map['I'];
			map['E']-=map['I'];
			map['N']-=map['I'];
			map['I']=0;
		}
		if(map.find('O')!=map.end())
			for(int i{0};i!=map['O'];++i)
				vec.emplace_back(1);
		sort(begin(vec),end(vec));
		ofs<<"Case #"<<case_i+1<<": ";
		for(auto val:vec)
			ofs<<val;
		ofs<<endl;
	}
}