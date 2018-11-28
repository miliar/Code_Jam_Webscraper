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
#include <iomanip>
#include <cstdio>
using namespace std;
double calculate(double t, double prevB, double f, double c, double x){
	return t - (x-c)/prevB + x/(prevB+f);
}
int main(int argc, char **argv)
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int times;
	cin >> times;
	for(int time = 1; time <= times; time++){
		double t, c, f, x, b;
		b = 2.0;
		cin >> c >> f >> x;
		t = x / b;
		while(true){
			double t2 = calculate(t,b,f,c,x);
			b += f;
			if(t2 > t) break;
			t = t2;
		}
		cout << "Case #" << time << ": " << fixed << setprecision(7) << t << endl;
	}
	return 0;
}

