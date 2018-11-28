#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <sstream>
#include <string>

typedef std::map<int,int> map;
typedef map::iterator mapit;

class SetOfDiners 
{
public:
	int m_time_spent;
	std::map<int,int> m_map;
public:
	SetOfDiners() : m_time_spent(0) { };
	
	int timespent() const { 
		return m_time_spent;
	}
	
	void adddiner(int stacksize)
	{
		m_map[stacksize] += 1;
	}
	
	void normalminute()
	{
		for( mapit it = m_map.begin(); it != m_map.end(); it++)	
		{
			int size = it->first, count = it->second;
			m_map[ size ] = 0;
			m_map[ size - 1 ] += count;
		}
		m_time_spent++;
		clean();
	}
	
	int biggeststack() const
	{
		return ( m_map.size() == 0 ? 0 : m_map.rbegin()->first );
	}
	
	void specialminute(int splitsize)
	{
		// Leaves splitsize 
		int stack = m_map.rbegin()->first;
		(m_map.rbegin()->second)--;
		
		m_map[ splitsize ] += 1;
		m_map[ stack - splitsize ] += 1;
		
		m_time_spent++;
		clean();
	}
	
	void clean()
	{
		for( map::iterator it = m_map.begin(); it != m_map.end(); it++ )
		{
			if ( it->first == 0 || it->second == 0 ) m_map.erase( it );
		}
	}
	
	void print() const
	{
		std::cout << hash() << std::endl;
	}

	std::string hash() const
	{
		std::stringstream r;
		for( std::map<int,int>::const_iterator it = m_map.begin(); it != m_map.end(); it++)
		{
			r << it->first << "^" << it->second << ",";
		}
		return r.str();
	}
	

};

std::map< std::string, int > memory;

int backtracksearch( const SetOfDiners& s )
{
	std::string hash = s.hash();
	if ( memory.find( hash ) != memory.end() )
	{
		return memory.find( hash )->second;
	}

	int returnvalue = s.biggeststack() + s.timespent();
	
	if ( s.biggeststack() > 0 )
	{
		// Normal minute
		{
			SetOfDiners s2 = s;
			s2.normalminute();
			int s = backtracksearch( s2 );
			if ( s < returnvalue ) returnvalue = s;
		}
		// Special minute
		int bs = s.biggeststack();
		for(int i = 1; i <= bs/2; i++)
		{
			SetOfDiners s2 = s;
			s2.specialminute( i );
			int s = backtracksearch( s2 );
			if ( s < returnvalue ) returnvalue = s;
		}
	}
	
	memory.insert( std::make_pair( hash, returnvalue ) );
	return returnvalue;
}

int testcase()
{
	SetOfDiners diners;

	// read data
	{
		int ndiners;
		std::cin >> ndiners;
		for(int i=0;i<ndiners;i++)
		{
			int k;
			std::cin >> k;
			diners.adddiner(k);
		}
	}
	
	// do the search
	memory.clear();
	int r = backtracksearch( diners );
	return r;
} 

int main()
{
	int n;
	std::cin >> n;
	
	for (int i = 0; i < n; i++)
	{
		int r = testcase();
		std::cout << "Case #" << i+1 << ": " << r << std::endl;
	}
	
	return 0;
}