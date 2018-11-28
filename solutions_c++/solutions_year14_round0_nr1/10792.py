/*
 * coba.cpp
 * 
 * Copyright 2014 Unknown <ropy@just-linux>
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


#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>      

int main () {
  
  freopen("A-small-attempt0.in", "r", stdin); 
  freopen("small0.txt", "w", stdout);
  
  int Grid1[4][4];
  int Grid2[4][4];
  int thePosition1, thePosition2; 
  int _T;
  scanf("%d", &_T);
  for(int _t = 1; _t <= _T; ++_t) 
  {
	scanf("%d", &thePosition1);
    for(int i=0;i<4;++i){		
		for(int j=0;j<4;++j){			
	   	  scanf("%d", &Grid1[i][j]);
		}
	} 
	  
	scanf("%d", &thePosition2);
	for(int i=0;i<4;++i){		
		for(int j=0;j<4;++j){			
	   	  scanf("%d", &Grid2[i][j]);
		}
	} 
	
	int first[4],second[4];
	for(int j=0;j<4;++j){			
	   	  first [j]= Grid1[thePosition1-1][j];
	   	  second[j]= Grid2[thePosition2-1][j];
		}
	
	std::vector<int> v(8);                      
	std::vector<int>::iterator it;

	std::sort (first,first+4);     
	std::sort (second,second+4);  

	it=std::set_intersection (first, first+5, second, second+5, v.begin());
  
	v.resize(it-v.begin());

	if(v.size()== 0) printf("Case #%d: Volunteer cheated!\n", _t);
	if(v.size()>  1) printf("Case #%d: Bad magician!\n", _t); 
	if(v.size()== 1) { it=v.begin(); printf("Case #%d: %d\n", _t, *it);  } 
	     
  }
  return 0;
}
