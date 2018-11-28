#include "stdafx.h"


#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <sstream>
#include <string>
#include <bitset>

typedef unsigned long long ull;

class Configuration
{
public:
	int m_R; 
	int m_C;
	std::bitset<16> m_used;
	
	Configuration(int R, int C, ull val) 
		: m_R(R), m_C(C), m_used( val ) {};
	
	// index i corresponds to column (i mod C) and row (i div C)
	int cell_to_index( int r, int c )
	{
		if ( r >= m_R || r < 0 || c >= m_C || c < 0 ) 
			return -1;
		return r*m_C + c;
	}
	int cell_exists_and_occupied( int r, int c )
	{
		int j = cell_to_index( r, c );
		return j != -1 && m_used[j];
	}

	ull nr_edges_shared()
	{
		ull ret = 0;
		for(int i = 0; i < m_R*m_C; i++)
		{
			if ( !m_used[i] ) continue;
			int r = i / m_C; int c = i % m_C;
			if ( cell_exists_and_occupied( r + 1, c ) ) ret++;
			if ( cell_exists_and_occupied( r, c + 1 ) ) ret++;
		}
		
		return ret;
	}
	
	void print()
	{
		std::cout << "Configuration R " << m_R << " C " << m_C << " nr edg " << nr_edges_shared() << std::endl;
		for( int i = 0 ; i < m_R; i++)
		{
			std::cout << " ";
			for(int j = 0; j < m_C; j++)
			{
				std::cout << m_used[i*m_C + j];
			}
			std::cout << std::endl;
		}
	}
	
};

int bruteforce() 
{
	unsigned int R, C, N;
	std::cin >> R >> C >> N;
	
	ull best = N*N;
	Configuration bestC(0,0,0);
	
	ull options = 1 << R*C;
	for( ull o = 0; o <= options; o++ )
	{
		Configuration c(R, C, o );
		if ( c.m_used.count() == N )
		{
			ull shared = c.nr_edges_shared();
			if ( shared < best ) 
			{
				best = shared;
				bestC = c;
			}
		}
	}
	
	return best;
}

int main()
{
	int n;
	std::cin >> n;
	
	for (int i = 0; i < n; i++)
	{
		int r = bruteforce();
		std::cout << "Case #" << i+1 << ": " << r << std::endl;
	}
	
	return 0;
}