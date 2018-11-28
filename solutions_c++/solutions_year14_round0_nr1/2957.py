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
#include <cstdio>
using namespace std;
int arr1[4];
int arr2[4];
int a1, a2;
int main(int argc, char **argv)
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int times = 1; times <= t; times++){
		cin >> a1;
		for(int i = 1; i <= 4; i++){
			for(int j = 0; j < 4; j++){
				if(a1 == i){
					cin >> arr1[j];
				}else{
					cin >> *(new int);
				}
			}
		}
		cin >> a2;
		for(int i = 1; i <= 4; i++){
			for(int j = 0; j < 4; j++){
				if(a2 == i){
					cin >> arr2[j];
				}else{
					cin >> *(new int);
				}
			}
		}
		int c = 0;
		int card = -1;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(arr1[i] == arr2[j]){
					c++;
					card = arr1[i];
				}
			}
		}
		cout << "Case #" << times << ": ";
		if(c == 0) cout << "Volunteer cheated!" << endl;
		else if(c == 1) cout << card << endl;
		else cout << "Bad magician!" << endl;
	}
	return 0;
}

