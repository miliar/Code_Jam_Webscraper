/*
 * untitled.cxx
 * 
 * Copyright 2013 Vipul <vipul@vipul-Ubuntu>
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

using namespace std;

int main(int argc, char **argv)
{
	ifstream input("B-small-attempt1.in");
	ofstream output("output1");
	
	int cases = 0;
	int iterator = 0;
	int n, m;
	input >> cases;
	while(++iterator <= cases) {
		input >> n;
		input >> m;
		//flags
		int flag = 1;
		int flag1 = 1, flag2 =1;
		//get input
		int array[n][m];
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				input >> array[i][j];
				
		//for each number
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				flag = 1;	
				//if number is 1
				if(array[i][j] == 1) {
					flag1 = 1;
					flag2 =1;
					//check if that whole column is 1
					for(int a = 0; a < n; a++)
						if(array[a][j] != 1) {
							flag1 = 0;
							break;
						}
					//check if that whole row is 1
					for(int a = 0; a < m; a++)
						if(array[i][a] != 1) {
							flag2 = 0;
							break;
						}
					
					if(!(flag1 || flag2)){
						output << "Case #"<<iterator<<": NO\n";
						flag = 0;
						break;
					}
				}
			}
			if(!flag)
				break;
		}
		if(flag)
			output << "Case #"<<iterator<<": YES\n";
				
	}
	input.close();
	output.close();
	return 0;
}

