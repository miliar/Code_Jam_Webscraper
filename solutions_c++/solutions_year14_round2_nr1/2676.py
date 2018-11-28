/*
 * repeater.cxx
 * 
 * Copyright 2014 Albert Benciho <albert.bendicho@gmail.com>
 * Sytems Engineer that likes challenges.
 * I am not a programer though, and that can be told in my code.
 * Also, the only C++ I have ever written is for CodeJam.
 * I am sure you can make this code waaay nicer and better.
 * Please, let me know if you ever watch/use/modify it.
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
#include <string>
#include <map>
#include <vector>
#include <set>
#include <algorithm>

int main()
{
    int T, t;
	int N, n;
	std::string s[100];

	int cl[100];
	
	std::cin >> T ;
	
	for ( t=1; t<=T; t++) {
		//clean 
		//read case
		std::cin >> N;
		for(n=0;n<N;n++) {
			std::cin >> s[n];
		}
		//calculate
		long long int changes=0;
		while(s[0].length()>0) {
			int maxcl;
			char currentchar=s[0][0];
			for(n=0;n<N;n++){
				maxcl=0;
				if(s[n][0]!=currentchar){changes=-1; n=N+1;s[0].clear() ;}
				else {
					cl[n]=0;
					while(s[n][0]==currentchar){
						cl[n]++;
						s[n].erase(s[n].begin());
					}
					maxcl=std::max(maxcl,cl[n]);
				}
			}
			if(changes!=-1){
				//cl loaded
				int minch=20000;
				for (int i=1; i<=maxcl;i++) {
					int currch=0;
					for(n=0;n<N;n++){
						currch+=abs(cl[n]-i);
					}
					if(currch<minch) {
						minch=currch;
					}
				}
				//opt len found
				changes+=minch;
			}
		}
		for(n=0;n<N;n++){
			if(s[n].length()!=0) {changes=-1;}
		}
		std::cout << "Case #" << t << ": ";
		//print result
		if(changes==-1) { std::cout<<"Fegla Won";}
		else { std::cout<<changes;}
		std::cout << "\n";
	}
}
