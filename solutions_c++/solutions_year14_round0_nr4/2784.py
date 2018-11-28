/*
 * senza nome.cxx
 * 
 * Copyright 2014 Vaush Wolf <healtyerslord@gmail.com>
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
#include <algorithm>
#include <cstdio>
#include <vector>
#include <set>
using namespace std;
vector<double> pesi1v, pesi2v;
set<double> pesi1s, pesi2s;

int main(int argc, char **argv)
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int times = 1; times <= t; times++){
		int n;
		cin >> n;
		pesi1s.clear();
		pesi2s.clear();
		pesi1v.clear();
		pesi2v.clear();
		for(int i = 0; i < n; i++){
			double temp;
			cin >> temp;
			pesi1s.insert(temp);
			pesi1v.push_back(temp);
		}
		for(int i = 0; i < n; i++){
			double temp;
			cin >> temp;
			pesi2s.insert(temp);
			pesi2v.push_back(temp);
		}
		sort(pesi1v.begin(), pesi1v.end());
		sort(pesi2v.begin(), pesi2v.end());
		int p1, p2;
		p1 = p2 = 0;
		for(int block = n-1; block >= 0; block--){
			set<double>::iterator pt = pesi1s.upper_bound(pesi2v[block]);
			if(pt == pesi1s.end()){
				pesi1s.erase(pesi1s.upper_bound(-1));
			}else{
				pesi1s.erase(pt);
				p1++;
			}
		}
		
		for(int block = n-1; block >= 0; block--){
			set<double>::iterator pt = pesi2s.upper_bound(pesi1v[block]);
			if(pt == pesi2s.end()){
				pesi2s.erase(pesi2s.upper_bound(-1));
				p2++;
			}else{
				pesi2s.erase(pt);
			}
		}
		cout << "Case #" << times << ": " << p1 << " " << p2 << endl;
	}
				
	return 0;
}

