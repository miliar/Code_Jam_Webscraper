/*
 * =====================================================================================
 *
 *       Filename:  A.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  2013年04月27日 08时54分34秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  梁涛 (suck_it), liangtao90s@gmail.com
 *   Organization:  
 *
 * =====================================================================================
 */
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
		int T;
		cin >> T;
		for (int c = 1; c <= T; c++) {
				double r, t;
				cin >> r >> t;
				double ans = ((1-2*r) + sqrt((2*r-1)*(2*r-1) + 8*t)) / 4.0;
				long long res = ans;	
				for (res = res; true ; res--) {
						if (2*res*res + 2*(r-1)*res <=t)
								break;
				}
				cout << "Case #" << c << ": ";
				cout << res << endl;
		}
		return 0;
}

