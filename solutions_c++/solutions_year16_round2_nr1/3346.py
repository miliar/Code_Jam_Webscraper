#include <iostream> 
#include <string>
#include <list>
#include <sstream> 
#include <vector>
#include <map>

using namespace std;
map<char,int> map_character;

void InsertMap(char c)
{
	map<char,int>::iterator it;
	it = map_character.find(c);
	if (it == map_character.end())
		map_character[c] = 1;
	else
		(it->second)++;
}
int FindDigit()
{
	map<char,int>::iterator it;
	it = map_character.find('Z');
	if(it != map_character.end())
	{
		//map_character.erase (it);
		if(map_character['Z'] == 1)
			map_character.erase('Z');
		else
			map_character['Z'] = map_character['Z'] - 1;
		map<char,int>::iterator itr;
		itr = map_character.find('O');
		if(itr == map_character.end())
			return 0;
		if(map_character['O'] == 1)
			map_character.erase('O');
		else
			map_character['O'] = map_character['O'] - 1;
		return 0;
	}
	it = map_character.find('W');
	if(it != map_character.end())
	{
		//map_character.erase (it); 
		if(map_character['W'] == 1)
			map_character.erase('W');
		else
			map_character['W'] = map_character['W'] - 1;
		map<char,int>::iterator itr;
		itr = map_character.find('O');
		if(itr == map_character.end())
			return 2;
		if(map_character['O'] == 1)
			map_character.erase('O');
		else
			map_character['O'] = map_character['O'] - 1;
		return 2;
	}
	it = map_character.find('U');
	if(it != map_character.end())
	{
		//map_character.erase (it); 
		if(map_character['U'] == 1)
			map_character.erase('U');
		else
			map_character['U'] = map_character['U'] - 1;
		map<char,int>::iterator itr;
		itr = map_character.find('O');
		if(itr == map_character.end())
			return 4;
		if(map_character['O'] == 1)
			map_character.erase('O');
		else
			map_character['O'] = map_character['O'] - 1;
		itr = map_character.find('F');
		if(itr == map_character.end())
			return 4;
		if(map_character['F'] == 1)
			map_character.erase('F');
		else
			map_character['F'] = map_character['F'] - 1;
		return 4;
	}
	it = map_character.find('X');
	if(it != map_character.end())
	{
		//map_character.erase (it); 
		if(map_character['X'] == 1)
			map_character.erase('X');
		else
			map_character['X'] = map_character['X'] - 1;
		map<char,int>::iterator itr;
		itr = map_character.find('S');
		if(itr == map_character.end())
			return 6;
		if(map_character['S'] == 1)
			map_character.erase('S');
		else
			map_character['S'] = map_character['S'] - 1;
		return 6;
	}
	it = map_character.find('G');
	if(it != map_character.end())
	{
		//map_character.erase (it); 
		if(map_character['G'] == 1)
			map_character.erase('G');
		else
			map_character['G'] = map_character['G'] - 1;
		map<char,int>::iterator itr;
		itr = map_character.find('H');
		if(itr == map_character.end())
			return 8;
		if(map_character['H'] == 1)
			map_character.erase('H');
		else
			map_character['H'] = map_character['H'] - 1;
		return 8;
	}
	it = map_character.find('O');
	if(it != map_character.end())
	{
		//map_character.erase (it); 
		if(map_character['O'] == 1)
			map_character.erase('O');
		else
			map_character['O'] = map_character['O'] - 1;
		map<char,int>::iterator itr;
		itr = map_character.find('N');
		if(itr == map_character.end())
			return 1;
		if(map_character['N'] == 1)
			map_character.erase('N');
		else
			map_character['N'] = map_character['N'] - 1;
		return 1;
	}
	it = map_character.find('H');
	if(it != map_character.end())
	{
		//map_character.erase (it); 
		if(map_character['H'] == 1)
			map_character.erase('H');
		else
			map_character['H'] = map_character['H'] - 1;
		return 3;
	}
	it = map_character.find('F');
	if(it != map_character.end())
	{
		//map_character.erase (it); 
		if(map_character['F'] == 1)
			map_character.erase('F');
		else
			map_character['F'] = map_character['F'] - 1;
		return 5;
	}
	it = map_character.find('S');
	if(it != map_character.end())
	{
		//map_character.erase (it); 
		if(map_character['S'] == 1)
			map_character.erase('S');
		else
			map_character['S'] = map_character['S'] - 1;
		map<char,int>::iterator itr;
		itr = map_character.find('N');
		if(itr == map_character.end())
			return 7;
		if(map_character['N'] == 1)
			map_character.erase('N');
		else
			map_character['N'] = map_character['N'] - 1;
		return 7;
	}
	it = map_character.find('N');
	if(it != map_character.end())
	{
		if(map_character['N'] == 2)
			map_character.erase('N');
		else
			map_character['N'] = map_character['N'] - 2;
		//map_character.erase (it); 

		return 9;
		
	}
	return -1;
}
void main(){
	int N, return_num;
	string str;
	list<int> lst_numbers;
	cin >> N;
	for (int i=0; i < N; i++)
	{
		lst_numbers.clear();
		map_character.clear();
		str = "";
		cin >> str;
		for(int j=0; j < str.size(); j++)
		{
			InsertMap(str[j]);
		}
		return_num = FindDigit();
		while(return_num != -1)
		{
			lst_numbers.push_back(return_num);
			return_num = FindDigit();
		}
		lst_numbers.sort();
		cout<<"Case #"<<i+1<<": ";
		for(list<int>::iterator it=lst_numbers.begin(); it != lst_numbers.end(); it++)
		{	
			cout<<*it;
		}
		cout<<endl;
	}
}

