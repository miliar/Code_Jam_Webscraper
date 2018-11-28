/*
 * A.cxx
 * 
 * Copyright 2013 aras <aras@aras-Satellite-C645D>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char **argv)
{
	int T,N,M,X[107][107],test = 1;

	ifstream IN("B-large.in");
	ofstream OUT("b.out");
	
	IN >> T;
	
	while(T--)
	{
		IN >> N >> M;
		
		for(int i = 0;i < N;i++)
			for(int j = 0;j < M;j++)
				IN >> X[i][j];
				
		bool possible = true;
		
		for(int i = 0;i < N;i++)
			for(int j = 0;j < M;j++)
			{
				bool _possible = false;
				
				int _max = 0;
				for(int k = 0;k < N;k++)
					_max = max(_max , X[k][j]);
					
				_possible |= _max == X[i][j];
					
				_max = 0;
				for(int k = 0;k < M;k++)
					_max = max(_max , X[i][k]);
					
				_possible |= _max == X[i][j];
				
				possible &= _possible;
			}

		cout << "Case #" << test << ": " << (possible ? "YES" : "NO") << endl;
		OUT << "Case #" << test++ << ": " << (possible ? "YES" : "NO") << endl;
	}
	
	return 0;
}

